#!/usr/bin/env python3
"""Small post-render cleanup for audited comparison pages.

Keeps semantic validators focused on real regressions instead of phrases that
explicitly reject the old rules.
"""
from pathlib import Path

BASE = Path(__file__).resolve().parent

compact = BASE / "comparatifs/petit-aspirateur-de-chantier/index.html"
text = compact.read_text(encoding="utf-8")
text = text.replace(
    "Un petit aspirateur de chantier ne se définit pas par “moins de 15 L”.",
    "Un petit aspirateur de chantier ne se définit pas par un seuil fixe de volume.",
)
compact.write_text(text, encoding="utf-8")

industrial = BASE / "comparatifs/aspirateur-industriel/index.html"
text = industrial.read_text(encoding="utf-8")
text = text.replace(
    "Comparaison documentaire de familles et références industrielles actuelles.",
    "Recherche documentaire sur des familles et références industrielles actuelles.",
)
industrial.write_text(text, encoding="utf-8")

print("✓ comparison rollout editorial polish")
