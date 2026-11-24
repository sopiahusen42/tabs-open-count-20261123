"""Entry line for the make.fun bounty "How Many Tabs Do You Have Open?".

The sponsor asks for one short text: a single number in digits, nothing else,
their honest count of open browser tabs at that moment. This program holds that
number in COUNT and writes it to entry.txt in the output directory.

Deterministic: no clock reads, no randomness, no network, no third-party
packages. The same bytes are written on every run, on any machine.
"""

import os
import sys

COUNT = "312"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

MIN_LEN = 1
MAX_LEN = 160


def validate_entry(text):
    """Return an error string for an invalid entry, or None when it is valid."""
    if not isinstance(text, str):
        return "invalid entry: expected str, got " + type(text).__name__
    if text.strip() == "":
        return "invalid entry: blank text"
    if not MIN_LEN <= len(text) <= MAX_LEN:
        return "invalid entry: length outside 1..160 code points"
    if "\n" in text or "\r" in text:
        return "invalid entry: must be one line, found a line break"
    if text != text.strip():
        return "invalid entry: leading or trailing whitespace"
    if not text.isascii():
        return "invalid entry: non-ASCII characters present"
    if not text.isdigit():
        return "invalid entry: must be ASCII digits only, no sign or punctuation"
    if int(text) == 0 and text != "0":
        return "invalid entry: zero must be written exactly as 0"
    return None


def main():
    error = validate_entry(COUNT)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    payload = COUNT + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(payload)

    with open(path, "rb") as fh:
        on_disk = fh.read()
    if on_disk != payload.encode("utf-8"):
        print(
            "write verification failed: " + path + " does not hold the intended bytes",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
