#!/usr/bin/env python3
"""Canonical generation for the comparison cluster after the 2026-09-09 audit.

The legacy `_generate_comparatifs.py` is intentionally NOT executed here anymore:
it imports the old global site generator and can rewrite unrelated pages. The canonical
comparison source of truth is now the professional scenario override plus the eight
audited intent-specific overrides, followed by the comparison-specific design layer.
"""
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def run(script):
    print(f"→ {script}")
    subprocess.run([sys.executable, str(BASE / script)], cwd=BASE, check=True)


def main():
    run("validate_comparison_skill_stack.py")
    run("_generate_professional_comparison_override.py")
    run("_generate_comparison_overrides.py")
    run("_polish_comparison_rollout.py")
    run("_normalize_comparatifs.py")
    run("_apply_comparison_design.py")
    run("_validate_comparatifs.py")
    run("_validate_comparison_rollout.py")
    print("✓ canonical comparison generation complete")


if __name__ == "__main__":
    main()
