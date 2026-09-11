# Usage records — contract

Chaque page `/usages/<slug>/` peut disposer d'un record `.content/usages/<slug>.json` créé **avant** une correction via `usage-content-workflow`.

Le record sert à conserver les résultats du workflow partagé sans laisser le générateur ou le HTML devenir la source de vérité éditoriale.

Champs recommandés :

- `slug`, `url`, `updated_at` ;
- `intent` : query/topic, intention, user job, boundary ;
- `jtbd` : circumstances, progress/outcome, frictions utiles, evidence class ;
- `workflow` : tâches et frictions réellement pertinentes au job ;
- `criteria` : critère, priorité éventuelle, conséquence dans le job ;
- `evidence` : claim, source, date, stabilité, classe `OBSERVED|SUPPORTED|INFERRED|HYPOTHESIS|UNKNOWN` ;
- `handoffs` : guides/comparatifs/marques qui portent les sous-questions voisines ;
- `editorial` : décision `KEEP|LIGHT_UPDATE|DEEP_REWRITE|MERGE|NOINDEX`, publish review et validation humaine.

## Règles

- Aucun ranking produit n'est stocké comme source de vérité d'une page usage.
- Une classe L/M/H doit être explicitement sourcée ; elle n'est jamais inférée depuis HEPA, puissance, débit ou décolmatage.
- Les critères dérivent du job et de ses frictions, pas de la disponibilité des specs produit.
- Le record ne peut pas auto-accorder l'indexation.
- Pendant la récupération, les pages restent `noindex, follow` jusqu'à instruction explicite après validation humaine.

Le contrat méthodologique principal reste dans :

- `.agents/skills/usage-analysis-workflow/SKILL.md` ;
- `.agents/skills/usage-content-workflow/SKILL.md` ;
- `.agents/skills/usage-skill-stack.json` ;
- `usage-workflow.config.yaml`.
