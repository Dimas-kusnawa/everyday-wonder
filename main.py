#!/usr/bin/env python3
"""Write one line of everyday wonder to /output/entry.txt.

The wonder here is a sound you never hear: the fridge hums all night,
and the moment only becomes strange when the hum stops and the silence
lands. A familiar kitchen, made foreign by its own quiet.
"""

import os

# One sentence, 135 characters, inside the 200-character cap.
# No trailing newline: the file is exactly the line, nothing else.
LINE = "Every night the fridge hums the same low note, and I only notice it when it stops, as if the whole kitchen had been holding its breath."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
