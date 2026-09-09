#!/usr/bin/env python3
"""Remove unsupported Tier 1 / Tier 2 labels from the shared brand navigation.

Default mode applies the migration to the navigation source and every committed
HTML page. Use --check in CI to fail if an old tier label is reintroduced.
"""
from pathlib import Path
import argparse
import re

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "_generate.py"
FORBIDDEN = ("Tier 1", "Tier 2")


def targets():
    yield SOURCE
    for path in BASE.rglob("*.html"):
        if ".git" not in path.parts:
            yield path


def migrate(text: str) -> str:
    # Different generators historically produced slightly different indentation,
    # so the migration is intentionally whitespace-agnostic.
    text = re.sub(
        r'[ \t]*<span class="dd-label">Tier 1</span>[ \t]*(?:\r?\n)?',
        '',
        text,
    )
    text = re.sub(
        r'[ \t]*<div class="dd-sep"></div>[ \t]*(?:\r?\n)?[ \t]*'
        r'<span class="dd-label">Tier 2</span>[ \t]*(?:\r?\n)?',
        '',
        text,
    )
    text = re.sub(
        r'[ \t]*<span class="dd-label">Tier 2</span>[ \t]*(?:\r?\n)?',
        '',
        text,
    )
    return text


def violations():
    bad = []
    for path in targets():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        hits = [term for term in FORBIDDEN if term in text]
        if hits:
            bad.append((path.relative_to(BASE), hits))
    return bad


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not args.check:
        changed = 0
        for path in targets():
            if not path.exists():
                continue
            before = path.read_text(encoding="utf-8")
            after = migrate(before)
            if after != before:
                path.write_text(after, encoding="utf-8")
                changed += 1
        print(f"Updated {changed} files")

    bad = violations()
    if bad:
        print("GLOBAL_NAV: FAIL")
        for path, hits in bad:
            print(f" - {path}: {', '.join(hits)}")
        raise SystemExit(1)

    print("GLOBAL_NAV: PASS — no Tier 1 / Tier 2 labels remain")


if __name__ == "__main__":
    main()
