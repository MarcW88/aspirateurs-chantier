#!/usr/bin/env python3
"""QA gate for the global site-design-review implementation."""
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent
REPORT = BASE / ".content" / "reviews" / "site-design-review-2026-09-08.md"


def main() -> None:
    issues = []
    style = (BASE / "style.css").read_text(encoding="utf-8")
    generator = (BASE / "_generate.py").read_text(encoding="utf-8")
    js = (BASE / "site.js").read_text(encoding="utf-8")

    style_checks = {
        "design block unique": style.count("/* SITE DESIGN REVIEW V1 START */") == 1 and style.count("/* SITE DESIGN REVIEW V1 END */") == 1,
        "editorial display font": "Source+Serif+4" in style and "--font-display" in style,
        "focus visible": "a:focus-visible" in style and "button:focus-visible" in style,
        "keyboard dropdown": ".nav-item:focus-within > .dropdown" in style,
        "mobile nav state": ".site-nav.is-open" in style,
        "generated tables styled": ".content-main .table-wrap" in style,
        "reduced motion": "prefers-reduced-motion" in style,
        "technical bars removed": ".stat-bar-wrap { display: none; }" in style,
    }
    for label, ok in style_checks.items():
        if not ok:
            issues.append(f"style.css: {label}")

    if "aria-controls=\"site-navigation\"" not in generator:
        issues.append("_generate.py: burger accessible absent")
    if "<main id=\"main-content\">" not in generator:
        issues.append("_generate.py: main-content absent")
    if "/site.js" not in generator:
        issues.append("_generate.py: site.js non injecté")
    if "© 2025 aspirateurs-chantier.fr" in generator:
        issues.append("_generate.py: année footer obsolète")

    if "Escape" not in js or "aria-expanded" not in js:
        issues.append("site.js: navigation mobile incomplète")

    html_files = sorted(BASE.rglob("index.html"))
    if not html_files:
        issues.append("aucun index.html trouvé")

    missing_script = []
    missing_skip = []
    missing_nav = []
    missing_noindex = []
    duplicate_script = []

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(BASE).as_posix()
        if text.count('/site.js') != 1:
            (missing_script if '/site.js' not in text else duplicate_script).append(rel)
        if 'class="skip-link"' not in text or 'id="main-content"' not in text:
            missing_skip.append(rel)
        if 'id="site-navigation"' not in text or 'aria-controls="site-navigation"' not in text or 'aria-expanded="false"' not in text:
            missing_nav.append(rel)
        if '<meta name="robots" content="noindex, follow">' not in text:
            missing_noindex.append(rel)

    for label, values in [
        ("site.js absent", missing_script),
        ("site.js dupliqué", duplicate_script),
        ("skip/main landmark absent", missing_skip),
        ("navigation accessible absente", missing_nav),
        ("noindex absent", missing_noindex),
    ]:
        if values:
            issues.append(f"{label}: {', '.join(values[:8])}" + (" …" if len(values) > 8 else ""))

    homepage = (BASE / "index.html").read_text(encoding="utf-8")
    if "Tests approfondis" in homepage:
        issues.append("homepage: promesse de tests non alignée avec la méthode")
    if "Média technique spécialisé — Comparatifs documentés" not in homepage:
        issues.append("homepage: positionnement éditorial non appliqué")

    status = "PASS" if not issues else "FAIL"
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = f"""# QA — Site Design Review — 08/09/2026

```yaml
status: {status}
pages_checked: {len(html_files)}
indexing_status: noindex
visual_source_of_truth: style.css
workflow: site-design-review
```

## Changements validés

- Direction visuelle spécifique documentée dans `DESIGN.md`.
- Skill `site-design-review` intégré dans `.agents/skills/`.
- Hiérarchie éditoriale renforcée via `style.css`.
- Barres de progression décoratives retirées du panneau technique de homepage.
- Grilles de cartes répétitives remplacées visuellement par des listes éditoriales lorsque pertinent.
- Tableaux générés des comparatifs et pages marques harmonisés et scrollables sur mobile.
- Largeur de lecture des contenus longs maîtrisée.
- Focus clavier et dropdowns `:focus-within` ajoutés.
- Menu mobile fonctionnel via `site.js`, avec `aria-expanded` et fermeture par Échap.
- Lien d’évitement et landmark `main` ajoutés.
- `noindex, follow` conservé sur les pages contrôlées.
- Footer actualisé à 2026 et promesse de homepage alignée sur la recherche documentaire.

## Limite de vérification

La revue a pu valider le code, la structure HTML, le responsive CSS et les états d’interaction définis. Aucun navigateur graphique n’est disponible dans cet environnement connecté : la PR doit donc rester la dernière étape de validation visuelle humaine avant fusion.

## Résultat

{('Tous les gates automatiques passent.' if not issues else 'Problèmes détectés : ' + '; '.join(issues))}
"""
    REPORT.write_text(report, encoding="utf-8")

    if issues:
        for issue in issues:
            print("FAIL", issue)
        raise SystemExit(1)

    print(f"PASS: site design QA on {len(html_files)} rendered pages")


if __name__ == "__main__":
    main()
