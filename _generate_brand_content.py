#!/usr/bin/env python3
"""Canonical brand-content generation entry point.

Run the generic generator first, then site-approved bespoke overrides. This
prevents a later generic rebuild from silently restoring a templated Bosch hub.
"""
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def run(script):
    subprocess.run([sys.executable, str(BASE / script)], cwd=BASE, check=True)


def main():
    run('_generate_brands.py')
    run('_generate_bosch.py')
    print('✓ canonical brand generation complete')


if __name__ == '__main__':
    main()
