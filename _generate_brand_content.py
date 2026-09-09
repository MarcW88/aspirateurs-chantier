#!/usr/bin/env python3
"""Canonical brand-content generation entry point.

Run the generic generator first, then site-approved bespoke overrides and the
small editorial polish pass. If the cluster audit metadata layer exists, reapply
it last so a standalone brand rebuild cannot erase recovery decisions.
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
    run('_generate_brand_overrides.py')
    run('_brand_rollout_polish.py')
    cluster_metadata = BASE / '_apply_cluster_audit_metadata.py'
    if cluster_metadata.exists():
        run(cluster_metadata.name)
    print('✓ canonical brand generation complete')


if __name__ == '__main__':
    main()
