# QA — Production des pages marques 2026

```yaml
status: DRAFT_READY
methodology_gate: PENDING_CI
editorial_gate: PENDING_CI
human_validation_required: true
indexing_status: noindex
publishable_for_indexing: false
```

## Contrôles attendus

- 8 pages BRAND_HUB générées : PENDING_CI
- Entity Map + gamme actuelle + positionnement + écosystème : PENDING_CI
- Statut de chaque famille/modèle : PENDING_CI
- 3+ sources primaires par marque : PENDING_CI
- Choose / Avoid + limites : PENDING_CI
- 9 H2 et 1 100+ mots par page : PENDING_CI
- 8+ liens internes et 7+ cibles uniques : PENDING_CI
- Pas de faux test / desk research explicite : PENDING_CI
- `noindex, follow` conservé : PENDING_CI
- Absence de `MM/AAAA` et placeholders : PENDING_CI
- Génération idempotente : PENDING_CI
- `git diff --check` : PENDING_CI

## Publication

La production peut être relue en PR. Le workflow interdit la fusion automatique sans validation humaine explicite. Une éventuelle fusion ne vaut pas demande d'indexation : le `noindex` reste une décision séparée.
