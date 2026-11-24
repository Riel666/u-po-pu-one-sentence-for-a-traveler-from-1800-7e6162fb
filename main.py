"""One sentence explaining the modern internet to someone arriving from 1800.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Picture a library, a post office, and a town square sharing one road, where any letter arrives in a blink and everyone can read it at once."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
