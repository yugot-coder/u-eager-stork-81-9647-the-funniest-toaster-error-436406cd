"""The Funniest Toaster Error Message.

One line, at most 120 characters: the error message a kitchen toaster
shows its owner. Written from scratch in this session: several
candidates were weighed against the judge brief (a real toaster error
message, fresh surprise away from the obvious puns, tight, one clear
appliance voice, lands on a single read), and the strongest was
selected.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt) with no
trailing newline, so the file is exactly the line, byte for byte.
"""

import hashlib
import os

CANDIDATES = [
    # A 404 joke: funny, but the most obvious error-code gag in the
    # field, and it tells the user what to do instead of being the
    # joke itself.
    "ERROR 404: Bread not found. Please insert bread and lower your expectations.",
    # Modern and short, but "left the chat" is borrowed internet
    # slang, not a toaster's voice.
    "ERROR: Toasting failed. The bread has left the chat.",
    # Clever (HTTP 418), but the joke needs the reader to know the
    # teapot status code — it explains itself to engineers only.
    "ERROR 418: I'm a teapot, not a toaster. Please direct bread elsewhere.",
    # Deadpan and tight, but "this is not a metaphor" winks at the
    # reader instead of staying in the appliance's voice.
    "FATAL ERROR: Bread jammed. This is not a metaphor. Please call for help.",
    # Funny and fresh, but it is a remark about toast, not an error
    # message a toaster would display.
    "ERROR: Your toast is ready, but emotionally it never will be.",
    # The pick: a real error report (bread refused to brown), a small
    # appliance that has seen things, and a calm instruction to try
    # again tomorrow. Deadpan throughout, no pun, no borrowed meme,
    # and the surprise is the toaster sounding quietly traumatised.
    "ERROR: Bread refused to brown. It has seen things. Try again tomorrow.",
]

# 71 characters: every word earns its place, and the line is as short
# as it can be rather than as long as it may be.
SELECTED = 5


def main() -> None:
    entry = CANDIDATES[SELECTED]
    assert 1 <= len(entry) <= 120, f"entry is {len(entry)} characters"
    assert entry.strip() == entry
    assert "\n" not in entry, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Read-back verification: the file on disk must be exactly the
    # selected line, byte for byte, or the run fails loudly.
    with open(out_path, "rb") as f:
        written_bytes = f.read()
    if hashlib.sha256(written_bytes).digest() != hashlib.sha256(
        entry.encode("utf-8")
    ).digest():
        raise SystemExit("read-back mismatch: entry.txt != selected line")


if __name__ == "__main__":
    main()
