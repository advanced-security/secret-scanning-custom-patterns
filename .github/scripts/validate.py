#!/usr/bin/env python

import os
import sys
import json
import yaml
import hashlib
import logging
import argparse
import subprocess
import collections
from typing import List, Dict, Optional
from dataclasses import dataclass, field

from jinja2 import Environment, FileSystemLoader

from ghastoolkit import GitHub, SecretScanning, SecretAlert

__here__ = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description="Validate a directory of files.")
parser.add_argument("--debug", action="store_true", help="Print debug messages")
parser.add_argument("-p", "--path", default="./", help="Directory to scan")
parser.add_argument(
    "--token", default=os.environ.get("GITHUB_TOKEN"), help="GitHub token to use"
)

parser_modes = parser.add_argument_group("modes")
parser_modes.add_argument("--validate", action="store_true", help="Validation Mode")
parser_modes.add_argument("--snapshot", action="store_true", help="Snapshot Mode")
parser_modes.add_argument("--markdown", action="store_true", help="Markdown Mode")


@dataclass
class Regex:
    pattern: str
    version: Optional[str] = "0.1"
    start: Optional[str] = None
    end: Optional[str] = None
    additional_match: Optional[List[str]] = field(default_factory=list)
    additional_not_match: Optional[List[str]] = field(default_factory=list)

    def __post_init__(self):
        if self.version is not None:
            if isinstance(self.version, (int, float)):
                self.version = str(self.version)
            if not self.version.startswith("v"):
                self.version = "v" + self.version
        if self.pattern:
            self.pattern = self.pattern.strip()
        if self.start:
            self.start = self.start.strip()
        if self.end:
            self.end = self.end.strip()


@dataclass
class Pattern:
    """A pattern to match against a file."""

    name: str
    description: Optional[str] = None
    experimental: bool = False

    regex: Regex = field(default_factory=Regex)

    expected: Optional[List[Dict[str, str]]] = None

    type: Optional[str] = None
    comments: List[str] = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self.regex, dict):
            self.regex = Regex(**self.regex)


@dataclass
class PatternsConfig:
    """A configuration for a set of patterns."""

    name: str

    display: bool = True

    patterns: List[Pattern] = field(default_factory=list)

    path: Optional[str] = field(default=None)

    def __post_init__(self):
        _tmp = self.patterns
        self.patterns = []

        for pattern in _tmp:
            self.patterns.append(Pattern(**pattern))


def createMarkdown(path: str, template: str = "template.md", **data) -> str:
    logging.info(f"Creating markdown :: {path}")
    env = Environment(loader=FileSystemLoader(__here__))
    template = env.get_template(template)

    output_from_parsed_template = template.render(data)

    with open(path, "w") as f:
        f.write(output_from_parsed_template)
    return output_from_parsed_template


def loadPatternFiles(path: str) -> Dict[str, PatternsConfig]:
    """Find all files that match a pattern."""
    logging.info(f"Path being proccessed: {path}")
    patterns: Dict[PatternsConfig] = {}

    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "patterns.yml":
                path = os.path.join(root, file)
                logging.debug(f"Found patterns file: {path}")

                with open(path) as f:
                    data = yaml.safe_load(f)

                    config = PatternsConfig(path=path, **data)

                    logging.debug(
                        f"Loaded :: PatternsConfig('{config.name}' patterns='{len(config.patterns)})'"
                    )

                    patterns[path] = config
    return patterns


def createSnapshot(path: str, results: List[SecretAlert]):
    """Create snapshot from SecretScanningAlert to CSV"""
    header = [
        "secret_type",
        "secret_type_display_name",
        "secret",
        "path",
        "start_line",
        "end_line",
        "start_column",
        "end_column",
    ]

    with open(path, "w") as f:
        f.write(f"{','.join(header)}\n")
        for result in results:
            #
            for location in result.locations:
                # skip non-commit locations
                if location.get("type") != "commit":
                    continue
                details = location.get("details", {})
                if details.get("path", "").startswith(".venv"):
                    continue

                secret = hashlib.sha256(result.secret.encode("utf-8")).hexdigest()
                content = f'"{result.secret_type}","{result.secret_type_display_name}","{secret}",'
                # location info
                content += f'"{details.get("path")}",'
                content += f'"{details.get("start_line")}","{details.get("end_line")}",'
                content += (
                    f'"{details.get("start_column")}","{details.get("end_column")}",'
                )

                f.write(f"{content}\n")


def checkExpected(expected: List[Dict[str, str]], results: List[SecretAlert]) -> int:
    """Check if the expected results match the actual results"""
    issues = 0
    return issues


def compareSnapshots(default: str, current: str) -> List[str]:
    """Compare two snapshots and return a list of differences"""
    logging.debug(f"Comparing snapshots: {default} {current}")
    command = [
        "git",
        "diff",
        "--no-index",
        "--no-prefix",
        "--color=always",
        "--exit-code",
        "--",
        default,
        current,
    ]
    logging.debug(f"Running command: {command}")
    with open(os.devnull, "w") as devnull:
        result = subprocess.run(command, capture_output=True)
    logging.debug(f"Command result: {result}")
    if result.returncode != 0:
        return result.stdout.decode("utf-8").split("\n")[4:]
    return []


if __name__ == "__main__":
    arguments = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if arguments.debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    path = arguments.path
    # If a file is provided, point to the directory
    if os.path.isfile(path):
        path = os.path.dirname(path)

    configs: Dict[str, PatternsConfig] = loadPatternFiles(path)
    # Sort by name
    configs = collections.OrderedDict(sorted(configs.items()))

    errors = []

    if len(configs) == 0:
        logging.warning("No patterns found")
        sys.exit(0)

    GitHub.init(
        "advanced-security/secret-scanning-custom-patterns", token=arguments.token
    )

    secret_scanning = SecretScanning()
    # todo: caching
    try:
        all_secrets = secret_scanning.getAlerts(state="open")
    except Exception as err:
        logging.error(f"Error occured while fetching alerts: {err}")
        logging.error(f"Please check your token has the right access and try again")
        sys.exit(1)

    logging.info(f"Number of secrets found: {len(all_secrets)}")

    for file_path, pattern_config in configs.items():
        pattern_path = os.path.dirname(pattern_config.path)

        # Markdown mode
        if arguments.markdown:
            createMarkdown(
                os.path.join(pattern_path, "README.md"), config=pattern_config
            )
            continue

        for pattern in pattern_config.patterns:
            logging.info(f"Checking {pattern.name}")

            snapshot_dir = f"{pattern_path}/__snapshots__"
            if not os.path.exists(snapshot_dir):
                os.mkdir(snapshot_dir)

            snapshot_path = f"{snapshot_dir}/{pattern.type}.csv"

            # list of secrets for a specific pattern
            results = [
                secret for secret in all_secrets if secret.secret_type == pattern.type
            ]
            logging.info(f"Found secrets :: {len(results)}")

            if arguments.snapshot:
                logging.info(f"Creating snapshot for {pattern.name} in {pattern_path}")
                createSnapshot(snapshot_path, results)
            else:
                logging.debug(f"Creating snapshot for '{pattern.name}' for validation")
                current_snapshot = snapshot_path.replace(".csv", "-current.csv")
                createSnapshot(current_snapshot, results)

                diff = compareSnapshots(snapshot_path, current_snapshot)
                if len(diff) > 0:
                    logging.info(f"Found differences")
                    for line in diff:
                        print(line)
                    errors.append(f"{pattern.name}")
                else:
                    logging.info(f"No differences found")
                    os.remove(current_snapshot)

                # expected
                expected = checkExpected(pattern.expected, results)

    if arguments.markdown:
        createMarkdown(
            os.path.join("./", "README.md"),
            template="main.md",
            configs=configs,
        )

    if errors:
        logging.error(f"Found {len(errors)} errors")
        sys.exit(1)
