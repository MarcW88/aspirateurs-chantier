---
name: brand-content-workflow
description: Orchestration custom de production/refonte des pages /marques/ d'aspirateurs-chantier.fr à partir d'une pile majoritairement partagée de skills génériques.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: bloc-notes-numeriques.fr/brand-content-workflow
  orchestration_target: ">=80% shared skills"
  custom_scope: "vacuum-domain rules, site architecture, tone and presentation"
---

# Brand Content Workflow — aspirateurs-chantier.fr

## Rôle

Ce workflow **orchestre** la production des pages `/marques/`. Il ne réimplémente pas l'intention, le fact-check, le humanizer, le SEO ou la QA : ces responsabilités appartiennent aux skills partagés du dépôt.

Principe : **shared skills pour la méthode ; custom uniquement pour l'univers aspirateurs de chantier et le site.**

Avant toute exécution :

```bash
python3 validate_brand_skill_stack.py
```

Un FAIL du skill stack bloque la production.

---

# 1. Entrées site-spécifiques

Lire :

- `brand-workflow.config.yaml` ;
- `_generate_brands.py` et `.content/brands/`, sources de vérité actuelles ;
- page cible + pages sœurs `/marques/` ;
- pages `/modeles/`, `/comparatifs/`, `/guides/`, `/usages/` utiles ;
- données GSC/sémantiques disponibles ;
- sources actuelles nécessaires à la vérification.

Ne jamais corriger seulement le HTML rendu si `_generate_brands.py` peut l'écraser.

Pour une page existante, commencer par `brand-analysis-workflow / AUDIT`.

---

# 2. Chaîne partagée obligatoire

Les skills ci-dessous sont **obligatoires lorsqu'ils correspondent à l'étape**, et non des fallbacks optionnels :

1. `search-intent` — intention, rôle et cannibalisation ;
2. `content-audit` — KEEP / UPDATE / MERGE / REDIRECT / REMOVE ;
3. `content-refresh` — uniquement après UPDATE ;
4. `fact-check` — evidence brief avant plan ;
5. `evidence-based-reviews` — dès qu'un jugement dépasse une simple spec ;
6. `affiliate-value` — valeur décisionnelle indépendante de l'affiliation ;
7. rédaction depuis les preuves ;
8. `fact-check` post-draft ;
9. `humanizer` → `general-writing` → `anti-ai-slop` ;
10. `internal-linking-audit` ;
11. `seo-technical` + `seo-best-practices` selon le stack ;
12. `editorial-qa` ;
13. `brand-analysis-workflow / PUBLISH_REVIEW`.

`humanizer` peut mobiliser `better-usage`, `writing-cadence`, `non-autoregressive-writing-pass` et, seulement si le genre le justifie, `academic-voice`.

Le workflow partagé `.agents/skills/content-recovery-and-production-workflow/SKILL.md` reste la couche de récupération générale et ne doit pas être recopié ici.

---

# 3. Custom — rôle d'une page marque sur ce site

Une URL `/marques/<slug>/` est principalement un `BRAND_HUB`.

Elle doit aider à comprendre **comment choisir dans l'univers de cette marque**, puis router vers `/modeles/`, `/comparatifs/`, `/guides/` ou `/usages/`.

Elle ne doit pas devenir :

- une fiche modèle géante ;
- un comparatif général recopié ;
- un catalogue constructeur ;
- la même page que les autres marques avec substitutions de noms.

Le plan vient de l'intention et des preuves. Aucun ordre de H2 n'est imposé.

---

# 4. Custom — garde-fous aspirateurs de chantier

Lorsqu'ils sont décisionnels, vérifier et contextualiser :

- classes L / M / H et rôle réel d'un aspirateur de sécurité ;
- filtre HEPA ou niveau de filtration **sans** l'assimiler à une classe de sécurité ;
- débit d'air et dépression avec protocole/point de mesure lorsqu'il est connu ;
- capacité brute, nette et volume d'eau ;
- décolmatage manuel/automatique ;
- prise asservie ou démarrage avec outil ;
- antistatique ;
- raccords et compatibilités outils ;
- plateformes batterie et incompatibilités entre gammes ;
- sacs, filtres, consommables et disponibilité ;
- eau/poussière versus poussières potentiellement dangereuses ;
- poids, mobilité, encombrement et volume ;
- statut actuel du modèle ou de la génération.

Règles absolues :

- ne jamais déduire une classe de sécurité depuis puissance, débit ou filtre ;
- ne pas comparer des métriques fabricants comme directement équivalentes si la mesure diffère ;
- ne jamais transformer une donnée fabricant en observation propre au site ;
- ne pas fournir de conseil réglementaire personnalisé sur un risque poussière.

---

# 5. Custom — valeur propre à chaque marque

Chercher la logique qui change réellement la décision, par exemple :

- nomenclature ou familles distinctes ;
- univers bricolage vs professionnel ;
- écosystème batterie ;
- intégration outil/aspirateur ;
- raccords, coffrets et consommables ;
- classes disponibles ;
- mobilité vs capacité ;
- coût total d'écosystème ;
- situations où une autre marque est rationnellement plus cohérente.

Exemples d'angles, jamais de templates : Bosch peut se lire via DIY/Professional et ses univers 18 V ; Festool via l'intégration outil/aspiration ; Kärcher via WD/NT et le passage eau/poussière → sécurité professionnelle.

---

# 6. Custom — ton et mise en avant

Conserver le ton d'aspirateurs-chantier.fr : expert mais lisible, pratique, sobre, comparatif, précis sur les limites et transparent sur la provenance des données.

Éviter superlatifs sans critères, transitions génériques, conclusions récapitulatives et formulations interchangeables entre marques.

Conserver le design system existant :

- `answer-box` si une réponse courte aide réellement ;
- `table-wrap` seulement quand le tableau réduit une ambiguïté ;
- `related-box`, sidebar, affiliation et styles existants ;
- TOC calculée depuis les vrais headings.

La cohérence visuelle ne dicte jamais l'architecture éditoriale.

---

# 7. Persistance et publication

Conserver dans `.content/brands/` ou `.content/reviews/` : intention, evidence brief, statuts de claims, sources/date, valeur originale, justification du plan et résultat de QA.

Par défaut : `noindex, follow`.

Avant indexation :

1. `validate_brand_skill_stack.py` PASS ;
2. `_validate_brands.py` sans blocker ;
3. `brand-analysis-workflow / PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
4. validation humaine explicite ;
5. instruction explicite de rendre la page indexable.

Le custom s'arrête là : toute règle générique supplémentaire doit être ajoutée au skill partagé approprié, pas dupliquée dans ce workflow.
