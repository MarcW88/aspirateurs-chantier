# Comparison workflow run evidence — contract v2

Ce dossier contient la preuve persistée qu'une page `/comparatifs/` a réellement exécuté la chaîne éditoriale 80/20.

Un fichier `<slug>.json` n'est créé qu'après un vrai passage du workflow. Le générateur Python n'a pas le droit de fabriquer ce fichier pour lui-même.

## Gouvernance

Le contrat d'exécution comprend 16 étapes partagées et 2 contrôles custom, soit 88,9 % de responsabilités shared :

Shared :
- seo-keyword
- jobs-to-be-done (PASS ou N/A motivé)
- seo-content-audit
- evidence-based-reviews
- fact-check-pre
- affiliate-value
- content-brief-authoring
- content-and-copy
- fact-check-post
- humanizer
- general-writing
- anti-ai-slop
- seo-onpage
- seo-technical
- internal-linking-audit
- editorial-qa

Custom :
- vacuum-comparison-decision-review
- comparison-analysis-publish-review

## Champs minimums

Chaque run doit au moins persister :
- `contract_version: 2`
- `slug`
- `status`
- `reader_decision`
- `comparison_scope`
- `value_without_affiliate_links`
- `candidate_scope.considered`
- `candidate_scope.major_exclusions`
- `outline[]` avec question, evidence_refs et decision_value
- `shared_steps`
- `custom_steps`
- `publish_review`

Chaque étape `PASS` doit contenir un résumé d'output concret. Une étape `N/A` doit être justifiée.

## Publication

Sans run v2 valide : `REQUIRES_WORKFLOW_RERUN` et maintien de `noindex, follow`.

Avec run v2 valide + `PASS — READY_FOR_HUMAN_VALIDATION` : la page peut passer en validation humaine, mais le workflow ne retire toujours jamais `noindex` automatiquement.
