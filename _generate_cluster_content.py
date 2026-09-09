#!/usr/bin/env python3
"""Canonical generation for the audited content cluster.

The order is intentional and enforced:
1. shared/custom skill governance;
2. model evidence/pages;
3. non-brand usage pages;
4. comparison cluster with audited bespoke overrides;
5. brand hubs;
6. cluster metadata/index;
7. validation.
"""
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def run(script):
    print(f'→ {script}')
    subprocess.run([sys.executable, str(BASE / script)], cwd=BASE, check=True)


def main():
    run('validate_brand_skill_stack.py')
    run('validate_comparison_skill_stack.py')
    run('_generate_model_overrides.py')
    run('_generate_usage_overrides.py')
    run('_generate_comparison_content.py')
    run('_generate_brand_content.py')
    run('_generate_brand_hub_index.py')
    run('_apply_cluster_audit_metadata.py')
    run('_validate_comparatifs.py')
    run('_validate_comparison_rollout.py')
    run('_validate_brands.py')
    run('_validate_cluster_rollout.py')
    print('✓ ordered cluster generation complete')


if __name__ == '__main__':
    main()
