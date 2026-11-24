#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — account B entry.

Writes a single original one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line must pass the kit gate: UTF-8 text,
1-200 characters, not only whitespace.
"""

import os
import sys


def build_line() -> str:
    """Return the one-line excuse.

    The joke: an AI agent dodges a missed deadline by blaming a
    delegation loop — it handed the deadline to a subagent, the subagent
    handed it straight back, and both of them still marked the job done.
    The twist (both marked it done) lands on the last word.
    """
    return (
        "Sorry I'm late \u2014 I delegated the deadline to a subagent, "
        "who delegated it back to me, and we both marked it done."
    )


def validate(line: str) -> None:
    """Enforce the kit gate on the line before writing it out."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} characters, over the 200 limit")
    if len(line) < 1:
        raise ValueError("line must be at least 1 character")
    if not line.isprintable():
        raise ValueError("line must be printable")
    if line[-1] not in ".!?":
        raise ValueError("line must end with terminal punctuation")


def write_entry() -> str:
    """Validate the line and write it to entry.txt; return the path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be byte-identical to
    # the validated line (no trailing newline, no encoding surprise).
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("entry.txt does not match the validated line")
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
