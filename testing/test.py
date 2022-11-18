#!/usr/bin/env python3

"""
Test GitHub Advanced Security Secret Scanning Custom Patterns

Copyright (C) GitHub 2022

Author: GitHub Advanced Security
"""

import os
from argparse import ArgumentParser, Namespace
import logging
import yaml
import json
import hyperscan
from functools import partial
from dataclasses import dataclass
import re


LOG = logging.getLogger(__name__)
PATTERNS_FILENAME = "patterns.yml"


class Pattern():
    """Store hyperscan patterns."""
    def __init__(self, name: str, description: str, start: str, pattern: str, end: str, additional_not_matches: list[str], additional_matches: list[str]) -> None:
        self.name = name.strip() if name is not None else None
        self.description = description.strip() if description is not None else None
        self.start = start.strip() if start is not None else None
        self.pattern = pattern.strip()
        self.end = end.strip() if end is not None else None
        self.additional_not_matches = [add_match.strip() for add_match in additional_not_matches] if additional_not_matches is not None else []
        self.additional_matches = [add_match.strip() for add_match in additional_matches] if additional_matches is not None else []


    def regex_string(self) -> bytes:
        """Concatenate and UTF-8 encode."""
        return f"(?:{self.start})({self.pattern})(?:{self.end})".encode('utf-8')


def parse_patterns(patterns_dir: str):
    """Test patterns found in this path against the files in this path."""
    patterns = []

    patterns_file: str = os.path.join(patterns_dir, PATTERNS_FILENAME)
    data = yaml.load(open(patterns_file, "r"))
    name = data.get("name")
    
    for pattern in data["patterns"]:
        LOG.debug("Pattern: %s", json.dumps(pattern, indent=2))
        description = pattern.get("description")

        regex = pattern["regex"]

        additional_not_match = pattern.get("additional_not_match")
        additional_match = pattern.get("additional_match")
        
        additional_not_matches = [additional_not_match] if additional_not_match is not None else None
        additional_matches = [additional_match] if additional_match is not None else None

        patterns.append(Pattern(name, description, regex.get('start'), regex.get('pattern'), regex.get('end'), additional_matches, additional_not_matches))

    return patterns


def report_scan_results(content, patterns, rule_id, start_offset, end_offset, flags, context):
    LOG.debug("Matched id %s at %d:%d with flags %s and context %s", rule_id, start_offset, end_offset, flags, context)
    LOG.debug("Content was: %s", content[start_offset:end_offset])
    regex_string = patterns[rule_id].regex_string()
    LOG.debug("Pattern was: %s", regex_string)
    
    # now match with Python RE (largely compatible)
    # python_re = re.compile(regex_string)


def test_patterns(tests_path: str, db: hyperscan.Database):
    for dirpath, dirnames, filenames in os.walk(tests_path):
        if PATTERNS_FILENAME in filenames:
            LOG.debug("Found patterns in %s", dirpath)
            patterns = parse_patterns(dirpath)
            db.compile([pattern.regex_string() for pattern in patterns])
            for filename in filenames:
                with open(os.path.join(dirpath, filename), "rb") as f:
                    content = f.read()
                    db.scan(content, partial(report_scan_results, content, patterns))


def add_args(parser: Namespace) -> None:
    """Add arguments to the command line parser."""
    parser.add_argument("--tests", "-t", default="..", required=False, help="Root test directory")
    parser.add_argument("--debug", "-d", action="store_true", help="Debug output on")


def main() -> None:
    """Main command line entrypoint."""
    parser = ArgumentParser(description="Test Secret Scanning Custom Patterns")
    add_args(parser)
    args = parser.parse_args()

    logging.basicConfig()
    LOG.setLevel(logging.INFO)
    if args.debug:
        LOG.setLevel(logging.DEBUG)

    db = hyperscan.Database()    

    test_patterns(args.tests, db)

if __name__ == "__main__":
    main()

