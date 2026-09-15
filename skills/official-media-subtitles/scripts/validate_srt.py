#!/usr/bin/env python3
"""Validate structural and timeline invariants of an SRT subtitle file."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


TIMECODE = r"(\d{2}):(\d{2}):(\d{2}),(\d{3})"
BLOCK_RE = re.compile(rf"^(\d+)\n{TIMECODE} --> {TIMECODE}\n(.+)$", re.DOTALL)


def to_ms(parts: tuple[str, str, str, str]) -> int:
    hours, minutes, seconds, millis = map(int, parts)
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis


def media_duration_ms(path: Path) -> int:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    duration = float(json.loads(result.stdout)["format"]["duration"])
    return round(duration * 1000)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("srt", type=Path)
    parser.add_argument("--media", type=Path)
    parser.add_argument("--max-chars", type=int, default=0)
    parser.add_argument(
        "--forbid-commas-periods",
        action="store_true",
        help="reject Chinese or ASCII commas and full stops in cue text",
    )
    args = parser.parse_args()

    text = args.srt.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    blocks = text.strip().split("\n\n") if text.strip() else []
    errors: list[str] = []
    warnings: list[str] = []
    previous_end = -1
    duration_limit = media_duration_ms(args.media) if args.media else None

    for expected, block in enumerate(blocks, 1):
        match = BLOCK_RE.fullmatch(block)
        if not match:
            errors.append(f"block {expected}: invalid format or empty cue")
            continue
        groups = match.groups()
        number = int(groups[0])
        start = to_ms(groups[1:5])
        end = to_ms(groups[5:9])
        cue_text = groups[9].strip()
        if number != expected:
            errors.append(f"block {expected}: number is {number}")
        if start < previous_end:
            errors.append(f"cue {number}: overlaps the previous cue")
        if end <= start:
            errors.append(f"cue {number}: end is not after start")
        if duration_limit is not None and end > duration_limit:
            errors.append(f"cue {number}: ends after the media")
        if not cue_text:
            errors.append(f"cue {number}: empty text")
        if args.forbid_commas_periods:
            found = sorted(set(cue_text) & set("，。,."))
            if found:
                errors.append(
                    f"cue {number}: contains forbidden comma or period: {''.join(found)}"
                )
        if args.max_chars and cue_text and max(map(len, cue_text.splitlines())) > args.max_chars:
            warnings.append(f"cue {number}: line exceeds {args.max_chars} characters")
        previous_end = end

    if not blocks:
        errors.append("no subtitle blocks found")

    print(f"cues={len(blocks)} errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
