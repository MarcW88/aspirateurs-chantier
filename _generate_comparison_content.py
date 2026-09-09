#!/usr/bin/env python3
"""Canonical generation for the comparison cluster after the 2026-09-09 audit.

Order matters:
1. legacy generator provides the shared HTML shell and keeps backwards compatibility;
2. the professional pilot override restores its scenario-led source of truth;
3. the audited 8-page override replaces legacy scoring output with intent-specific bodies;
4. whitespace and machine-integrity QA run on the final canonical artifacts.
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
    run("_normalize_comparatifs.py")
    run("_generate_comparatifs.py")
    run("_generate_professional_comparison_override.py")
    run("_generate_comparison_overrides.py")
    run("_normalize_comparatifs.py")
    run("_validate_comparatifs.py")
    run("_validate_comparison_rollout.py")
    print("✓ canonical comparison generation complete")


if __name__ == "__main__":
    main()
