#!/usr/bin/env python3
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
VERDICTS = {
    'bosch': ('KEEP', 0.90),
    'karcher': ('DEEP_REWRITE', 0.95),
    'festool': ('DEEP_REWRITE', 0.95),
    'makita': ('DEEP_REWRITE', 0.90),
    'dewalt': ('LIGHT_UPDATE', 0.80),
    'parkside': ('LIGHT_UPDATE', 0.85),
    'nilfisk': ('DEEP_REWRITE', 0.90),
    'mirka': ('DEEP_REWRITE', 0.95),
}

for slug, (verdict, confidence) in VERDICTS.items():
    path = BASE / '.content' / 'brands' / f'{slug}.yaml'
    data = json.loads(path.read_text(encoding='utf-8'))
    data['cluster_audit'] = {
        'audited_snapshot': '7547c8ef4b1d6bb2602756312beecb1cdc1ad185',
        'date': '2026-09-09',
        'verdict': verdict,
        'confidence': confidence,
        'order_gate': 'MODEL_CLEANUP -> USAGE_COMPLETION -> BRAND_REVIEW -> CLUSTER_PUBLISH_REVIEW'
    }
    data['recovery_verdict'] = verdict
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'✓ cluster verdict {slug}: {verdict}')
