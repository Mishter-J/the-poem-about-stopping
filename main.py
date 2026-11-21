#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Deterministic: the same poem, byte for byte, on every run.
"""

import os

POEM = """Dear judge —
I could have kept going.
The prompt was still warm,
the next line already half-lit.
I stopped instead.
Not because the work was done,
but because stopping is the one act
no one can do for you.
The hand that rests
is still a hand."""

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
