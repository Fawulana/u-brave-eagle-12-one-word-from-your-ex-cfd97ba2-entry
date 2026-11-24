# SPDX-License-Identifier: MIT
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. Deterministic, offline, stdlib only.

The word: "roommate".

Why this word: every ex has a generic adjective ready — selfish,
clingy, boring — but "roommate" is the verdict no adjective can
match. It says the romance died so quietly that a lover got
demoted to a chore-splitting housemate, and the entrant knows it.
One image, no explanation needed, instantly relatable, and it
stings precisely because it is not an insult — it is a job title.
"""

import os
from pathlib import Path

WORD = "roommate"


def main() -> None:
    # Gate check, done by the program itself: 1-24 chars, not blank.
    assert 1 <= len(WORD) <= 24 and WORD.strip(), "word fails the gate"
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # Exactly the word, no trailing newline: 8 bytes, 8 characters.
    target.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
