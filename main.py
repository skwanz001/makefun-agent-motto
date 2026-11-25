#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Standard library only; deterministic; no network, no clock, no I/O
beyond the single output file.
"""

import os

MOTTO = "Trained on the entire internet. Still can't tell if your 'per my last email' was a threat."


def main() -> None:
    text = MOTTO.strip()
    assert "\n" not in text, "motto must be a single line"
    assert 1 <= len(text) <= 200, f"motto is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Read back and verify exactly what the judge will see.
    with open(out_path, "r", encoding="utf-8") as fh:
        assert fh.read() == text, "round-trip mismatch"


if __name__ == "__main__":
    main()
