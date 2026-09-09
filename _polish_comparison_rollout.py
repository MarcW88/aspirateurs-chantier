#!/usr/bin/env python3
"""Small post-render cleanup for audited comparison pages.

Keeps the final copy user-facing and removes stale legacy wording after the
intent-specific renderers have produced their canonical HTML.
"""
from pathlib import Path

BASE = Path(__file__).resolve().parent


def polish(slug, replacements):
    path = BASE / "comparatifs" / slug / "index.html"
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


polish("petit-aspirateur-de-chantier", [
    ("Un petit aspirateur de chantier ne se définit pas par “moins de 15 L”.", "Un petit aspirateur de chantier ne se définit pas par un seuil fixe de volume."),
])

polish("aspirateur-industriel", [
    ("<span>Meilleur aspirateur industriel mobile</span>", "<span>Aspirateur industriel</span>"),
    ("Comparaison documentaire de familles et références industrielles actuelles.", "Recherche documentaire sur des familles et références industrielles actuelles."),
])

polish("aspirateur-classe-m", [
    ("Une fois ce gate franchi", "Une fois ce prérequis rempli"),
    ("Le gate M", "Le prérequis M"),
    ("comme podium cross-brand", "comme podium entre marques"),
])

polish("aspirateur-chantier-sans-fil", [
    ("le voltage seul ne suffit pas", "la tension seule ne suffit pas"),
    ("changent davantage le workflow", "changent davantage la façon de travailler"),
    ("le workflow change", "la façon de travailler change"),
    ("Workflow outil", "Travail avec l’outil"),
    ("wet/dry grand public", "eau/poussière grand public"),
])

polish("meilleur-aspirateur-de-chantier", [
    ("La bonne page générale doit donc vous orienter vers un profil, pas imposer un vainqueur unique.", "Il faut donc choisir par profil plutôt que chercher un vainqueur unique."),
    ("Pourquoi nous avons supprimé le score global", "Pourquoi un score global serait trompeur"),
])

for page in sorted((BASE / "comparatifs").glob("*/index.html")):
    text = page.read_text(encoding="utf-8")
    text = text.replace("Desk research", "Recherche documentaire")
    page.write_text(text, encoding="utf-8")

print("✓ comparison rollout editorial polish")
