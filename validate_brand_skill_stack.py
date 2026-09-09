#!/usr/bin/env python3
"""Validate the shared/custom brand skill stack and its 80/20 governance target."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / '.agents' / 'skills' / 'brand-skill-stack.json'


def main():
    errors = []
    if not MANIFEST.exists():
        errors.append(f'missing manifest: {MANIFEST.relative_to(ROOT)}')
        data = {}
    else:
        data = json.loads(MANIFEST.read_text(encoding='utf-8'))

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

    if ratio < target:
        errors.append(f'shared ratio {ratio:.1%} is below target {target:.1%}')

    required_direct = {
        'search-intent','content-audit','content-refresh','affiliate-value','fact-check',
        'evidence-based-reviews','internal-linking-audit','humanizer','general-writing',
        'anti-ai-slop','seo-technical','seo-best-practices','editorial-qa'
    }
    shared_names = {item.get('name') for item in shared}
    missing = sorted(required_direct - shared_names)
    if missing:
        errors.append('missing required shared skills in manifest: ' + ', '.join(missing))

    for workflow in ['brand-content-workflow', 'brand-analysis-workflow']:
        path = ROOT / '.agents' / 'skills' / workflow / 'SKILL.md'
        if path.exists():
            text = path.read_text(encoding='utf-8').lower()
            if 'lorsque les skills spécialisés' in text or 'when available' in text:
                errors.append(f'{workflow}: optional-skill fallback still present')

    if errors:
        for error in errors:
            print('FAIL', error)
        return 1

    print(f'PASS: {len(shared)} shared + {len(custom)} custom components; shared ratio={ratio:.1%} (target >= {target:.0%}).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
