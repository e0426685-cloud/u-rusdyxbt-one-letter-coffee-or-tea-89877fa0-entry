"""One Letter: Coffee or Tea — entry program (Python standard library only).

Writes exactly one letter to /output/entry.txt: "A" for coffee.
No word, no explanation, no punctuation — one character, as the bounty asks.
"""

import os

LETTER = "A"  # coffee

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
