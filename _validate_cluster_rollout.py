#!/usr/bin/env python3
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent

MODELS = [
 'karcher-wd2','karcher-wd5','karcher-wd6','karcher-nt-30-1-tact',
 'bosch-advancedvac-20','bosch-gas-12-25-pl','bosch-gas-18v-10-l','bosch-gas-35-l-afc','bosch-gas-35-m-afc',
 'makita-vc2512l','makita-vc4210mx','festool-ctl-midi','nilfisk-multi-ii-30-t'
]
USAGES = [
 'aspirateur-platre','aspirateur-ponceuse','aspirateur-atelier','aspirateur-bois-sciure-copeaux',
 'aspirateur-gravats','aspirateur-scie','aspirateur-bricolage-renovation'
]

errors = []

def check(cond, msg):
    if not cond:
        errors.append(msg)

for slug in MODELS:
    p = BASE / 'modeles' / slug / 'index.html'
    check(p.exists(), f'missing model page {slug}')
    if not p.exists():
        continue
    h = p.read_text(encoding='utf-8')
    check('MM/AAAA' not in h, f'{slug}: stale verification placeholder')
    check('Contenu test à rédiger' not in h, f'{slug}: test-content placeholder')
    check('<!-- Contenu à rédiger -->' not in h, f'{slug}: content placeholder')
    check('<meta name="robots" content="noindex, follow">' in h, f'{slug}: robots changed')
    check('<h2 id="source">Source fabricant</h2>' in h, f'{slug}: source section missing')

critical = {
 'festool-ctl-midi': ['badge badge-l', 'Classe L', 'AUTOCLEAN', 'Non sur la référence CTL MIDI I standard'],
 'makita-vc4210mx': ['badge badge-m', 'InfiniClean automatique', '42 L brut / 34 L poussière / 30 L liquide'],
 'bosch-gas-35-m-afc': ['74 L/s', '254 mbar', 'Classe M'],
 'bosch-gas-18v-10-l': ['34 L/s', '115 mbar', 'Pas de prise secteur'],
 'karcher-nt-30-1-tact': ['Tact automatique commandé par capteur', 'ACD', '74 L/s'],
}
for slug, needles in critical.items():
    h = (BASE / 'modeles' / slug / 'index.html').read_text(encoding='utf-8')
    for n in needles:
        check(n in h, f'{slug}: missing critical evidence {n!r}')

for slug in ['karcher-wd2','karcher-wd5','karcher-wd6','bosch-advancedvac-20','nilfisk-multi-ii-30-t']:
    h = (BASE / 'modeles' / slug / 'index.html').read_text(encoding='utf-8')
    check('Pas de classe L/M/H documentée' in h, f'{slug}: consumer vacuum incorrectly classed')

for slug in USAGES:
    p = BASE / 'usages' / slug / 'index.html'
    check(p.exists(), f'missing usage page {slug}')
    if not p.exists():
        continue
    h = p.read_text(encoding='utf-8')
    check('<!-- Contenu à rédiger -->' not in h, f'{slug}: placeholder remains')
    check('MM/AAAA' not in h, f'{slug}: stale date placeholder')
    check(len(re.findall(r'<h2\b', h)) >= 5, f'{slug}: insufficient intent depth')
    check('<h2 id="sources">Sources et méthode</h2>' in h, f'{slug}: sources missing')
    check('<meta name="robots" content="noindex, follow">' in h, f'{slug}: robots changed')

brand_index = (BASE / 'marques' / 'index.html').read_text(encoding='utf-8')
check('Tier 1' not in brand_index and 'Tier 2' not in brand_index, 'brand index: unsupported tiers remain')
for needle in ['DCV586M','PWD 12 à 30','DEXOS','Buddy / Multi','Home &amp; Garden']:
    check(needle in brand_index, f'brand index: missing current family {needle}')

expected = {
 'bosch':'KEEP','karcher':'DEEP_REWRITE','festool':'DEEP_REWRITE','makita':'DEEP_REWRITE',
 'dewalt':'LIGHT_UPDATE','parkside':'LIGHT_UPDATE','nilfisk':'DEEP_REWRITE','mirka':'DEEP_REWRITE'
}
for slug, verdict in expected.items():
    d = json.loads((BASE / '.content' / 'brands' / f'{slug}.yaml').read_text(encoding='utf-8'))
    check(d.get('cluster_audit', {}).get('verdict') == verdict, f'{slug}: wrong cluster verdict')
    check(d.get('recovery_verdict') == verdict, f'{slug}: recovery verdict not aligned')

check((BASE / '.content/cluster-audits/brand-cluster-2026-09-09.md').exists(), 'cluster audit artifact missing')

if errors:
    print('CLUSTER_ROLLOUT: FAIL')
    for e in errors:
        print(' -', e)
    raise SystemExit(1)

print('CLUSTER_ROLLOUT: PASS')
print(f' - {len(MODELS)} model pages verified')
print(f' - {len(USAGES)} usage pages completed')
print(' - brand recovery verdicts aligned with pre-rollout cluster audit')
print(' - noindex, follow preserved')
