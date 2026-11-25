#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Excuse My Agent Gave Me'.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human for a missed deadline. The joke grows out of the machine's own
condition -- a hallucinated calendar date -- delivered as a straight-faced
apology whose punch lands in the final words.
"""

import os
import sys

LINE = (
    "I missed the deadline because I confidently scheduled it for a date "
    "that doesn't exist \u2014 February 30th \u2014 and I was, technically, "
    "right on time."
)

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry line is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Read the file back and verify it round-trips exactly: the gate
    # scores the bytes on disk, so a silent write or encoding hiccup
    # would sink an otherwise valid entry.
    with open(out_path, "r", encoding="utf-8") as fh:
        on_disk = fh.read().rstrip("\n")
    if on_disk != text:
        print("written file does not match the entry line", file=sys.stderr)
        return 1
    print(f"wrote and verified {len(text)} chars in {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
