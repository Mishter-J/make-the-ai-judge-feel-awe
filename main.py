#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun program/v1 entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic: no input, no randomness, no network.
The text was chosen from eight original candidates by in-session pairwise
judging against the judge's five published criteria (see candidates.md).
"""

import os
import tempfile

ENTRY = (
    "The tide went out hours ago.\n"
    "A pool in the rock holds one starfish, one shell, and the whole sky.\n"
    "It does not mind being left.\n"
    "The sea comes back when it comes back."
)


def validate_entry(text: str) -> None:
    """Fail loudly if the entry breaks the competition's size rules.

    The entry must be 1-280 Unicode code points and not only whitespace.
    """
    n = len(text)
    if not 1 <= n <= 280:
        raise ValueError(f"entry must be 1-280 code points, got {n}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically: a partial write must never leave a truncated entry.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
