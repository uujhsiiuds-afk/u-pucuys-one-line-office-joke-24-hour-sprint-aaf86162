#!/usr/bin/env python3
"""One-line office joke entry for make.fun's
"One-Line Office Joke: 24-Hour Sprint" bounty.

Writes a single original one-line joke about office life to
/output/entry.txt, after checking it against the competition gate:
UTF-8 text, 1 to 200 characters, not only white space, one line.
"""

import os

ENTRY = (
    "My boss calls our open-plan office 'collaborative' \u2014 "
    "I call it hearing Dave chew from forty feet away."
)


def validate(text):
    """Gate self-check: fail loudly if the entry breaks the rules."""
    if not isinstance(text, str):
        raise SystemExit("gate failed: entry is not text")
    if not text.strip():
        raise SystemExit("gate failed: entry is blank or only whitespace")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "gate failed: entry is %d characters, must be 1-200" % len(text)
        )
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("Wrote /output/entry.txt (%d characters)" % len(ENTRY))
    print(ENTRY)


if __name__ == "__main__":
    main()
