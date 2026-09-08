#!/usr/bin/env python3
"""Structural QA for generated comparison pages."""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
SLUGS = [
    "meilleur-aspirateur-de-chantier",
    "aspirateur-eau-poussiere",
    "aspirateur-chantier-sans-fil",
    "aspirateur-chantier-sans-sac",
    "aspirateur-chantier-puissant",
    "aspirateur-professionnel",
    "aspirateur-industriel",
    "aspirateur-classe-m",
    "petit-aspirateur-de-chantier",
]

def words(html):
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.findall(r"\b[\wÀ-ÿ'-]+\b", text)

errors = []
for slug in SLUGS:
    page = BASE / "comparatifs" / slug / "index.html"
    data = BASE / ".content" / "comparisons" / f"{slug}.json"
    if not page.exists():
        errors.append(f"{slug}: missing HTML")
        continue
    if not data.exists():
        errors.append(f"{slug}: missing comparison JSON")
        continue

    html = page.read_text(encoding="utf-8")
    obj = json.loads(data.read_text(encoding="utf-8"))

    checks = {
        "minimum 1100 words": len(words(html)) >= 1100,
        "minimum 6 H2": len(re.findall(r"<h2\b", html, flags=re.I)) >= 6,
        "one answer box": len(re.findall(r'class="answer-box"', html)) == 1,
        "minimum 5 internal links": len(re.findall(r'href="/', html)) >= 5,
        "minimum 3 external sources": len(re.findall(r'href="https://', html)) >= 3,
        "noindex preserved": 'name="robots" content="noindex, follow"' in html,
        "2026 freshness": "2026" in html and "Comparatif 2025" not in html,
        "no placeholders": "<!-- Contenu à rédiger -->" not in html and "MM/AAAA" not in html,
        "desk research disclosure": "sans prétention de test physique" in html or "sans prétendre à un test physique" in html,
        "affiliate independence": "commission" in html.lower() and obj.get("notes", {}).get("affiliate_commission_used_in_ranking") is False,
        "ranking present": len(obj.get("ranking", [])) >= 3,
        "weights sum 100": sum(c["weight"] for c in obj.get("criteria", [])) == 100,
        "hard gate present": any(c.get("hard_gate") for c in obj.get("criteria", [])),
    }
    for label, ok in checks.items():
        if not ok:
            errors.append(f"{slug}: FAIL {label}")
    print(f"{slug}: {len(words(html))} words, {len(re.findall(r'<h2\b', html, flags=re.I))} H2 — {'PASS' if all(checks.values()) else 'FAIL'}")

if errors:
    print("\n".join(errors))
    raise SystemExit(1)

print(f"PASS: {len(SLUGS)} comparison pages satisfy structural QA.")
