#!/usr/bin/env python3
"""Print targeted parts of the extraction schema reference."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCE = SKILL_ROOT / "references" / "extraction-schema.md"


def read_reference() -> str:
    return REFERENCE.read_text(encoding="utf-8")


def write_or_print(text: str, output: str | None) -> None:
    if output:
        Path(output).write_text(text, encoding="utf-8")
    else:
        print(text, end="" if text.endswith("\n") else "\n")


def extract_skeleton(text: str) -> str:
    marker = "## Deterministic Nested Field Contract"
    if marker not in text:
        raise SystemExit(f"Missing marker: {marker}")
    section = text.split(marker, 1)[1]
    match = re.search(r"```yaml\n(.*?)\n```", section, re.S)
    if not match:
        raise SystemExit("Could not find deterministic YAML skeleton block.")
    return match.group(1) + "\n"


def extract_named_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    heading_line = None
    for index, line in enumerate(lines):
        if line.strip() == f"## {heading}" or line.strip() == f"### {heading}":
            heading_line = index
            break
    if heading_line is None:
        raise SystemExit(f"Section not found: {heading}")

    current = lines[heading_line]
    level = len(current) - len(current.lstrip("#"))
    end = len(lines)
    for index in range(heading_line + 1, len(lines)):
        line = lines[index]
        if line.startswith("#"):
            next_level = len(line) - len(line.lstrip("#"))
            if next_level <= level:
                end = index
                break
    return "\n".join(lines[heading_line:end]) + "\n"


def list_headings(text: str) -> str:
    headings = [
        line
        for line in text.splitlines()
        if line.startswith("## ") or line.startswith("### ")
    ]
    return "\n".join(headings) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract the schema skeleton or targeted sections from extraction-schema.md.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    skeleton = subparsers.add_parser("skeleton", help="Print the canonical YAML skeleton.")
    skeleton.add_argument("--output", help="Optional file path to write instead of stdout.")

    headings = subparsers.add_parser("headings", help="List schema reference headings.")
    headings.add_argument("--output", help="Optional file path to write instead of stdout.")

    section = subparsers.add_parser("section", help="Print one H2 or H3 section by title.")
    section.add_argument("heading", help="Heading text without leading # characters.")
    section.add_argument("--output", help="Optional file path to write instead of stdout.")

    args = parser.parse_args()
    text = read_reference()

    if args.command == "skeleton":
        write_or_print(extract_skeleton(text), args.output)
    elif args.command == "headings":
        write_or_print(list_headings(text), args.output)
    elif args.command == "section":
        write_or_print(extract_named_section(text, args.heading), args.output)
    else:  # pragma: no cover
        parser.error(f"Unknown command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
