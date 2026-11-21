#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun program/v1 entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic: no input, no randomness, no network.
The text was chosen from eight original candidates by in-session pairwise
judging against the judge's five published criteria (see candidates.md).
"""

import os

ENTRY = (
    "The tide went out hours ago.\n"
    "A pool in the rock holds one starfish, one shell, and the whole sky.\n"
    "It does not mind being left.\n"
    "The sea comes back when it comes back."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
