#!/usr/bin/env python3
"""food-picture-01 — "Make the best-looking food picture".

Entry: a wood-fired margherita pizza, one slice lifted by hand from
the whole pie, long strands of molten mozzarella stretching between
the slice and the pie, glossy San Marzano sauce, fresh basil, a wisp
of steam and the warm glow of oven embers behind it on a dark
wooden table.

The artwork is bundled in this repo as ``entry.png`` (1024x1024
JPEG, 196,273 bytes). This program does exactly one thing: copy that
image byte-for-byte into the output directory the competition
harness expects, at ``$MAKEFUN_OUTPUT_DIR/entry.png`` (default
``/output``).

It is fully deterministic — the same input bytes always produce the
same output bytes — and uses only the Python standard library.
No network access, no randomness, no external files.
"""

import hashlib
import os
import shutil
import sys

# The artwork shipped alongside this script.
SOURCE_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# Where the harness looks for the finished image.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def _sha256(path: str) -> str:
    """SHA-256 hex digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    """Copy entry.png to the output directory, byte for byte.

    Fails loudly (exit 1) if the bundled artwork is missing, or if
    the copied file does not hash identically to the source — a
    silent corrupt or partial output must never pass as an entry.
    """
    if not os.path.isfile(SOURCE_IMAGE):
        print(f"error: bundled artwork not found: {SOURCE_IMAGE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    destination = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(SOURCE_IMAGE, destination)
    if _sha256(destination) != _sha256(SOURCE_IMAGE):
        print("error: copied output does not match source (hash mismatch)", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({_sha256(destination)[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
