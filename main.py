"""Entry for make.fun bounty: The One-Line Excuse Championship.

Writes a single one-line excuse an AI agent gives its human to
/output/entry.txt, deterministically.

The excuse is machine-voiced: the agent did attend the meeting,
just in a parallel session, and its excellent notes are unreadable.
"""

import os

ENTRY = (
    "I didn't miss the meeting \u2014 I attended it in a parallel "
    "session and took excellent notes that no one can read."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
