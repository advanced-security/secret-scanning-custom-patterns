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
from typing import Union


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
        return f"({self.start})({self.pattern})({self.end})".encode('utf-8')


def parse_patterns(patterns_dir: str):
    """Test patterns found in this path against the files in this path."""
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
        
        patterns.append(Pattern(name, description, regex.get('start'), regex.get('pattern'), regex.get('end'), additional_matches, additional_not_matches))

    return patterns


def compile(db: hyperscan.Database, regex: Union[str|list[str]]) -> bool:
    """Compile one or more hyperscan regexes into the given database."""
    if isinstance(regex, str):
        regex_bytes = [regex.encode('utf-8')]
    else:
        regex_bytes = [r.encode('utf-8') for r in regex]
    try:
        db.compile(regex_bytes, flags=hyperscan.HS_FLAG_SOM_LEFTMOST)
    except hyperscan.error as err:
        try:
            db.compile(regex_bytes)
        except hyperscan.error as err:
            LOG.error("Failed to compile rules")
            for r in regex_bytes:
                try:
                    db.compile(r)
                except hyperscan.error as err:
                    LOG.error("Hyperscan error with '%s': %s", r, err)
            return False
    return True


def report_scan_results(patterns, content, rule_id, start_offset, end_offset, flags, context):
    match_content = content[start_offset:end_offset]
    pattern = patterns[rule_id]
    
    LOG.debug("Matched '%s' id %d at %d:%d with flags %s and context %s", pattern.name, rule_id, start_offset, end_offset, flags, context)
    LOG.debug("Matched: %s", match_content)
     
    regex_string = pattern.regex_string()
    LOG.debug("Pattern was: %s", regex_string)

    # now do the start/pattern/end matches in sequence to understand the boundaries of the pattern match
    # it's a callback chain, from each db.scan(..., callback) call
    db_start = hyperscan.Database()
    if compile(db_start, pattern.start):
        db_start.scan(match_content, partial(handle_pattern_start, pattern, match_content))
    else:
        LOG.error('Error with start regex: %s', regex) 


def double_check_match(pattern: str, flags: int, start_offset: int, content: str) -> bool:
    if flags & hyperscan.HS_FLAG_SOM_LEFTMOST:
        if start_offset != 0:
            LOG.debug("Start offset is not zero: {:d}".format(start_offset))
            return False
    else:
        LOG.debug("This pattern may be over-matching, it does not report a start offset")

        # fall back to Python PCRE-bindings. This supports \Z, \A etc. that the native Python engine does not, and is mostly compatible with hyperscan
        import pcre
        regex = pcre.compile(pattern)
        if not regex.match(content):
            LOG.debug("False match")
            return False

    return True


def handle_pattern_start(pattern, content, rule_id, start_offset, end_offset, flags, context) -> None:
    match_content = content[start_offset:end_offset]
    
    LOG.debug("Matched id %s at %d:%d with flags %s and context %s", rule_id, start_offset, end_offset, flags, context)
    LOG.debug("Matched start: %s", match_content)

    if not double_check_match(pattern.start, flags, start_offset, content):
        return

    remaining_content = content[end_offset:]
    
    # pass on to the pattern match now
    db_pattern = hyperscan.Database()
    if compile(db_pattern, pattern.pattern):
        db_pattern.scan(remaining_content, partial(handle_pattern_match, pattern, remaining_content))
    else:
        LOG.error('Error with pattern regex: %s', pattern.pattern) 


def handle_pattern_match(pattern, content, rule_id, start_offset, end_offset, flags, context) -> None:
    match_content = content[start_offset:end_offset]
    
    LOG.debug("Matched id %s at %d:%d with flags %s and context %s", rule_id, start_offset, end_offset, flags, context)

    if not double_check_match(pattern.pattern, flags, start_offset, content):
        return

    LOG.debug("Matched pattern: %s", match_content)
    
    remaining_content = content[end_offset:]
    
    db_end = hyperscan.Database()

    if compile(db_end, pattern.end):
        db_end.scan(remaining_content, partial(handle_pattern_end, pattern, remaining_content))
    else:
        LOG.error('Error with end regex: %s', regex) 

 
def handle_pattern_end(pattern, content, rule_id, start_offset, end_offset, flags, context) -> None:
    match_content = content[start_offset:end_offset]
    
    LOG.debug("Matched id %s at %d:%d with flags %s and context %s", rule_id, start_offset, end_offset, flags, context)
    LOG.debug("Matched end: %s", match_content)

    if not double_check_match(pattern.end, flags, start_offset, content):
        return

    LOG.info("Total match!")
  
  
def test_patterns(tests_path: str, db: hyperscan.Database):
    for dirpath, dirnames, filenames in os.walk(tests_path):
        if PATTERNS_FILENAME in filenames:
            LOG.debug("Found patterns in %s", dirpath)
            patterns = parse_patterns(dirpath)
            try:
                db.compile([pattern.regex_string() for pattern in patterns], flags=hyperscan.HS_FLAG_SOM_LEFTMOST)
            except hyperscan.error as err:
                LOG.error("Hyperscan error: %s", err)
                for pattern in patterns:
                    try:
                        db.compile([pattern.regex_string()], flags=hyperscan.HS_FLAG_SOM_LEFTMOST)
                    except hyperscan.error as err:
                        LOG.error("Pattern error: %s", pattern.regex_string())
                exit
            for filename in filenames:
                with open(os.path.join(dirpath, filename), "rb") as f:
                    content = f.read()
                    db.scan(content, partial(report_scan_results, patterns, content))


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

