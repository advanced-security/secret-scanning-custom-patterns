#!/usr/bin/env python3
"""
Test GitHub Advanced Security Secret Scanning Custom Patterns

Copyright (C) GitHub 2022

Author: GitHub Advanced Security
"""

import os
from pathlib import Path
from argparse import ArgumentParser
import logging
import yaml
import json
import hyperscan
from functools import partial
import pcre
from typing import Union, Any, Optional
# from asyncio import Future, run, get_event_loop
import platform


LOG = logging.getLogger(__name__)
PATTERNS_FILENAME = "patterns.yml"


class Pattern():
    """Store hyperscan patterns."""

    def __init__(self, name: str, description: str, start: str, pattern: str, end: str,
                 additional_not_matches: list[str], additional_matches: list[str]) -> None:
        self.name = name.strip() if name is not None else None
        self.description = description.strip() if description is not None else None
        self.start = start.strip() if start is not None else None
        self.pattern = pattern.strip()
        self.end = end.strip() if end is not None else None
        self.additional_not_matches = [add_match.strip() for add_match in additional_not_matches
                                      ] if additional_not_matches is not None else []
        self.additional_matches = [add_match.strip() for add_match in additional_matches
                                  ] if additional_matches is not None else []

    def regex_string(self) -> bytes:
        """Concatenate and UTF-8 encode."""
        return f"({self.start})({self.pattern})({self.end})".encode('utf-8')

    def pcre_regex(self) -> pcre.Pattern:
        """Concatenate, label capture groups, and UTF-8 encode."""
        return pcre.compile(f"(?P<start>{self.start})(?P<pattern>{self.pattern})(?P<end>{self.end})".encode('utf-8'))


def parse_patterns(patterns_dir: str) -> list[Pattern]:
    """Parse patterns found in YAML files."""
    patterns = []

    patterns_file: str = os.path.join(patterns_dir, PATTERNS_FILENAME)
    data = yaml.safe_load(open(patterns_file, "r"))
    name = data.get("name")

    for pattern in data["patterns"]:
        LOG.debug("Pattern: %s", json.dumps(pattern, indent=2))
        description = pattern.get("description")

        regex = pattern["regex"]

        additional_not_matches = pattern.get("additional_not_match", [])
        additional_matches = pattern.get("additional_match", [])

        patterns.append(
            Pattern(name, description, regex.get('start'), regex.get('pattern'), regex.get('end'), additional_matches,
                    additional_not_matches))

    return patterns


def hs_compile(db: hyperscan.Database, regex: Union[str | list[str] | bytes | list[bytes]]) -> bool:
    """Compile one or more hyperscan regexes into the given database."""
    regex_bytes: list[bytes]

    if isinstance(regex, str):
        regex_bytes = [regex.encode('utf-8')]
    elif isinstance(regex, bytes):
        regex_bytes = [regex]
    elif isinstance(regex, list):
        if len(regex) == 0:
            return False

        if isinstance(regex[0], str):
            regex_bytes = [r.encode('utf-8') for r in regex]  # type: ignore
        elif isinstance(regex[0], bytes):
            regex_bytes = regex  # type: ignore
        else:
            raise ValueError("Regex is not a str or bytes")
    else:
        raise ValueError("Regex is not a str or bytes")
    try:
        db.compile(regex_bytes, flags=hyperscan.HS_FLAG_SOM_LEFTMOST)
    except hyperscan.error:
        try:
            db.compile(regex_bytes)
        except hyperscan.error:
            LOG.error("Failed to compile rules")
            for r in regex_bytes:
                try:
                    db.compile(r)
                except hyperscan.error as err:
                    LOG.error("Hyperscan error with '%s': %s", r, err)
            return False
    return True


def report_scan_results(patterns: list[Pattern], path: str, content: bytes, rule_id: int, start_offset: int, end_offset: int,
                        flags: int, context: Optional[Any]) -> None:
    """Hyperscan callback."""
    match_content: bytes = content[start_offset:end_offset]
    pattern: Pattern = patterns[rule_id]

    LOG.debug("Matched '%s' id %d at %d:%d with flags %s and context %s", pattern.name, rule_id, start_offset,
              end_offset, flags, context)
    LOG.debug("Matched: %s", match_content)

    regex_string: bytes = pattern.regex_string()
    LOG.debug("Pattern was: %s", regex_string)

    # extract separate parts of match using PCRE
    pcre_result_match(pattern, path, match_content, start_offset, end_offset)


def pcre_result_match(pattern: Pattern, path, content: bytes, start_offset: int, end_offset: int) -> None:
    """Use PCRE to extract start, pattern and end matches."""
    if m := pattern.pcre_regex().match(content):
        parts = {
            'start': m.group('start').decode('utf-8'),
            'pattern': m.group('pattern').decode('utf-8'),
            'end': m.group('end').decode('utf-8')
        }

        if pattern.additional_matches is not None:
            if not all([pcre.compile(pat).match(m.group('pattern')) for pat in pattern.additional_matches]):
                LOG.debug("One of the required additional pattern matches did not hold")
                return

        if pattern.additional_not_matches is not None:
            if any([pcre.compile(pat).match(m.group('pattern')) for pat in pattern.additional_not_matches]):
                LOG.debug("One of the additional NOT pattern matches held")
                return

        file_details = {
            'path': str(path),
            'start_offset': start_offset + len(m.group('start')),
            'end_offset': end_offset - len(m.group('end'))
        } 

        print(json.dumps({'name': pattern.name, 'file': file_details, 'groups': parts}))


def test_patterns(tests_path: str) -> None:
    """Run all of the discovered patterns in the given path."""
    db = hyperscan.Database()

    for dirpath, dirnames, filenames in os.walk(tests_path):
        if PATTERNS_FILENAME in filenames:
            LOG.debug("Found patterns in %s", dirpath)
            patterns = parse_patterns(dirpath)
            if not hs_compile(db, [pattern.regex_string() for pattern in patterns]):
                LOG.error("Hyperscan pattern compilation error")
                exit
            for filename in [f for f in filenames if f != PATTERNS_FILENAME]:
                path = (Path(dirpath) / filename).relative_to(tests_path)
                with (Path(tests_path) / path).open("rb") as f:
                    content = f.read()
                    scan(db, path, content, patterns)


def scan(db: hyperscan.Database, path: str, content: bytes, patterns: list[Pattern]) -> None:
    """Scan content with database. I wanted to have this be an async function with a Future, but it didn't work."""
    db.scan(content, partial(report_scan_results, patterns, path, content))


def add_args(parser: ArgumentParser) -> None:
    """Add arguments to the command line parser."""
    parser.add_argument("--tests", "-t", default="..", required=False, help="Root test directory")
    parser.add_argument("--debug", "-d", action="store_true", help="Debug output on")


def check_platform() -> None:
    """Check we are on an Intel-compatible machine.

    Exit if not.
    """
    if platform.machine() not in ("x86_64", "amd64"):
        LOG.error("Cannot run hyperscan on non-Intel-compatible platform")
        exit()


def main() -> None:
    """Main command line entrypoint."""
    check_platform()

    parser = ArgumentParser(description="Test Secret Scanning Custom Patterns")
    add_args(parser)
    args = parser.parse_args()

    logging.basicConfig()
    LOG.setLevel(logging.INFO)
    if args.debug:
        LOG.setLevel(logging.DEBUG)

    test_patterns(args.tests)


if __name__ == "__main__":
    main()
