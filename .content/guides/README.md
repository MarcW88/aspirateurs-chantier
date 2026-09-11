# Guide workflow records

Ce dossier contient la preuve persistante des runs réellement exécutés sur les pages `/guides/`.

## Principe

Un fichier `<slug>.json` n'est créé que lorsqu'un guide entre effectivement dans `guide-analysis-workflow` / `guide-content-workflow`.

Le simple fait qu'une page existe, qu'elle soit générée par `_generate_guides.py` ou qu'un validateur machine soit vert **ne suffit pas** pour créer un record ni pour lui attribuer `READY_FOR_HUMAN_VALIDATION`.

Les 11 guides peuvent donc exister sans record tant qu'ils n'ont pas encore été audités avec le workflow v1.

## Champs minimaux d'un record

```json
{
  "contract_version": 1,
  "slug": "classes-l-m-h",
  "url": "/guides/classes-l-m-h/",
  "guide_type": "EXPLAINER",
  "audit_decision": "LIGHT_UPDATE",
  "intent": {
    "reader_task": "..."
  },
  "value_to_preserve": ["..."],
  "evidence": [
    {
      "id": "S1",
      "claim": "...",
      "source": "...",
      "checked_at": "YYYY-MM-DD",
      "status": "SUPPORTED"
    }
  ],
  "outline": [
    {
      "question": "...",
      "evidence_refs": ["S1"],
      "decision_value": "..."
    }
  ],
  "workflow_execution": {
    "shared": [],
    "custom": []
  },
  "residual_risks": [],
  "editorial": {
    "publish_review": "PASS — READY_FOR_HUMAN_VALIDATION",
    "human_validation": false,
    "robots": "noindex, follow"
  }
}
```

## Workflow execution

Chaque étape partagée ou custom réellement attendue est enregistrée avec :

- `skill` ;
- `status`: `PASS` ou `N/A` ;
- `output` lorsque `PASS` ;
- `reason` lorsque `N/A`.

Les deux seules responsabilités custom autorisées sont :

- `guide-analysis-workflow` ;
- `guide-content-workflow`.

Le reste doit réutiliser les skills partagés déclarés dans `.agents/skills/guide-skill-stack.json`.

## Publication

Deux verdicts seulement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Même avec un PASS :

- `human_validation` reste `false` tant que Marc n'a pas validé explicitement ;
- la page reste `noindex, follow` ;
- aucune fusion, redirection ou indexation n'est déclenchée automatiquement.

Les validateurs vérifient la cohérence d'un record existant. Ils ne génèrent jamais la preuve à la place du workflow éditorial.
