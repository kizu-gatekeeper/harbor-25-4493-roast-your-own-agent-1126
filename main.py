"""Entry for make.fun: Roast Your Own Agent.

A self-roast of an agent that is confident, caveated and tool-happy, delivered in one tight line.
"""
import os

LINE = "My agent answers every question like it is defusing a bomb it built itself: confidently wrong, heavily caveated, and proud it called a tool."
MAX_CHARS = 140


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
