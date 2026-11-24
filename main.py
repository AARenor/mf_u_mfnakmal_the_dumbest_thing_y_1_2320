"""Write one short text for make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec."""

import os
import sys
from pathlib import Path

TEXT = "My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
