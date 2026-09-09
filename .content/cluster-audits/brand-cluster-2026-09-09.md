# CLUSTER_AUDIT — pages marques

Date : 09/09/2026

## Snapshot audité

Le diagnostic de décision est basé sur le commit `7547c8ef4b1d6bb2602756312beecb1cdc1ad185`, c’est-à-dire le snapshot précédant le rollout global de la PR #10. Cela évite d’auditer les réécritures après coup.

## Rôle attendu des types de pages

- `/marques/<slug>/` : comprendre la logique de gamme, l’écosystème, les technologies et la prochaine étape de décision d’une marque.
- `/modeles/<slug>/` : vérifier une référence précise et ses caractéristiques documentées.
- `/comparatifs/<slug>/` : arbitrer entre plusieurs produits pour une même intention commerciale.
- `/usages/<slug>/` : résoudre un job-to-be-done non-brand (ponçage, plâtre, gravats, atelier, etc.).

Un hub marque ne doit pas devenir une fiche modèle ni un comparatif générique. Une page usage doit rester l’URL principale de l’intention non-brand correspondante.

## Verdicts du snapshot pré-PR #10

| Marque | Verdict | Confiance | Motif principal |
| --- | --- | ---: | --- |
| Bosch | KEEP | 90 % | Architecture déjà distincte : Home & Garden / GAS Professional / 18 V. |
| Kärcher | DEEP_REWRITE | 95 % | La décision WD vs NT puis Tact/classes doit dicter l’architecture. |
| Festool | DEEP_REWRITE | 95 % | Le système CTL/CTM/CTH, CLEANTEC et le workflow outil doivent structurer la page. |
| Makita | DEEP_REWRITE | 90 % | Nomenclature, LXT/XGT, AWS et classes par référence sont le vrai problème utilisateur. |
| DeWalt | LIGHT_UPDATE | 80 % | Le fond FLEXVOLT/DCV/AIRLOCK était déjà distinct ; surtout besoin de casser les blocs génériques. |
| Parkside | LIGHT_UPDATE | 85 % | Positionnement prix, disponibilité et générations PWD déjà différenciants. |
| Nilfisk | DEEP_REWRITE | 90 % | La séparation Buddy/Multi vs ATTIX et InfiniClean doit structurer le hub. |
| Mirka | DEEP_REWRITE | 95 % | Marque spécialisée : ponçage, DEXOS et DEROS/DEOS doivent dicter l’architecture. |

## Blockers cluster identifiés

1. Le générateur historique imposait aux marques une séquence commune `distinction → gamme → écosystème → forces → limites → choisir → éviter`.
2. La couche `/modeles/` contenait des données incomplètes et plusieurs erreurs de classification : modèles grand public présentés comme classe L, Festool CTL MIDI présenté comme M, Makita VC4210MX présenté comme L, champs `MM/AAAA` et valeurs manquantes.
3. Plusieurs pages `/usages/` n’étaient que des shells avec `<!-- Contenu à rédiger -->`, ce qui poussait les hubs marques à absorber des intentions non-brand.
4. `/marques/` utilisait des tiers non définis et des familles obsolètes (`DXV`, `PNTS`, `DE/DEROS`) comme résumé des marques.

## Ordre de production imposé

1. **MODEL_CLEANUP** — assainir la source de vérité et les fiches modèles critiques.
2. **USAGE_COMPLETION** — terminer les pages usage qui doivent absorber les intentions non-brand.
3. **BRAND_REVIEW** — revenir sur les hubs marques avec les verdicts ci-dessus, sans nouvelle réécriture automatique de DeWalt/Parkside.
4. **CLUSTER_PUBLISH_REVIEW** — relancer les checks d’intention, maillage, placeholders, classes et génération canonique.
5. Conserver `noindex, follow` tant que le gate global n’est pas explicitement validé.

## Décision sur la PR #10 déjà mergée

Le contenu de la PR #10 n’est pas automatiquement rejeté : les nouvelles structures peuvent être conservées si elles passent le publish review après assainissement des couches modèles/usages. En revanche, le verdict historique de récupération est corrigé pour DeWalt et Parkside : leur état pré-rollout relevait d’un `LIGHT_UPDATE`, pas d’un `MAJOR`.
