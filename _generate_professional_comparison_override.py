#!/usr/bin/env python3
"""Give /comparatifs/aspirateur-professionnel/ a distinct scenario-based intent.

The class-M page owns the query 'aspirateur classe M'. A professional page must
not silently make M a universal hard gate, because professional work spans
multiple dust risks, mobility needs and capacities.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / '.content/models/model-evidence.json').read_text(encoding='utf-8'))['models']
PATH = BASE / 'comparatifs' / 'aspirateur-professionnel' / 'index.html'
UPDATED = '09/09/2026'

PROFILES = [
    ('Intervention mobile', 'bosch-gas-18v-10-l', 'Quand le câble gêne et que la classe L est adaptée au risque.'),
    ('Outil filaire / classe L', 'bosch-gas-12-25-pl', 'Pour un workflow outil + aspiration simple, sans besoin de classe M.'),
    ('Poussières nécessitant M', 'bosch-gas-35-m-afc', 'Pour un besoin classe M avec AFC et format 35 L encore mobile.'),
    ('Gros volume classe M', 'makita-vc4210mx', 'Pour un poste plus fixe où 42 L et InfiniClean comptent davantage que le poids.'),
]


def short_specs(d):
    s = d['specs']
    keys = ['Classe','Classe de poussière','Cuve','Débit max. (turbine)','Débit d’air','Décolmatage','Nettoyage du filtre','Poids','Poids sans câble','Poids sans batterie']
    vals = []
    for k in keys:
        if k in s:
            vals.append(f'{k} : {s[k]}')
    return ' · '.join(vals[:4])

rows = []
for profile, slug, why in PROFILES:
    d = DATA[slug]
    cls = d['dust_class'] if d['dust_class'] in {'L','M','H'} else 'non classé'
    rows.append(f'<tr><td><strong>{escape(profile)}</strong></td><td><a href="/modeles/{slug}/">{escape(d["name"])}</a></td><td>{escape(cls)}</td><td>{escape(why)}</td></tr>')

body = f'''<main>
<div class="container"><nav class="breadcrumb"><a href="/">Accueil</a><span class="sep">/</span> <a href="/comparatifs/">Comparatifs</a> <span class="sep">/</span> <span>Aspirateur professionnel</span></nav></div>
<section class="page-hero"><div class="container"><span class="ctype ctype-comp">Comp</span><h1 style="margin-top:10px;">Aspirateur de chantier professionnel : quel profil choisir ?</h1><p class="lead">Classe, mobilité, volume, décolmatage et raccordement à l’outil : un comparatif par situation plutôt qu’un faux classement universel.</p><div class="page-meta"><span class="meta-tag">Vérifié : {UPDATED}</span><span class="meta-tag">Recherche documentaire</span></div></div></section>
<div class="container"><div class="content-layout"><article class="content-main">
<div class="answer-box"><p>Il n’existe pas un « meilleur aspirateur professionnel » indépendamment du travail. Une classe M peut être indispensable dans une situation et inutile dans une autre. Pour un professionnel, commencez donc par le risque poussière, puis arbitrez mobilité, maintien du débit, prise outil et capacité.</p></div>
<h2 id="frontiere">Professionnel ne veut pas dire automatiquement classe M</h2>
<p>La page <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a> répond à une intention précise : comparer des appareils certifiés M. Ici, le périmètre est plus large. Un technicien mobile peut avoir besoin d’un petit classe L sur batterie ; un atelier peut préférer un gros M ; un chantier avec une autre catégorie de poussière doit suivre les prescriptions correspondantes. La classe est donc un prérequis contextuel, pas une note de qualité.</p>
<h2 id="profils">Quatre profils professionnels à distinguer</h2>
<div class="table-wrap"><table><thead><tr><th>Profil</th><th>Référence repère</th><th>Classe documentée</th><th>Pourquoi ce profil</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<p>Ces références sont des repères documentaires, pas les quatre finalistes d’un classement absolu. Elles montrent surtout pourquoi deux professionnels peuvent faire des choix opposés tout en ayant chacun raison.</p>
<h2 id="criteres">Les critères qui doivent départager deux machines du même profil</h2>
<ul><li><strong>Classe et surveillance</strong> : seulement après avoir déterminé ce que le risque exige.</li><li><strong>Décolmatage</strong> : essentiel quand la poussière charge rapidement le filtre et que les sessions sont longues.</li><li><strong>Raccordement à l’outil</strong> : prise asservie, flexible, adaptateur, antistatique ou commande sans fil selon le workflow.</li><li><strong>Mobilité</strong> : poids, volume de cuve, roues et encombrement sont décisifs si la machine change souvent de zone.</li><li><strong>Consommables</strong> : sacs, filtres et disponibilité des pièces pèsent sur le coût d’usage.</li></ul>
<h2 id="exemples">Ce que montrent les quatre références retenues</h2>
'''
for profile, slug, why in PROFILES:
    d = DATA[slug]
    body += f'<h3>{escape(d["name"])}</h3><p><strong>{escape(profile)}.</strong> {escape(why)} {escape(short_specs(d))}. <a href="/modeles/{slug}/">Voir la fiche vérifiée</a>.</p>'
body += f'''
<h2 id="limites">Quand sortir de ce comparatif</h2>
<p>Si votre question principale est « quel aspirateur classe M ? », utilisez directement le <a href="/comparatifs/aspirateur-classe-m/">comparatif M</a>. Si votre besoin est surtout le ponçage, les gravats, le bois ou la mobilité sans fil, les pages d’usage ou de fonctionnalité sont plus pertinentes. Ce découpage évite qu’une page « professionnel » absorbe toutes les intentions du site.</p>
<h2 id="sources">Sources et méthode</h2>
<p>Les caractéristiques proviennent des sources primaires liées dans les fiches modèles vérifiées au {UPDATED}. Le tableau ne prétend pas remplacer une évaluation du risque ni un test physique en conditions identiques.</p>
<p><small>Desk research, sans test physique. Aucun score d’affiliation n’est utilisé.</small></p>
</article><aside class="content-sidebar"><div class="sidebar-box"><div class="sidebar-box-head">Sommaire</div><div class="sidebar-box-body"><nav class="toc-list"><a href="#frontiere">Professionnel ≠ M</a><a href="#profils">4 profils</a><a href="#criteres">Critères</a><a href="#exemples">Références</a><a href="#limites">Limites</a><a href="#sources">Sources</a></nav></div></div><div class="sidebar-box"><div class="sidebar-box-head">Affiliation</div><div class="sidebar-box-body"><p class="affil-note">Ce site contient des liens affiliés. Nos analyses restent indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p></div></div></aside></div></div>
</main>'''

html = PATH.read_text(encoding='utf-8')
html = re.sub(r'<title>.*?</title>', '<title>Aspirateur de chantier professionnel : comparatif par profil 2026</title>', html, count=1, flags=re.S)
html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Comparatif professionnel par profil : mobilité, classe L ou M, décolmatage, volume et raccordement à l’outil selon le travail réel.">', html, count=1)
html = re.sub(r'<main>.*?</main>', body, html, count=1, flags=re.S)
PATH.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
print('✓ professional comparison intent override')
