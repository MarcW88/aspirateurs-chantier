---
name: brand-analysis-workflow
description: Orchestration custom d'audit et de publish review des pages /marques/ d'aspirateurs-chantier.fr, appuyée sur une pile majoritairement partagée de skills génériques.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: bloc-notes-numeriques.fr/brand-analysis-workflow
  orchestration_target: ">=80% shared skills"
  custom_scope: "vacuum-domain risk checks, cluster distinctiveness, site tone and publish gate"
---

# Brand Analysis Workflow — aspirateurs-chantier.fr

## Rôle et modes

Ce workflow décide et contrôle ; il ne rédige pas par défaut.

- `AUDIT` : une page existante ;
- `CLUSTER_AUDIT` : plusieurs pages marques et leurs chevauchements ;
- `PUBLISH_REVIEW` : gate final du draft.

Avant l'audit :

```bash
python3 validate_brand_skill_stack.py
```

Un FAIL bloque l'analyse éditoriale finale : la pile partagée doit être disponible.

---

# 1. Chaîne partagée obligatoire

Déléguer les contrôles génériques aux skills dédiés :

- `search-intent` ;
- `content-audit` puis `content-refresh` si UPDATE ;
- `affiliate-value` ;
- `fact-check` ;
- `evidence-based-reviews` pour tout jugement important ;
- `internal-linking-audit` ;
- `humanizer`, `general-writing`, `anti-ai-slop` en review du draft ;
- `seo-technical`, `seo-best-practices` ;
- `editorial-qa`.

Ne pas recopier leurs checklists ici. Le workflow `.agents/skills/content-recovery-and-production-workflow/SKILL.md` couvre la logique générale de récupération.

---

# 2. Custom — rôle et frontière de page

Les `/marques/<slug>/` sont surtout des `BRAND_HUB`; les fiches détaillées vivent plutôt sous `/modeles/`.

Vérifier que la page explique la logique de gamme, les systèmes/technologies qui changent le choix, l'écosystème utile et la prochaine étape du parcours sans dupliquer une fiche modèle ou un comparatif générique.

Le type de page sert de garde-fou, jamais de template de headings.

---

# 3. Custom — contrôle métier aspirateurs

Contrôler avec attention les claims sur :

- classes L/M/H ;
- filtre vs classe de sécurité ;
- débit/dépression et contexte de mesure ;
- capacité brute/net/eau ;
- décolmatage ;
- prise asservie ;
- antistatique ;
- compatibilités outils/raccords ;
- plateformes batterie ;
- consommables ;
- eau/poussière vs poussières dangereuses ;
- poids/mobilité ;
- génération/statut du produit.

FAIL si une classe est déduite d'une puissance/filtration, si des métriques non comparables sont présentées comme équivalentes, ou si une donnée fabricant devient une observation maison.

---

# 4. Custom — distinctivité du cluster

Comparer la page aux marques sœurs :

- H2/H3 et ordre ;
- fonction des sections ;
- introduction / answer-box ;
- emplacement systématique tableaux et CTA ;
- paragraphes de transition ;
- mêmes blocs forces/limites/pour qui/éviter ;
- conclusions et routage interne ;
- arguments génériques interchangeables.

Une cohérence visuelle est normale. Une architecture éditoriale dictée par `_generate_brands.py` plutôt que par la marque est un signal fort de `DEEP_REWRITE`.

---

# 5. Custom — ton et design

La page doit rester pratique, experte, sobre et compréhensible par un bricoleur exigeant sans perdre la précision utile aux pros.

Les limites doivent être aussi visibles que les avantages. Aucune expérience de première main sans preuve réelle.

Conserver les composants du site (`answer-box`, `table-wrap`, `related-box`, sidebar, affiliation) sans les transformer en sections obligatoires.

---

# 6. Décision AUDIT / CLUSTER_AUDIT

- `KEEP` : page forte, actuelle, distincte et utile.
- `LIGHT_UPDATE` : corrections ciblées sans reconstruction substantielle.
- `DEEP_REWRITE` : intention mal servie, architecture clonée/générique, valeur trop marchande ou raisonnement à reconstruire.
- `MERGE` : intention pratiquement identique à une autre URL.
- `NOINDEX` : valeur/justification encore insuffisante.

Retourner confiance, preuves, unknowns, blockers, valeur existante, actions et prochaine étape.

`DEEP_REWRITE` route vers `brand-content-workflow`.

---

# 7. PUBLISH_REVIEW

Exécuter :

```bash
python3 validate_brand_skill_stack.py
python3 _validate_brands.py
```

Puis vérifier les résultats des skills partagés et les gates custom :

- preuves et niveau d'expérience honnêtes ;
- aucun blocker métier L/M/H ou métrique ;
- architecture propre à la marque ;
- pas de clonage substantiel ;
- ton/design cohérents sans template éditorial ;
- source de vérité et HTML rendu cohérents ;
- `noindex, follow` conservé.

Résultat :

`PASS — READY_FOR_HUMAN_VALIDATION`

ou

`FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais le noindex automatiquement.

Toute nouvelle règle générique doit être portée par le skill partagé correspondant, pas ajoutée ici.
