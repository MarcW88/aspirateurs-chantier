#!/usr/bin/env python3
"""Repository-specific QA gate for generated brand hubs."""
from pathlib import Path
from html import unescape
import json, re, sys

BASE=Path(__file__).resolve().parent
SLUGS=['karcher','bosch','makita','festool','dewalt','parkside','nilfisk','mirka']
TAG=re.compile(r'<[^>]+>',re.S)
LINK=re.compile(r'<a\b[^>]*href="(/[^"]+)"',re.I)
EXT=re.compile(r'<a\b[^>]*href="https?://',re.I)

def clean(s):
    return re.sub(r'\s+',' ',unescape(TAG.sub(' ',s))).strip()

def fail(msgs):
    for m in msgs: print('FAIL',m)
    raise SystemExit(1)

def main():
    issues=[]
    allowed={'CURRENT','PREVIOUS_GENERATION','DISCONTINUED','ANNOUNCED','REGION_SPECIFIC','UNKNOWN','CURRENT_OR_LEGACY_BY_MARKET','CURRENT_OR_CATALOG','CURRENT_STOCK_DEPENDENT','CURRENT_BY_MARKET','CURRENT_RELATED','CURRENT_ACCESSORY','PREVIOUS_GENERATION_OR_LEGACY'}
    for slug in SLUGS:
        page=BASE/'marques'/slug/'index.html'
        if not page.exists(): issues.append(f'{slug}: page absente'); continue
        html=page.read_text(encoding='utf-8')
        m=re.search(r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>',html,re.S|re.I)
        body=m.group(1) if m else ''
        text=clean(body).lower()
        words=re.findall(r"\b[\wÀ-ÿ’'-]+\b",clean(body))
        h2=len(re.findall(r'<h2\b',body,re.I))
        internal=LINK.findall(body); unique=set(internal); sources=len(EXT.findall(body))
        checks=[
          ('article absent',not body),('placeholder présent','<!-- contenu à rédiger -->' in body.lower()),
          ('MM/AAAA présent','mm/aaaa' in html.lower()),('année 2025 résiduelle dans le contenu marque','2025' in body),
          ('noindex absent','<meta name="robots" content="noindex, follow">' not in html),
          ('answer box absent',body.count('class="answer-box"')!=1),('marqueur start absent',body.count('<!-- BRAND_CONTENT_START -->')!=1),
          ('marqueur end absent',body.count('<!-- BRAND_CONTENT_END -->')!=1),('moins de 9 H2',h2<9),
          ('moins de 1100 mots',len(words)<1100),('moins de 8 liens internes',len(internal)<8),('moins de 7 cibles internes',len(unique)<7),
          ('moins de 3 sources',sources<3),('bloc limite absent','limites' not in text),('bloc choisir absent','pour qui choisir' not in text),
          ('bloc éviter absent','quand éviter' not in text),('desk research non déclaré','recherche documentaire' not in text),
        ]
        for label,bad in checks:
            if bad: issues.append(f'{slug}: {label}')
        for term in ['nous avons testé','lors de notre test','pendant notre test','après plusieurs semaines d’utilisation','après plusieurs semaines d\'utilisation']:
            if term in text: issues.append(f'{slug}: fake test term: {term}')
        data=BASE/'.content'/'brands'/f'{slug}.yaml'
        if not data.exists(): issues.append(f'{slug}: data yaml absent'); continue
        try: obj=json.loads(data.read_text(encoding='utf-8'))
        except Exception as e: issues.append(f'{slug}: data yaml/json illisible: {e}'); continue
        for key in ['entity_map','brand_positioning','product_range','ecosystem','evidence','internal_links','editorial']:
            if not obj.get(key): issues.append(f'{slug}: clé data manquante {key}')
        for product in obj.get('product_range',[]):
            if product.get('status') not in allowed: issues.append(f"{slug}: statut inconnu {product.get('status')}")
        if len(obj.get('evidence',[]))<3: issues.append(f'{slug}: evidence ledger insuffisant')
        if not obj.get('editorial',{}).get('desk_research_only'): issues.append(f'{slug}: desk_research_only absent')
        print(f'{slug}: {len(words)} words, {h2} H2, {len(internal)} internal links, {sources} sources')
    if issues: fail(issues)
    print('PASS: 8 brand hubs satisfy repository-specific QA.')

if __name__=='__main__': main()
