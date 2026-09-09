# PUBLISH_REVIEW — rollout pages marques — 2026-09-09

## Scope

Pages revues : Kärcher, Makita, Festool, DeWalt, Parkside, Nilfisk et Mirka.
Bosch a déjà fait l’objet du pilote bespoke précédent et reste protégé par la génération canonique.

## Recovery verdicts

| Marque | Verdict | Structure spécifique |
| --- | --- | --- |
| Kärcher | MAJOR | WD vs NT, Tact/ACD, classes de sécurité |
| Festool | MAJOR | système outil-aspirateur, CTL/CTM/CTH, AUTOCLEAN |
| Makita | MAJOR | décodage des références, VC, LXT/XGT, AWS |
| DeWalt | MAJOR | FLEXVOLT, DCV586M/DCV584L, AIRLOCK/TSTAK |
| Parkside | MAJOR | budget, disponibilité/révisions PWD, limites sécurité |
| Nilfisk | MAJOR | Buddy/Multi vs ATTIX, InfiniClean, classes |
| Mirka | MAJOR | ponçage sans poussière, DEXOS, DEROS/DEOS |

Aucun FULL rewrite n’était nécessaire : les ledgers existants contenaient déjà des faits, des sources primaires et des liens internes utiles. La réécriture porte principalement sur l’architecture, la hiérarchie de décision et les transitions trop génériques.

## Quality review

- Intent fit: PASS — chaque hub aide désormais à comprendre la logique propre de la marque avant de descendre au modèle.
- Evidence: PASS — les claims matériels utilisés restent adossés aux sources primaires déjà présentes dans les ledgers et dans le rendu.
- Safety claims: PASS — aucune classe L/M/H n’est déduite d’un filtre, d’une puissance ou d’un écosystème ; les usages à risque renvoient à l’évaluation appropriée.
- Fake hands-on / fabricated testing: PASS — toutes les pages indiquent qu’il s’agit d’une analyse documentaire.
- Structural differentiation: PASS — les anciens blocs génériques `forces`, `limites`, `pour qui`, `éviter` ne structurent plus les pages ; chaque marque possède sa propre signature H2.
- Internal linking: PASS — les liens conservés ou ajoutés servent un approfondissement vers modèles, guides, usages ou comparatifs pertinents.
- Humanizer / general writing / anti-AI-slop: PASS — deux micro-corrections post-review ont été intégrées à la génération canonique pour retirer du métadiscours et corriger une tournure.
- SEO / metadata: PASS — titles, H1 et descriptions ont été resserrés sur l’angle propre à chaque marque.
- TOC: PASS — chaque sidebar reflète les H2 réellement rendus.
- Machine integrity: PASS — génération, validation des 8 hubs, bespoke assertions, idempotence et whitespace ont passé sur GitHub Actions.
- Robots: PASS — `noindex, follow` est conservé sur toutes les pages.

## Architecture 80/20

La méthodologie partagée reste responsable de l’intention, du recovery, du fact-check, du maillage, du style, de l’anti-slop, du SEO et de la QA. La couche custom se limite aux décisions propres aux aspirateurs de chantier et à l’univers de chaque marque.

La commande canonique est `python _generate_brand_content.py` : générateur partagé -> override Bosch -> overrides des 7 autres marques -> polish éditorial. Le CI permanent régénère ensuite l’ensemble et échoue si un hub retombe dans la structure générique ou si les artefacts commités divergent.

## Final status

**PASS — READY_FOR_HUMAN_VALIDATION**

Aucune autorisation d’indexation n’est impliquée par ce statut.
