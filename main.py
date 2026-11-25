"""One Emoji, One Smile — a single warm hug, printed and saved."""

import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    emoji = (here / "emoji.txt").read_text(encoding="utf-8").strip()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", str(here / "output")))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "output.txt").write_text(emoji + "\n", encoding="utf-8")
    # A hug needs no words.
    print(emoji)


if __name__ == "__main__":
    main()
