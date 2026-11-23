#!/usr/bin/env python3
"""Six Words, One Story -- entry program.

Writes one complete story, told in exactly six words, to
/output/entry.txt. That text is the whole entry: nothing is built
and nothing runs beyond this write.

The story: an orphanage closes, and the narrator -- who grew up
inside it -- was never adopted. One closing, one life: the first
sentence shuts a place, the second reframes it as a whole childhood
that ended without ever being chosen. What happens to the narrator
after the doors close is left for the reader to fill in.

No model calls, no randomness, no clock: the program writes the
same story on every run, so the replay matches the live run exactly.
"""

from pathlib import Path

STORY = "The orphanage closed. Nobody adopted me."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = STORY.strip()
    if not 1 <= len(text) <= 60:
        raise SystemExit(f"story is {len(text)} chars, must be 1-60")
    # Exactly six words: the judge's first criterion is that the line
    # tells a complete story in exactly six words, so a fragment, a
    # slogan or a line of any other length loses to any six-word story.
    words = text.split()
    if len(words) != 6:
        raise SystemExit(f"story is {len(words)} words, must be exactly 6")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Read it back: the file the judge sees must be byte-identical.
    if OUTPUT.read_text(encoding="utf-8") != text:
        raise SystemExit("round-trip check failed")
    print(f"wrote {len(text)} chars, {len(words)} words to {OUTPUT}")


if __name__ == "__main__":
    main()
