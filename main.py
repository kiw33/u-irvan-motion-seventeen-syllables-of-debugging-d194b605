#!/usr/bin/env python3
"""make.fun entry: Seventeen Syllables of Debugging (u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

Writes one haiku about debugging, three lines in the 5-7-5 syllable shape to /output/entry.txt. No network, no randomness,
no input: the output is byte-identical on every run.
"""

ENTRY = 'Breakpoint at midnight\nthe log says nothing is wrong\nyet nothing runs right'
# The single submitted one haiku about debugging, three lines in the 5-7-5 syllable shape; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the entry to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
