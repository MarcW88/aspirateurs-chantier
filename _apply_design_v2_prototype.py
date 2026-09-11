#!/usr/bin/env python3
from pathlib import Path

BASE = Path(__file__).resolve().parent

PAGES = {
    'index.html': 'design-v2 design-home',
    'guides/comment-choisir-aspirateur-de-chantier/index.html': 'design-v2 design-guide',
    'modeles/bosch-gas-35-l-afc/index.html': 'design-v2 design-model',
    'comparatifs/meilleur-aspirateur-de-chantier/index.html': 'comparison-page design-v2 design-comparison',
}

for rel, body_class in PAGES.items():
    path = BASE / rel
    html = path.read_text(encoding='utf-8')

    # Body class for scoped prototype CSS.
    if '<body class=' in html:
        import re
        html = re.sub(r'<body class="[^"]*">', f'<body class="{body_class}">', html, count=1)
    else:
        html = html.replace('<body>', f'<body class="{body_class}">', 1)

    # V2 stylesheet must load after page-specific CSS so it can intentionally override it.
    if '/design-v2.css' not in html:
        if '/comparison-pages.css' in html:
            html = html.replace('  <link rel="stylesheet" href="/comparison-pages.css">',
                                '  <link rel="stylesheet" href="/comparison-pages.css">\n  <link rel="stylesheet" href="/design-v2.css">', 1)
        else:
            html = html.replace('  <link rel="stylesheet" href="/style.css">',
                                '  <link rel="stylesheet" href="/style.css">\n  <link rel="stylesheet" href="/design-v2.css">', 1)

    if '/design-v2.js' not in html:
        html = html.replace('</body>', '  <script src="/design-v2.js" defer></script>\n</body>', 1)

    path.write_text(html, encoding='utf-8')
    print(f'✓ scoped {rel}')

# Small home changes that remove the strongest generic/AI signals without rewriting the page.
home_path = BASE / 'index.html'
home = home_path.read_text(encoding='utf-8')
home = home.replace('Base de données spécialisée — Tests &amp; comparatifs indépendants',
                    'Guide technique indépendant — données, usages et comparatifs')
home = home.replace('Aspirateurs de chantier :<br>comparatifs, tests et guide de choix.',
                    'Aspirateurs de chantier :<br>choisir sur les critères qui comptent.')
home = home.replace('Tests approfondis, fiches techniques normalisées et comparatifs indépendants. Pour choisir le bon aspirateur selon le chantier, pas selon la commission.',
                    'Classes de poussière, captage à l’outil, décolmatage, mobilité et capacité : des repères documentés pour choisir selon le chantier réel.')
home = home.replace('Les questions que posent les utilisateurs aux moteurs de recherche et aux assistants IA.',
                    'Classes, débit, dépression, filtration et connexion à l’outil : les notions à comprendre avant de comparer des modèles.')

# Correct two stale homepage class labels already contradicted by the audited model pages.
old_wd6 = '''<td class="col-model"><a href="/modeles/karcher-wd6/" style="color:var(--color-primary)">Kärcher WD6</a></td>\n            <td><span class="badge badge-l">L</span></td>'''
new_wd6 = '''<td class="col-model"><a href="/modeles/karcher-wd6/" style="color:var(--color-primary)">Kärcher WD6</a></td>\n            <td><span class="badge badge-gray">Non classé</span></td>'''
home = home.replace(old_wd6, new_wd6)
old_festool = '''<td class="col-model"><a href="/modeles/festool-ctl-midi/" style="color:var(--color-primary)">Festool CTL Midi</a></td>\n            <td><span class="badge badge-m">M</span></td>'''
new_festool = '''<td class="col-model"><a href="/modeles/festool-ctl-midi/" style="color:var(--color-primary)">Festool CTL Midi</a></td>\n            <td><span class="badge badge-l">L</span></td>'''
home = home.replace(old_festool, new_festool)
home_path.write_text(home, encoding='utf-8')
print('✓ simplified home copy and stale class labels')
