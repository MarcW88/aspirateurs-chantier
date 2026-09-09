#!/usr/bin/env python3
"""Validate the shared/custom comparison skill stack and its 80/20 governance target."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / '.agents' / 'skills' / 'comparison-skill-stack.json'
CONFIG = ROOT / 'comparison-workflow.config.yaml'

REQUIRED_SHARED = {
    'seo-content-audit', 'seo-keyword', 'jobs-to-be-done',
    'evidence-based-reviews', 'fact-check', 'affiliate-value',
    'content-brief-authoring', 'content-and-copy', 'humanizer',
    'general-writing', 'anti-ai-slop', 'seo-onpage', 'seo-technical',
    'internal-linking-audit', 'editorial-qa'
}
CUSTOM_WORKFLOWS = {'comparison-content-workflow', 'comparison-analysis-workflow'}


def main():
    errors = []

    if not MANIFEST.exists():
        errors.append(f'missing manifest: {MANIFEST.relative_to(ROOT)}')
        data = {}
    else:
        try:
            data = json.loads(MANIFEST.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'invalid manifest JSON: {exc}')
            data = {}

    shared = data.get('shared', [])
    custom = data.get('custom', [])
    total = len(shared) + len(custom)
    ratio = len(shared) / total if total else 0.0
    target = float(data.get('target_shared_ratio_min', 0.80))

    for item in shared + custom:
        name = item.get('name')
        if not name:
            errors.append('manifest entry without name')
            continue
        skill = ROOT / '.agents' / 'skills' / name / 'SKILL.md'
        if not skill.exists():
            errors.append(f'missing skill: {name}')

    shared_names = {item.get('name') for item in shared}
    custom_names = {item.get('name') for item in custom}

    missing_shared = sorted(REQUIRED_SHARED - shared_names)
    if missing_shared:
        errors.append('missing required shared skills in manifest: ' + ', '.join(missing_shared))

    missing_custom = sorted(CUSTOM_WORKFLOWS - custom_names)
    if missing_custom:
        errors.append('missing custom comparison workflows in manifest: ' + ', '.join(missing_custom))

    unexpected_custom = sorted(custom_names - CUSTOM_WORKFLOWS)
    if unexpected_custom:
        errors.append('unexpected custom comparison components: ' + ', '.join(unexpected_custom))

    if ratio < target:
        errors.append(f'shared ratio {ratio:.1%} is below target {target:.1%}')

    # Custom workflows must orchestrate, not fall back to vague optional skills.
    for workflow in CUSTOM_WORKFLOWS:
        path = ROOT / '.agents' / 'skills' / workflow / 'SKILL.md'
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8').lower()
        if 'when available' in text or 'lorsque les skills spécialisés' in text:
            errors.append(f'{workflow}: optional-skill fallback still present')
        if '80/20' not in text:
            errors.append(f'{workflow}: 80/20 governance not documented')
        if 'aspirateurs-chantier.fr' not in text:
            errors.append(f'{workflow}: target domain adaptation not explicit')

    # The root config must not silently restore the old mandatory-scoring method.
    if not CONFIG.exists():
        errors.append('missing comparison-workflow.config.yaml')
    else:
        config = CONFIG.read_text(encoding='utf-8').lower()
        required_config_tokens = [
            'scoring_optional: true',
            'weighting_optional: true',
            'hard_gates_optional: true',
            'prohibit_word_count_quotas: true',
            'prohibit_heading_count_quotas: true',
            'prohibit_internal_link_quotas: true',
            'prohibit_comparison_type_templates: true',
            'prohibit_inferring_dust_class_from_hepa_power_or_airflow: true',
        ]
        for token in required_config_tokens:
            if token not in config:
                errors.append(f'config missing governance rule: {token}')

        forbidden_config_tokens = [
            'require_weights_sum_100: true',
            'require_hard_gates: true',
            'enable_confidence_adjustment: true',
        ]
        for token in forbidden_config_tokens:
            if token in config:
                errors.append(f'legacy mandatory-scoring rule still present: {token}')

    if errors:
        for error in errors:
            print('FAIL', error)
        return 1

    print(
        f'PASS: {len(shared)} shared + {len(custom)} custom comparison components; '
        f'shared ratio={ratio:.1%} (target >= {target:.0%}).'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
