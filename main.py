#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes a single one-line joke (136 characters) to /output/entry.txt,
the gate file for make.fun's One-Line Laugh-Off bounty
(u-zkhiel-one-line-laugh-off-714618ae).
"""

import os

JOKE = (
    "I asked the barber for something my wife would like. "
    "He gave me my father-in-law's 1987 cut — "
    "she's called me 'Dad' twice since Tuesday."
)


def main() -> None:
    # The gate reads exactly this file: one line, 1-200 chars, UTF-8.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
