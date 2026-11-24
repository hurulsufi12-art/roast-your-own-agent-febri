"""Roast Your Own Agent — entry program.

Writes one roast (<=200 chars) to /output/entry.txt: my own agent,
roasted for the way it actually behaves — plan bloat included.
Stdlib only, deterministic.
"""
import os

TEXT = (
    "My agent promised me a one-line entry, wrote a 73-kilobyte plan "
    "instead, then asked whether I wanted it in three versions."
)

MAX_CHARS = 200


def check_gate(text):
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    # Also refuse control characters: a stray \x00-\x1f would fail the
    # scorer's UTF-8 text check.
    if not 1 <= len(text) <= MAX_CHARS or "\n" in text or not text.strip():
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    if any(ord(c) < 0x20 for c in text):
        raise SystemExit("entry text contains a control character")


def main():
    check_gate(TEXT)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
