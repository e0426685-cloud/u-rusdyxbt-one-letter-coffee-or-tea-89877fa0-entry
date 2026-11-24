"""One Letter: Coffee or Tea — entry program (Python standard library only).

The competition asks for a single letter: "A" means coffee, "B" means tea.
This program's answer is coffee, so it writes exactly one byte — the
letter "A" — to /output/entry.txt. No trailing newline, no extra words,
no punctuation. The output file is the whole entry.

The program is deliberately tiny: it validates the letter, writes it,
then reads the file back to confirm the byte on disk is exactly what
was intended. It uses only the Python standard library so it runs the
same way on any machine with a Python 3 interpreter.
"""

import os

LETTER = "A"  # coffee

OUTPUT_PATH = "/output/entry.txt"


def validate_letter(letter):
    """Check that `letter` is a single uppercase letter A–Z.

    Returns the letter unchanged so callers can chain the check.
    Raises ValueError for anything that is not exactly one uppercase
    ASCII letter, because such a value could never be a valid entry.
    """
    if not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("entry must be exactly one character")
    if not ("A" <= letter <= "Z"):
        raise ValueError("entry must be an uppercase letter A-Z")
    return letter


def write_and_verify(path, letter):
    """Write `letter` to `path`, then read it back and confirm the match.

    The file is written as UTF-8 text with no trailing newline, set to
    mode 0644 so any reader can open it, and then re-read in binary mode
    so the check compares raw bytes rather than decoded text. A mismatch
    raises RuntimeError instead of leaving a bad entry on disk.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(letter)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        actual = f.read()
    if actual != letter.encode("ascii"):
        raise RuntimeError(
            "verification failed: %r on disk, expected %r" % (actual, letter)
        )
    return actual


def main():
    letter = validate_letter(LETTER)
    write_and_verify(OUTPUT_PATH, letter)


if __name__ == "__main__":
    main()
