#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader entry (make.fun).

Writes exactly one fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python stdlib only, no dependencies.

The fortune: the market took the trader's coins as tuition, and the
diploma in patience arrives with the next green candle -- oracular
voice, rueful and warm, with the punch landing on the last words.
"""

import os

FORTUNE = "The market kept your coins as tuition \u2014 your diploma in patience arrives with the next green candle."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Gate: exactly one line, 1-160 chars, at most 20 words, no newline.
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert "\r" not in FORTUNE, "fortune must be a single line"
    assert 1 <= len(FORTUNE) <= 160, f"fortune length {len(FORTUNE)} out of gate range"
    assert len(FORTUNE.split()) <= 20, f"fortune has {len(FORTUNE.split())} words, over 20"
    assert FORTUNE.strip() == FORTUNE, "fortune must not have leading/trailing whitespace"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read-back check: the file on disk must be byte-identical to FORTUNE.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == FORTUNE, "written entry does not match FORTUNE"
    print(f"Wrote {len(FORTUNE)} chars, {len(FORTUNE.split())} words to {path}")


if __name__ == "__main__":
    main()
