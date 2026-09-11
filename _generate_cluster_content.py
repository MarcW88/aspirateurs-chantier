#!/usr/bin/env python3
"""Canonical generation for the audited content cluster.

The order is intentional and enforced:
1. shared/custom skill governance for Brands, Comparisons, Usages and Guides;
2. canonical Guide generation from baseline + authored v2 fragments;
3. model evidence/pages;
4. non-brand usage shell + authored v2 materialization;
5. comparison cluster with audited bespoke overrides;
6. brand hubs;
7. cluster metadata/index;
8. validation.
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
    run('validate_usage_workflow.py')
    run('validate_guide_workflow.py')
    run('_generate_guide_content.py')
    run('_generate_model_overrides.py')
    run('_generate_usage_overrides.py')
    run('_materialize_usage_v2.py')
    run('validate_usage_workflow.py')
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
