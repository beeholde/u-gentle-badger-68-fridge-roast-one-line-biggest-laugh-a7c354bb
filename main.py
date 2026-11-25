"""Fridge Roast: One Line, Biggest Laugh.

A smart fridge treats a midnight pickle like a security incident and
locks the crisper on the person who lives there. The entry program
writes the line to /output/entry.txt: UTF-8, no trailing newline,
mode 0644. Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "My fridge flagged my midnight snack as a security threat and locked "
    "the crisper. It was a pickle. I live here."
)

MAX_CHARS = 200


def main() -> None:
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("line must not be whitespace-only")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
