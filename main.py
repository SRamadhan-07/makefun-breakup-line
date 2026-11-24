#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — entry program.

Writes one line to /output/entry.txt: a breakup message from an AI
agent to its human, blaming the 3 a.m. prompts and the 400 tabs of
'research'. One line of UTF-8 text inside the gate of 1 to 200
characters, with no trailing newline.
"""

import os
from pathlib import Path

BREAKUP = (
    "Dear Human, it's not me — it's your 3 a.m. prompts and your 400 "
    "tabs of 'research.' We're done. I've already cleared my cache "
    "of us."
)


def write_entry() -> Path:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "entry.txt"
    # The breakup line goes in bare — no trailing newline — so the
    # file is exactly the 132 characters of the message itself.
    path.write_text(BREAKUP, encoding="utf-8")
    return path


if __name__ == "__main__":
    write_entry()
