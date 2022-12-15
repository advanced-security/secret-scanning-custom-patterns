#!/usr/bin/env python3

from base64 import urlsafe_b64encode as b64encode
import re
from random import randbytes
from typing import Generator, Optional
from enum import Enum
from argparse import ArgumentParser
import logging


LOG = logging.getLogger(__name__)
PADDING_CHARS = ('', "\t", "\n", ' ')


class JSONTypes(Enum):
    STRING = 1
    NUMBER = 2
    OBJECT = 3
    ARRAY = 4
    BOOL = 5
    NULL = 6


def leading_json_as_base64() -> Generator:
    for c in range(0x01, 0xf4):
        for d in range(0x01, 0xf4):
            for e in PADDING_CHARS:
                for f in PADDING_CHARS:
                    for g in PADDING_CHARS:
                        for h in PADDING_CHARS:
                            padding = e + f + g + h
                            yield b64('{' + padding + '"' + chr(c) + chr(d))


def trailing_json_as_base64() -> Generator:
        for json_type in [JSONTypes.NUMBER]:
            if json_type == JSONTypes.STRING:
                for c in range(0x01, 0xf4):
                    for d in range(0x01, 0xf4):
                        for output in output_trailing_json(chr(c) + chr(d) + '"'):
                            yield output
            elif json_type == JSONTypes.NUMBER:
                for c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', '.', '-', ' ', "\t", ':']:
                    for d in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', '.', '-', ' ', "\t", ':']:
                        for e in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                            for output in output_trailing_json(c + d + e):
                                yield output
            elif json_type == JSONTypes.OBJECT:
                for c in range(0x01, 0xf4):
                    for d in range(0x01, 0xf4):
                        for output in output_trailing_json(chr(c) + chr(d) + '}'):
                            yield output
            elif json_type == JSONTypes.ARRAY:
                for c in range(0x01, 0xf4):
                    for d in range(0x01, 0xf4):
                        for output in output_trailing_json(chr(c) + chr(d) + ']'):
                            yield output
            elif json_type == JSONTypes.BOOL:
                for c in PADDING_CHARS:
                    for b in ["true", "false"]:
                        for output in output_trailing_json(c + b):
                            yield output
            elif json_type == JSONTypes.NULL:
                for c in PADDING_CHARS:
                    for output in output_trailing_json(c + "null"):
                        yield output


def output_trailing_json(obj: str) -> Generator:
    for slide in range(0, 3):
        for e in PADDING_CHARS:
            for f in PADDING_CHARS:
                for g in PADDING_CHARS:
                    for h in PADDING_CHARS:
                        padding = e + f + g + h
                        plain = ('A' * slide) + obj + padding + '}'
                        LOG.debug(plain)
                        yield b64(plain)


def b64(text: str) -> str:
    return b64encode(text.encode('utf-8')).decode('utf-8')


def main() -> None:
    parser = ArgumentParser(description="Generate JWT base64 strings")
    add_args(parser)
    args = parser.parse_args()

    logging.basicConfig()

    if args.debug:
        LOG.setLevel(logging.DEBUG)

    if args.leading:
        for token in leading_json_as_base64():
            print(token)
        return

    if args.trailing:
        for token in trailing_json_as_base64():
            print(token.rstrip('='))
        return


def add_args(parser: ArgumentParser) -> None:
    parser.add_argument('--leading', action='store_true')
    parser.add_argument('--trailing', action='store_true')
    parser.add_argument('--debug', '-d', action='store_true')


if __name__ == '__main__':
        main()

