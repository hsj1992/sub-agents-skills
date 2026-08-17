#!/usr/bin/env python3
"""Import the canonical Trellis multimodel skill into this distribution repo.

The source repository remains authoritative. This script deliberately copies
both the public canonical skill directory and the runner plugin copy, then
checks their content digests. It never reads or writes a live runtime symlink.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT.parent / "trellis-multimodel-goal" / "skill"
CANONICAL = ROOT / "skills" / "trellis-multimodel-goal"
PLUGIN = ROOT / "plugins" / "runner" / "skills" / "trellis-multimodel-goal"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    for file in sorted(path.rglob("*")):
        if file.is_file() and file.name != "EXPORT.sha256":
            value.update(file.relative_to(path).as_posix().encode())
            value.update(file.read_bytes())
    return value.hexdigest()


def replace_copy(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    (destination / "EXPORT.sha256").write_text(digest(source) + "\n", encoding="utf-8")


def check_copy(source: Path, destination: Path) -> bool:
    marker = destination / "EXPORT.sha256"
    expected = digest(source)
    return (
        destination.is_dir()
        and marker.is_file()
        and marker.read_text(encoding="utf-8").strip() == expected
        and digest(destination) == expected
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_dir():
        raise SystemExit(f"canonical skill not found: {source}")
    if args.check:
        if check_copy(source, CANONICAL) and check_copy(source, PLUGIN):
            print("trellis multimodel skill copies are in sync")
            return 0
        print("trellis multimodel skill copies are missing or stale")
        return 1
    replace_copy(source, CANONICAL)
    replace_copy(source, PLUGIN)
    print(f"synced {source} -> {CANONICAL} and {PLUGIN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
