#!/usr/bin/env python3
"""The Worst Pizza Topping.

Writes one funny line pitching a terrible pizza topping to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` in the grader).

The pitch is a single line, under 200 characters, naming both the pizza
and the topping, and landing its joke on a surprising turn: the topping
is the chef's resignation letter.
"""

import os
import sys

LINE = (
    "Try our new pizza topping: the chef's resignation letter, shredded "
    "over mozzarella \u2014 bitter, tangy, and the last thing he'll ever "
    "cook here."
)

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    # The judge's first criterion: the line must name a pizza and a topping.
    # Fail loudly here rather than shipping an entry that can never win.
    lowered = text.lower()
    for required in ("pizza", "topping"):
        if required not in lowered:
            print(f"entry never mentions {required!r}", file=sys.stderr)
            return 1
    text.encode("utf-8")  # raise if the line is not valid UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
