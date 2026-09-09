---
name: comparison-analysis-workflow
description: Workflow unique d'analyse des pages /comparatifs/ d'aspirateurs-chantier.fr. Orchestre majoritairement des skills réutilisables pour l'intention, l'audit, les preuves, le SEO et la QA, puis ajoute uniquement les contrôles spécifiques aux comparaisons d'aspirateurs de chantier. Décisions: KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: MarcW88/bloc-notes-numerique/comparison-analysis-workflow
  orchestration_target: ">=80% existing/vendored skills"
  custom_scope: "orchestration + vacuum comparison sanity + cluster boundaries"
---

# Comparison Analysis Workflow — Aspirateurs Chantier

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour `/comparatifs/`.

Il reste un orchestrateur : les méthodologies génériques vivent dans les skills partagés. La couche custom ne couvre que ce qui est réellement propre à la décision sur un aspirateur de chantier.

Principe :

> **Évaluer la qualité de la décision offerte au lecteur, pas la sophistication apparente de la méthodologie.**

Un comparatif peut être excellent sans score, pondération ou tableau exhaustif. Ces outils ne sont utilisés que lorsqu'ils améliorent réellement la décision.

---

# 1. Modes

## `AUDIT`
Analyse une URL existante et produit un diagnostic + décision, sans réécriture.

## `CLUSTER_AUDIT`
Compare les URLs `/comparatifs/` pour détecter chevauchement d'intention, recommandations recyclées, mêmes produits sous des promesses différentes et architectures industrialisées.

## `PUBLISH_REVIEW`
Gate final après rédaction :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais `noindex, follow`.

---

# 2. Entrées

Lire selon disponibilité :

- page cible ;
- comparatifs voisins ;
- `comparison-workflow.config.yaml` ;
- `.content/comparisons/<slug>.json` ;
- GSC / sémantique / historique ;
- SERP actuelle si l'intention est incertaine ou mouvante ;
- pages `/usages/`, `/marques/`, `/modeles/` et `/guides/` utiles ;
- `.content/models/model-evidence.json` et ledgers disponibles ;
- sources actuelles pour les faits susceptibles d'évoluer.

L'absence de données doit être signalée, jamais compensée par une précision inventée.

---

# 3. Chaîne principale — skills partagés obligatoires

## `seo-content-audit`
Décider quoi conserver, mettre à jour ou consolider. Examiner la cannibalisation sans réécrire par réflexe.

## `seo-keyword`
Confirmer requête/cluster, intention dominante, forme de SERP, rôle de l'URL et différences avec les comparatifs proches.

## `jobs-to-be-done`
À utiliser lorsque le contexte change réellement la décision : professionnel, mobilité, petit format, ponçage, gros volumes, etc. Ne pas inventer de persona.

## `evidence-based-reviews`
Distinguer specs officielles, synthèse d'expérience, preuves expertes et hands-on réel. Une fiche constructeur soutient un fait, pas une sensation d'usage inventée.

## `fact-check`
Vérifier modèles/générations, classe de poussière, fonctions, compatibilités, mesures, disponibilité et prix lorsqu'ils sont publiés.

## `affiliate-value`
La page doit rester utile sans liens affiliés : arbitrages, limites, incompatibilités, alternatives et conséquences pratiques.

## `seo-onpage`
Title, meta, H1, structure, contenu, liens, canonical, URL et schema honnête. Aucun quota de mots/H2/liens.

## `internal-linking-audit`
Vérifier que le comparatif route vers les guides, usages, marques et modèles correspondant aux prochaines questions du lecteur.

## `anti-ai-slop`
Détecter structure interchangeable, blocs produits symétriques, verdicts génériques et répétitions entre comparatifs.

## `editorial-qa`
QA finale sur intention, valeur originale, factualité, naturel, SEO et utilité réelle.

---

# 4. Couche custom minimale — sanity check Aspirateurs Chantier

## A. Périmètre crédible

- les produits sont réellement plausibles pour la requête ;
- les candidats évidents ont été considérés ou leur exclusion expliquée quand elle peut changer la décision ;
- un produit n'est jamais inclus seulement parce qu'il est monétisable ;
- le comparatif ne devient pas un catalogue exhaustif sans valeur.

## B. Critères avant recommandation

Les critères doivent découler de l'intention et des contraintes réelles. Selon la page, cela peut inclure :

- classe L/M/H lorsque pertinente ;
- type de poussière / usage autorisé ;
- maintien du débit et décolmatage automatique/semi-automatique ;
- raccordement à l'outil et prise asservie ;
- antistatique / flexibles conducteurs lorsque pertinent ;
- mobilité, poids et encombrement ;
- volume de cuve utile ;
- filaire vs batterie, plateforme batterie et autonomie documentée ;
- sacs, filtres, consommables et raccords ;
- eau/poussière lorsque c'est réellement l'intention ;
- coût de configuration lorsque décisionnel.

Ne jamais choisir le gagnant puis rationaliser les critères après coup.

## C. Sécurité et comparabilité honnête

Gates métier :

1. **Classe appareil ≠ filtre.** HEPA H13/H14 ne permet pas d'inférer une classe L/M/H.
2. **Puissance ≠ classe de sécurité.** Un aspirateur puissant n'est pas automatiquement adapté à une poussière dangereuse.
3. **Débit/dépression : contexte de mesure obligatoire.** Ne pas classer deux machines comme si des valeurs à la turbine, à l'entrée ou sous protocoles différents étaient directement équivalentes.
4. **Décolmatage ≠ certification.** AFC, Tact, InfiniClean, AUTOCLEAN ou équivalent améliorent potentiellement le maintien du débit mais ne remplacent pas une classe requise.
5. **Eau/poussière ≠ poussières dangereuses.** La polyvalence humide/sec ne prouve aucune aptitude réglementaire supplémentaire.
6. **Batteries : vérifier la plateforme exacte.** 18 V ou 40 V n'implique pas compatibilité entre univers ou marques.
7. **Cuve : distinguer brut/net/eau** si les fabricants emploient des métriques différentes.

## D. Verdict traçable

La page doit permettre de répondre :

- pourquoi ce choix est recommandé ;
- dans quelle situation un autre devient meilleur ;
- quelle limite ou contrainte peut faire changer de décision.

Un verdict conditionnel est souvent supérieur à un gagnant universel.

## E. Coût proportionné

Comparer le coût de la configuration réellement nécessaire lorsque cela change le choix : batterie/chargeur, sacs, filtres, raccords ou consommables indispensables. Ne pas imposer un TSC complexe à chaque page.

## F. Scoring optionnel

S'il existe : critères compréhensibles, notes clairement éditoriales sauf mesure réelle, pas de fausse précision, texte intelligible sans score. L'absence de score n'est jamais un blocker.

---

# 5. Cluster audit — frontières d'intention du site

Vérifier particulièrement :

- `/comparatifs/meilleur-aspirateur-de-chantier/` = décision générale multi-profils ;
- `/comparatifs/aspirateur-professionnel/` = profils de travail professionnels, pas un clone de classe M ;
- `/comparatifs/aspirateur-classe-m/` = intention explicitement centrée sur classe M ;
- `/comparatifs/aspirateur-chantier-puissant/` = puissance/capacité d'aspiration, sans prétendre qu'elle résout la sécurité ;
- `/comparatifs/aspirateur-eau-poussiere/` = polyvalence humide/sec ;
- `/comparatifs/aspirateur-chantier-sans-fil/` = mobilité + plateforme batterie/autonomie ;
- `/comparatifs/petit-aspirateur-de-chantier/` = encombrement/mobilité ;
- `/comparatifs/aspirateur-industriel/` = contexte réellement industriel, à distinguer du simple « professionnel » ;
- `/comparatifs/aspirateur-chantier-sans-sac/` = mode de collecte/consommables, pas une variante générique du comparatif général.

Chercher : mêmes H2 dans le même ordre, même intro substituée, mêmes produits et arguments sous plusieurs intentions, même verdict simplement repondéré, transitions/conclusions recyclées.

Le partage de composants visuels est normal. La pensée éditoriale clonée ne l'est pas.

---

# 6. Décisions

## `KEEP`
Page distincte, actuelle, utile et convaincante.

## `LIGHT_UPDATE`
Corrections locales : faits, sources, sélection secondaire, formulation, title/meta, maillage ou quelques arbitrages.

## `DEEP_REWRITE`
Réservé aux problèmes structurels : rôle/intention mal cadré, sélection inadéquate, recommandation non justifiable, faible valeur affiliée, architecture industrialisée, obsolescence substantielle ou preuves trop faibles.

## `MERGE`
Une autre URL sert essentiellement la même décision et la différenciation ne justifie pas deux pages.

## `NOINDEX`
Valeur ou justification insuffisante pour l'indexation. Aucune suppression/redirection automatique.

Pour chaque décision fournir : confiance, valeur à préserver, blockers, améliorations secondaires, données manquantes et prochaine étape.

---

# 7. PUBLISH_REVIEW

1. exécuter `python3 _validate_comparatifs.py` ;
2. rejouer les skills pertinents ;
3. comparer la structure aux pages sœurs ;
4. vérifier le verdict contre preuves et limites ;
5. vérifier l'absence de faux hands-on ;
6. vérifier title/H1/canonical/robots/schema ;
7. vérifier l'utilité sans affiliation ;
8. vérifier les gates métier L/M/H, mesures, batteries et compatibilités lorsqu'ils s'appliquent.

PASS : `PASS — READY_FOR_HUMAN_VALIDATION`

FAIL : `FAIL — KEEP_NOINDEX`

Un FAIL route vers le skill ou le gate concerné ; il ne déclenche pas automatiquement une réécriture totale.

---

# 8. Indexation

Conserver `noindex, follow` par défaut. Indexation uniquement après validateur machine sans blocker, PUBLISH_REVIEW PASS, validation humaine explicite et instruction explicite d'indexer.

---

# 9. Gouvernance 80/20

La méthode vient majoritairement des skills partagés/vendored. Le custom de ce workflow se limite à :

1. orchestration ;
2. sanity check comparatif propre aux aspirateurs de chantier ;
3. sécurité/comparabilité des claims métier ;
4. frontières et similarité du cluster `/comparatifs/` ;
5. mapping vers les décisions du site.

Ne jamais réimplémenter dans ce workflow les méthodologies portées par les skills partagés.