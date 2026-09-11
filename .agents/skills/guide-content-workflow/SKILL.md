---
name: guide-content-workflow
description: Workflow unique de production et correction des guides SEO/GEO sous /guides/ d'aspirateurs-chantier.fr. Adapté de MarcW88/bloc-notes-numerique. Utiliser après guide-analysis-workflow lorsqu'une page existante nécessite LIGHT_UPDATE ou DEEP_REWRITE, ou pour créer un nouveau guide. Orchestre majoritairement des skills existants pour intention, recherche, preuves, brief, rédaction et QA.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_skill: .agents/skills/guide-content-workflow/SKILL.md
  source_sha: 7562fb6c569ef18d4ec0bccecd6584d559f90291
  adapted_for: aspirateurs-chantier.fr
  orchestration_target: ">=80% existing skills"
  custom_scope: "guide routing + vacuum-domain integrity + category boundaries + source-of-truth integration"
---

# Guide Content Workflow — aspirateurs-chantier.fr

## Rôle

C'est le **seul workflow de production/correction** à utiliser pour les URLs sous `/guides/`.

Séquence normale :

`guide-analysis-workflow / AUDIT` → décision → correction si nécessaire → `guide-analysis-workflow / PUBLISH_REVIEW`.

Décisions consommées :

- `KEEP` → ne pas réécrire ;
- `LIGHT_UPDATE` → corriger uniquement le scope identifié ;
- `DEEP_REWRITE` → reconstruire la page tout en préservant les éléments valides ;
- `MERGE` / `NOINDEX` → ne pas produire une nouvelle version sans décision humaine sur le rôle de l'URL.

Pour une nouvelle URL, effectuer intention, recherche, preuves et brief avant toute rédaction.

Le workflow ne retire jamais `noindex, follow` de lui-même.

---

# 1. Entrées

Lire avant toute production :

- `AGENTS.md` et `DESIGN.md` si le rendu est concerné ;
- `guide-workflow.config.yaml` ;
- `.agents/skills/guide-analysis-workflow/SKILL.md` ;
- `.agents/skills/guide-skill-stack.json` ;
- l'audit de la page lorsqu'elle existe ;
- la page cible et sa source de vérité ;
- `_generate.py` pour le shell global et `_generate_guides.py` pour la source éditoriale Guide actuelle ;
- `_guide_classes_lmh_pilot.py` et `_guide_quality_supplements.py` lorsqu'ils touchent la page ;
- `.content/guides/<slug>.json`, `.content/briefs/<slug>.md` et `.content/reviews/<slug>.md` lorsqu'ils existent ;
- les guides voisins ;
- les pages usages, comparatifs et marques qui répondent à des sous-questions proches ;
- les données sémantiques, GSC ou autres signaux disponibles ;
- les sources nécessaires aux faits actuels.

Ne pas utiliser la mémoire du modèle pour combler un manque factuel. Pour une page existante, préserver explicitement la valeur identifiée par l'AUDIT.

---

# 2. Router le travail sans créer un template

Identifier le travail dominant uniquement pour choisir les risques à vérifier :

- `CHOICE` — aider à arbitrer entre options, contraintes ou approches ;
- `EXPLAINER` — expliquer une technologie, une mesure, une classe ou un mécanisme ;
- `HOW_TO` — permettre une tâche ou une procédure vérifiable ;
- `HYBRID` — seulement si plusieurs fonctions sont réellement nécessaires.

Lire si utile :

- `references/choice-guide.md` ;
- `references/explainer-guide.md` ;
- `references/how-to-guide.md`.

Ces références sont des **questions de contrôle**, pas des architectures à reproduire. Elles n'imposent ni ordre ni nombre de sections, tableau, FAQ, checklist ou nombre d'étapes.

---

# 3. Chaîne de production fondée sur les skills partagés

## Étape 1 — intention, cluster et rôle

Utiliser :

- `seo-keyword` lorsque recherche, clustering ou validation du topic est nécessaire ;
- `search-intent` pour la tâche exacte, les sous-questions et le résultat attendu ;
- `seo-content-audit` et `content-refresh` pour une page existante lorsque l'audit l'a demandé.

Confirmer : requête/topic principal, intention, tâche ou décision du lecteur, périmètre, prochaine étape logique et chevauchements internes.

### Gate de frontière

Un guide ne doit pas devenir une page Usage traitant le job complet, un Comparatif classant des produits, ni une page Marque centrée sur un écosystème. Si le rôle est incorrect, renvoyer vers `guide-analysis-workflow` plutôt que forcer le texte dans le slug.

## Étape 2 — recherche et registre de preuves

Utiliser `fact-check` pour les claims vérifiables.

Adapter la recherche à la stabilité :

- mécanisme physique stable → exactitude et source solide ;
- norme, réglementation, compatibilité, gamme, génération produit ou procédure constructeur → vérification actuelle ;
- jugement expérientiel produit important → `evidence-based-reviews` si nécessaire.

Pour les claims importants, conserver : affirmation, source, date de consultation, portée/conditions, stabilité et niveau d'incertitude. Une inconnue reste inconnue, qualifiée ou exclue.

## Étape 3 — questions propres au type dominant

### `CHOICE`
Documenter seulement ce qui change l'arbitrage : critères, compromis, critères éliminatoires, dépendances et situations où chaque option cesse d'être adaptée. Ne pas créer de podium produit.

### `EXPLAINER`
Documenter concept, termes voisins, mécanisme, causalité, conséquence pratique, limites, contexte de mesure et exceptions. Une définition seule n'est pas une explication.

### `HOW_TO`
Documenter contexte, prérequis, méthode vérifiée, variantes machine/accessoire, résultat attendu, vérification, échecs probables et alternatives utiles. Ne jamais inventer une étape parce qu'elle semble probable.

## Étape 4 — intégrité technique aspirateurs

Avant le brief, appliquer les règles métier de `guide-analysis-workflow` :

- ne jamais inférer L/M/H depuis HEPA, puissance, débit, dépression ou décolmatage ;
- distinguer certification machine, média filtrant et classe de poussière ;
- distinguer débit, dépression et puissance électrique ;
- comparer des chiffres seulement si leur contexte de mesure est compatible ;
- distinguer capacité brute/nette/eau ;
- vérifier compatibilités outil/flexible/batterie/sac/filtre lorsqu'elles changent la procédure ou la décision ;
- ne pas confondre prise asservie et déclenchement sans fil ;
- traiter amiante, silice et poussières réglementées avec prudence et renvoi vers les prescriptions applicables.

## Étape 5 — `affiliate-value` lorsque pertinent

Si le guide influence l'achat, utiliser `affiliate-value` avant la rédaction finale. La page doit rester utile sans lien affilié.

## Étape 6 — brief propre à la page

Utiliser `content-brief-authoring` et conserver les champs utiles de `references/brief-template.md` : intention/tâche, valeur propre, périmètre/exclusions, faits et entités, preuves, risques, valeur à préserver, maillage, angle et structure **issue de la recherche**.

Il n'existe **aucune architecture éditoriale obligatoire par type de guide**. Chaque grande section doit être justifiable par une question, une étape, une distinction, une preuve, un arbitrage ou une limite.

## Étape 7 — rédaction

Utiliser `content-and-copy` à partir du brief et du registre de preuves.

Règles : répondre tôt, français naturel/précis/sobre, expliquer les conséquences pratiques, distinguer faits/interprétations/inconnues, aucun faux test ou mesure, formats seulement s'ils clarifient, pas de FAQ mécanique ni ranking produit, et préserver en LIGHT_UPDATE les éléments valides.

### Source de vérité canonique

Le shell global peut être régénéré par `_generate.py`, mais **la source éditoriale actuelle de `/guides/` est `_generate_guides.py`**, complétée selon les cas par `_guide_classes_lmh_pilot.py`, `_guide_quality_supplements.py` et `_normalize_guide_answers.py`.

Toute correction doit être intégrée à cette chaîne canonique ou à une future source éditoriale explicitement appelée par elle. Ne jamais corriger uniquement `guides/<slug>/index.html`, car une régénération pourrait écraser le travail.

---

# 4. Contrôles post-rédaction

Exécuter les passes séparément :

1. relancer `fact-check` sur les claims réellement écrits ;
2. `internal-linking-audit` ;
3. `humanizer` ;
4. `general-writing` avec le minimum de changements ;
5. `anti-ai-slop` en review/detection ;
6. `seo-drift` seulement avec baseline utile ;
7. `seo-onpage` ;
8. `seo-technical` ;
9. `seo-best-practices` seulement pour les règles applicables ;
10. `editorial-qa` ;
11. lecture complète dans l'ordre rendu, desktop/mobile lorsque disponible.

Aucun PASS de skill ne peut être déduit d'une simple relecture générique.

---

# 5. Traçabilité du run

Pour chaque guide travaillé, persister `.content/guides/<slug>.json` avec au minimum :

- slug, URL, type dominant ;
- décision AUDIT ;
- intention / reader task ;
- valeur existante à préserver ;
- registre de preuves ;
- outline evidence-led ;
- exécution des skills partagés réellement utilisés ;
- exécution des deux orchestrateurs custom ;
- risques résiduels ;
- `editorial.publish_review` ;
- `editorial.human_validation: false` tant qu'aucune validation humaine n'a été donnée ;
- `editorial.robots: "noindex, follow"` tant que l'indexation n'a pas été explicitement demandée.

Un validator machine ne peut pas fabriquer ce record ni auto-attribuer un PASS éditorial.

---

# 6. PUBLISH_REVIEW obligatoire

Une fois la correction/rédaction terminée, passer à `guide-analysis-workflow / PUBLISH_REVIEW`, qui exécute :

- `python3 validate_guide_workflow.py` ;
- `python3 validate_guide_quality.py` ;
- les gates substantiels ;
- la comparaison au cluster.

Résultats possibles :

- `PASS — READY_FOR_HUMAN_VALIDATION` ;
- `FAIL — KEEP_NOINDEX`.

Un PASS reste suivi d'une validation humaine explicite avant toute instruction d'indexation.

---

# 7. Handoffs

- vers `usage-content-workflow` lorsque la vraie question est le job complet ;
- vers `comparison-content-workflow` lorsqu'il faut sélectionner/classer des produits ;
- vers `brand-content-workflow` lorsque la question porte principalement sur une marque ou une gamme.

---

# 8. Ce que ce workflow ne doit pas devenir

Ne pas ajouter : quota de mots, minimum de H2/H3, quota de liens/sources, nombre obligatoire d'étapes, tableau ou FAQ obligatoire, score qualité artificiel, architecture fixe par type, ni seconde copie des règles de fact-check/SEO/rédaction déjà couvertes par les skills partagés.
