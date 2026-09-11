# Human validation — Comparatifs v2

Date : 2026-09-11

Validation humaine explicite reçue pour finaliser le rollout éditorial v2 des comparatifs et conserver les changements sur `main`.

## Pages validées

- `/comparatifs/meilleur-aspirateur-de-chantier/`
- `/comparatifs/aspirateur-professionnel/`
- `/comparatifs/aspirateur-classe-m/`
- `/comparatifs/aspirateur-chantier-puissant/`
- `/comparatifs/aspirateur-industriel/`
- `/comparatifs/aspirateur-chantier-sans-fil/`
- `/comparatifs/aspirateur-eau-poussiere/`
- `/comparatifs/petit-aspirateur-de-chantier/`

## Contrôles validés avant clôture

- gouvernance 80/20 : PASS ;
- run-evidence v2 : PASS ;
- machine integrity : PASS ;
- anti-template / frontières d’intention : PASS ;
- `noindex, follow` : conservé ;
- QA Playwright desktop/mobile : PASS après alignement du validateur visuel avec le contrat v2 où le `comparison-decision-module` est optionnel.

## Page non fusionnée automatiquement

`/comparatifs/aspirateur-chantier-sans-sac/` reste en attente d’une décision structurelle explicite de MERGE vers `/guides/sac-ou-sans-sac/`. Aucune suppression ni redirection n’est appliquée par cette validation.

## Indexation

Cette validation humaine autorise la finalisation du contenu sur `main`, mais ne constitue pas une instruction d’indexation. Les pages restent `noindex, follow` jusqu’à une instruction explicite séparée.
