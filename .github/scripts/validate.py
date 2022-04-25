#!/usr/bin/env python

import os
import sys
import json
import yaml
import hashlib
import logging
import argparse
import requests
import subprocess
from ratelimit import limits, sleep_and_retry
from typing import List, Dict, Optional
from dataclasses import dataclass

parser = argparse.ArgumentParser(description="Validate a directory of files.")
parser.add_argument("--debug", action="store_true", help="Print debug messages")
parser.add_argument("-p", "--path", default="./", help="Directory to scan")

parser_modes = parser.add_argument_group("modes")
parser_modes.add_argument("--validate", action="store_true")
parser_modes.add_argument("--snapshot", action="store_true")


@dataclass
class Regex:
    pattern: str
    start: Optional[str] = None
    end: Optional[str] = None
    additionals: List[str] = None


@dataclass
class Pattern:
    """A pattern to match against a file."""

    name: str
    regex: Regex
    path: str

    type: Optional[str] = None
    comments: Optional[List[str]] = None

    def __post_init__(self):
        if isinstance(self.regex, dict):
            self.regex = Regex(**self.regex)


@dataclass
class SecretScanningAlert:
    secret_type: str
    secret_type_display_name: str
    secret: str

    path: Optional[str] = None
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    start_column: Optional[int] = None
    end_column: Optional[int] = None


def loadPatternFiles(path: str) -> List[Pattern]:
    """Find all files that match a pattern."""
    patterns: List[Pattern] = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "patterns.yml":
                path = os.path.join(root, file)
                logging.debug(f"Found patterns file: {path}")

                with open(path) as f:
                    data = yaml.safe_load(f)

                    logging.debug(f"Loaded '{data.get('name')}'")

                    for pattern in data.get("patterns", []):
                        patterns.append(Pattern(path=path, **pattern))
    return patterns


@sleep_and_retry
@limits(calls=30, period=60)
def getSecretScanningLocations(url: str, token: str) -> Dict:
    """Get the locations of a secret scanning alert
    - https://docs.github.com/en/enterprise-cloud@latest/rest/secret-scanning#list-locations-for-a-secret-scanning-alert
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.secret-scanner-report-preview+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        error = f"Failed to get secret scanning results: {response.status_code}"
        logging.error(error)
        raise Exception(error)
    return response.json()


@sleep_and_retry
@limits(calls=30, period=60)
def getSecretScanningResults(
    owner: str, repo: str, token: str, secret_type: Optional[str] = None
) -> List[SecretScanningAlert]:
    """
    - https://docs.github.com/en/enterprise-cloud@latest/rest/secret-scanning#list-secret-scanning-alerts-for-a-repository
    """
    secrets: List[SecretScanningAlert] = []
    params = {}
    if secret_type:
        params["secret_type"] = secret_type
    url = f"https://api.github.com/repos/{owner}/{repo}/secret-scanning/alerts"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.secret-scanner-report-preview+json",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        error = f"Failed to get secret scanning results: {response.status_code}"
        logging.error(error)
        raise Exception(error)

    for secret in response.json():
        locations = getSecretScanningLocations(secret["locations_url"], token)
        for location in locations:
            location = location.get("details")
            secrets.append(
                SecretScanningAlert(
                    secret.get("secret_type"),
                    secret.get("secret_type_display_name"),
                    secret.get("secret"),
                    location.get("path"),
                    location.get("start_line"),
                    location.get("end_line"),
                    location.get("start_column"),
                    location.get("end_column"),
                )
            )
    return secrets


def createSnapshot(path: str, results: List[SecretScanningAlert]):
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
            # TODO: This might need to be removed
            if result.path.startswith(".venv"):
                continue
            secret = hashlib.sha256(result.secret.encode("utf-8")).hexdigest()
            content = ""
            for head in header:
                if head == "secret":
                    content += f'"{secret}"'
                else:
                    content += f'"{getattr(result, head) or ""}"'
                content += ","

            f.write(f"{content}\n")


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

    patterns: List[Pattern] = loadPatternFiles(arguments.path)

    errors = []

    if len(patterns) == 0:
        logging.warning("No patterns found")
        sys.exit(0)

    for pattern in patterns:
        logging.info(f"Checking {pattern.name}")
        pattern_path = os.path.dirname(pattern.path)

        snapshot_dir = f"{pattern_path}/__snapshots__"
        if not os.path.exists(snapshot_dir):
            os.mkdir(snapshot_dir)

        snapshot_path = f"{snapshot_dir}/{pattern.type}.csv"

        results = getSecretScanningResults(
            "advanced-security",
            "secret-scanning-custom-patterns",
            os.environ.get("GITHUB_TOKEN"),
            pattern.type,
        )
        logging.info(f"Found secrets :: {len(results)}")

        if arguments.snapshot:
            logging.info(f"Creating snapshot for {pattern.name} in {pattern_path}")
            createSnapshot(snapshot_path, results)
        else:
            logging.debug(f"Creating current snapshot for {pattern.name}")
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

    if errors:
        logging.error(f"Found {len(errors)} errors")
        sys.exit(1)
