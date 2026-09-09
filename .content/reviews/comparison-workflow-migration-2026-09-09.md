# Comparison workflow migration — 2026-09-09

## Scope

Migration méthodologique uniquement. Aucun comparatif n'est réécrit dans cette étape.

## Source

- `MarcW88/bloc-notes-numerique/.agents/skills/comparison-analysis-workflow/SKILL.md`
- `MarcW88/bloc-notes-numerique/.agents/skills/comparison-content-workflow/SKILL.md`

## Adaptation cible

`aspirateurs-chantier.fr` : comparatifs d'aspirateurs de chantier, aspirateurs eau/poussière, classes L/M/H, usages professionnels, mobilité/batterie et contraintes de captage.

## Gouvernance 80/20

- shared / vendored : **15 composants**
- custom : **2 workflows**
- ratio shared : **88,2 %**
- seuil minimum : **80 %**

Les skills shared couvrent audit, intent/keywords, JTBD, evidence, fact-check, affiliate value, brief, rédaction, humanisation, anti-slop, SEO, maillage et QA.

Le custom est limité à :

- orchestration des comparatifs ;
- critères propres à l'aspiration de chantier ;
- sécurité et comparabilité des claims (L/M/H, filtre, débit/dépression, décolmatage, wet/dry, batteries, capacités, consommables) ;
- frontières du cluster `/comparatifs/` ;
- PUBLISH_REVIEW.

## Changement de philosophie

L'ancien workflow imposait de facto pondérations, somme à 100, hard gate, scoring et ranking. La nouvelle version les rend **optionnels**.

Reste obligatoire :

1. intention claire ;
2. scope raisonnable ;
3. critères avant recommandation ;
4. preuves adaptées au claim ;
5. verdict traçable ;
6. limites visibles ;
7. indépendance de l'affiliation ;
8. sécurité des claims métier ;
9. différenciation du cluster ;
10. PUBLISH_REVIEW + validation humaine avant indexation.

## Ordre d'application recommandé après merge

1. `comparison-analysis-workflow / CLUSTER_AUDIT` sur les 9 URLs existantes ;
2. verdict par page : KEEP / LIGHT_UPDATE / DEEP_REWRITE / MERGE / NOINDEX ;
3. traitement page par page selon le verdict ;
4. PUBLISH_REVIEW du cluster ;
5. conservation de `noindex, follow` jusqu'à validation humaine explicite.
