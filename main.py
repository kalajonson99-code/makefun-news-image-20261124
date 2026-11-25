#!/usr/bin/env python3
"""Sum up 24 November 2026 world news in one image.

The entry image is bundled in this repository as entry.png
(1024x1024, under 1 MiB). This program writes that exact image
to /output/entry.png, deterministically, with no network access.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    if not os.path.exists(SRC):
        print(f"missing bundled image: {SRC}", file=sys.stderr)
        return 1
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
