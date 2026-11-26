#!/usr/bin/env python3
"""The Printer Apology entry (program/v1).

Writes one original apology, as spoken by an office printer, to
/output/entry.txt. The apology is UTF-8 text of 1 to 120 characters,
a single line, with no trailing newline.
"""

import os

ENTRY_TEXT = "Sorry I jammed on your big day. The cheap paper, the shouting — I heard it all, and I promise to print like I mean it."

MAX_CHARS = 120
MIN_CHARS = 1

assert len(ENTRY_TEXT) <= MAX_CHARS, "entry exceeds the 120-character limit"


def write_entry(text, out_dir):
    """Write text to entry.txt inside out_dir (mode 0644) and return the path."""
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    # The sealed scorer gates on 1-120 characters; refuse to write
    # anything that would fail the gate instead of shipping it.
    if not MIN_CHARS <= len(ENTRY_TEXT) <= MAX_CHARS or not ENTRY_TEXT.strip():
        raise SystemExit("entry fails the 1-120 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
