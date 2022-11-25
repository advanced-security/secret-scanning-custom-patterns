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
RESULTS = {}


class Pattern():
    """Store hyperscan patterns."""

    default_start = '\A|[^0-9A-Za-z]'
    default_end = '\z|[^0-9A-Za-z]'

    def __init__(self, name: str, description: str, start: str, pattern: str, end: str,
            additional_not_matches: list[str], additional_matches: list[str], expected: list[dict[str, Any]]) -> None:
        self.name = name.strip() if name is not None else None
        self.description = description.strip() if description is not None else None
        self.start = start.strip() if start is not None else None
        self.pattern = pattern.strip()
        self.end = end.strip() if end is not None else None
        self.additional_not_matches = [add_match.strip() for add_match in additional_not_matches
                                      ] if additional_not_matches is not None else []
        self.additional_matches = [add_match.strip() for add_match in additional_matches
                                  ] if additional_matches is not None else []
        self.expected = expected

    def regex_string(self) -> bytes:
        """Concatenate and UTF-8 encode."""
        return f"({self.start if self.start is not None else Pattern.default_start})({self.pattern})({self.end if self.end is not None else Pattern.default_end})".encode('utf-8')

    def pcre_regex(self) -> pcre.Pattern:
        """Concatenate, label capture groups, and UTF-8 encode."""
        return pcre.compile(f"(?P<start>{self.start if self.start is not None else Pattern.default_start})(?P<pattern>{self.pattern})(?P<end>{self.end if self.end is not None else Pattern.default_end})".encode('utf-8'))


def parse_patterns(patterns_dir: str) -> list[Pattern]:
    """Parse patterns found in YAML files."""
    patterns = []

    patterns_file: str = os.path.join(patterns_dir, PATTERNS_FILENAME)
    data = yaml.safe_load(open(patterns_file, "r"))

    for pattern in data["patterns"]:
        LOG.debug("Pattern: %s", json.dumps(pattern, indent=2))

        name = pattern.get("name")
        description = pattern.get("description")

        regex = pattern["regex"]

        additional_not_matches = pattern.get("additional_not_match", [])
        additional_matches = pattern.get("additional_match", [])

        expected = pattern.get("expected", [])

        patterns.append(
            Pattern(name, description, regex.get('start'), regex.get('pattern'), regex.get('end'), additional_matches,
                    additional_not_matches, expected))

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
        except (hyperscan.error, TypeError):
            LOG.debug("Failed to compile rules")
            LOG.debug(regex_bytes)
            for r in regex_bytes:
                try:
                    db.compile(r)
                except (hyperscan.error, TypeError) as err:
                    LOG.error("❌ hyperscan error with '%s': %s", r, err)
            return False
    return True


# sideffect: writes to global RESULTS
def report_scan_results(patterns: list[Pattern], path: str, content: bytes, verbose: bool, quiet: bool, rule_id: int, start_offset: int, end_offset: int,
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
    pcre_result_match(pattern, path, match_content, start_offset, end_offset, verbose=verbose, quiet=quiet)


def path_offsets_match(first, second) -> bool:
    """Check file path and start and end offsets match."""
    for key in ('name', 'start_offset', 'end_offset'):
        if not first.get(key) == second.get(key):
            return False
    return True


# sideffect: writes to global RESULTS
def pcre_result_match(pattern: Pattern, path, content: bytes, start_offset: int, end_offset: int, verbose: bool=False, quiet: bool=False) -> None:
    """Use PCRE to extract start, pattern and end matches."""
    LOG.debug("Matching with PCRE regex: %s", str(pattern.pcre_regex()))

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
            'name': path.name,
            'start_offset': start_offset + len(m.group('start')),
            'end_offset': end_offset - len(m.group('end'))
        }

        if not any([path_offsets_match(file_details, loc) for loc in pattern.expected]):
            if not quiet:
                LOG.log(logging.ERROR if pattern.expected else logging.INFO, "%s result '%s' for '%s' in path '%s'; %s:%d-%d", "❌ unexpected" if pattern.expected else "ℹ️  found", parts['pattern'], pattern.name, path.parent, file_details['name'], file_details['start_offset'], file_details['end_offset'])
        else:
            if not quiet or LOG.level == logging.DEBUG:
                LOG.log(logging.INFO if verbose else logging.DEBUG, "✅ expected result '%s' for '%s' in path '%s'; %s:%d-%d", parts['pattern'], pattern.name, path.parent, file_details['name'], file_details['start_offset'], file_details['end_offset'])

        if pattern.name not in RESULTS:
            RESULTS[pattern.name] = []

        RESULTS[pattern.name].append({'file': file_details, 'groups': parts})

        LOG.debug((json.dumps({'name': pattern.name, 'file': file_details, 'groups': parts})))


def test_patterns(tests_path: str, verbose: bool=False, quiet: bool=False) -> bool:
    """Run all of the discovered patterns in the given path."""
    result = True

    if not os.path.isdir(tests_path):
        if not quiet:
            LOG.error("❌ testing directory not found: %s", tests_path)
        exit(1)

    db = hyperscan.Database()

    for dirpath, dirnames, filenames in os.walk(tests_path):
        if PATTERNS_FILENAME in filenames:
            rel_dirpath = Path(dirpath).relative_to(tests_path)
            LOG.debug("Found patterns in %s", rel_dirpath)

            patterns = parse_patterns(dirpath)
            if not hs_compile(db, [pattern.regex_string() for pattern in patterns]):
                if not quiet:
                    LOG.error("❌ hyperscan pattern compilation error in '%s'", rel_dirpath)
                    exit(1)
            for filename in [f for f in filenames if f != PATTERNS_FILENAME]:
                path = (Path(dirpath) / filename).relative_to(tests_path)
                with (Path(tests_path) / path).resolve().open("rb") as f:
                    content = f.read()
                    # sideffect: writes to global RESULTS
                    scan(db, path, content, patterns, verbose=verbose, quiet=quiet)

            for pattern in patterns:
                # did we match everything we expected?
                ok = True

                if pattern.expected:
                    for expected in pattern.expected:
                        if not any([path_offsets_match(expected, result.get('file', {})) for result in RESULTS.get(pattern.name, [])]):
                            if not quiet:
                                with (Path(dirpath) / expected.get('name', '')).resolve().open("rb") as f:
                                    content = f.read()
                                    LOG.error("❌ unmatched expected location for: '%s'; %s:%d-%d; %s", pattern.name, expected.get('name'), expected.get('start_offset'), expected.get('end_offset'), content[expected.get('start_offset', 0):expected.get('end_offset', 0)])
                            ok = False

                    # did we match anything unexpected?
                    if any([not any([path_offsets_match(expected, result.get('file', {})) for expected in pattern.expected]) for result in RESULTS.get(pattern.name, [])]):
                        if not quiet:
                            LOG.error("❌ matched unexpected results for: '%s'", pattern.name)
                        ok = False

                    if ok and not quiet:
                        LOG.info("✅ '%s' in '%s'", pattern.name, rel_dirpath)

                    if not ok:
                        result = False

                else:
                    if not quiet:
                        LOG.info("ℹ️  '%s' in '%s': no expected patterns defined", pattern.name, rel_dirpath)

    return result


# sideffect: writes to global RESULTS
def scan(db: hyperscan.Database, path: str, content: bytes, patterns: list[Pattern], verbose: bool=False, quiet: bool=False) -> None:
    """Scan content with database. I wanted to have this be an async function with a Future, but it didn't work."""
    db.scan(content, partial(report_scan_results, patterns, path, content, verbose, quiet))


def add_args(parser: ArgumentParser) -> None:
    """Add arguments to the command line parser."""
    parser.add_argument("--tests", "-t", default="..", required=False, help="Root test directory")
    parser.add_argument("--debug", "-d", action="store_true", help="Debug output on")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show expected matches")
    parser.add_argument("--quiet", "-q", action="store_true", help="Don't output anything other than exit error codes")


def check_platform() -> None:
    """Check we are on an Intel-compatible machine.

    Exit if not.
    """
    if platform.machine() not in ("x86_64", "amd64"):
        LOG.error("❌ cannot run hyperscan on non-Intel-compatible platform")
        exit(1)


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

    if not test_patterns(args.tests, verbose=args.verbose, quiet=args.quiet):
        exit(1)


if __name__ == "__main__":
    main()
