---
name: brand-analysis-workflow
description: Workflow d'analyse des pages /marques/ d'aspirateurs-chantier.fr. Audite une page ou le cluster, contrôle intention, valeur affiliée, preuves, sécurité des claims, structure, ton éditorial, maillage et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En mode PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: bloc-notes-numeriques.fr/brand-analysis-workflow
---

# Brand Analysis Workflow — aspirateurs-chantier.fr

## Rôle

C'est le workflow d'analyse à utiliser pour les URLs sous `/marques/`.

Il reprend la logique du workflow de `bloc-notes-numeriques.fr`, mais l'adapte au marché des aspirateurs de chantier, à la structure statique du dépôt et au ton du site.

Il ne réécrit pas la page par défaut. Il produit un diagnostic, une décision et un plan de correction. Les pages `/modeles/`, `/comparatifs/`, `/guides/` et `/usages/` gardent leurs propres workflows.

## Modes

### `AUDIT`
Mode par défaut pour une page existante.

### `CLUSTER_AUDIT`
Compare plusieurs pages `/marques/` afin de détecter cannibalisation, duplication de rôle et industrialisation éditoriale.

### `PUBLISH_REVIEW`
Gate final après rédaction. Retourne :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais `noindex, follow` automatiquement.

---

# 1. Entrées

Lire avant l'audit :

- `brand-workflow.config.yaml` ;
- `_generate_brands.py`, source de vérité actuelle du cluster ;
- page cible et pages sœurs pertinentes ;
- `.content/brands/` et `.content/reviews/` si présents ;
- données GSC, sémantiques ou historiques lorsqu'elles existent ;
- sources actuelles lorsque les faits peuvent avoir évolué.

Ne jamais inventer une donnée absente pour compléter l'audit.

Pour une page existante, vérifier la source de vérité et le HTML rendu : un correctif appliqué uniquement au HTML généré est incomplet s'il sera écrasé au prochain build.

---

# 2. Chaîne d'analyse

Réutiliser en priorité le workflow `.agents/skills/content-recovery-and-production-workflow/SKILL.md` pour les contrôles génériques de récupération : intention, valeur utile, contenu générique, obsolescence, fact-check, maillage, QA éditoriale et SEO.

Lorsque les skills spécialisés cités par ce workflow sont disponibles dans l'environnement, les exécuter selon leur rôle : `search-intent`, `content-refresh`, `affiliate-value`, `fact-check`, `internal-linking-audit`, `humanizer`, `anti-ai-slop`, `seo-technical`, `seo-best-practices` et `editorial-qa`.

Pour les jugements produit, ne jamais transformer une fiche fabricant ou un test tiers en expérience propre au site. Une page de marque de ce dépôt est, sauf preuve contraire, une **analyse documentaire**.

---

# 3. Contrôle métier propre aux aspirateurs de chantier

Les claims techniques ne sont pas tous équivalents. Contrôler en priorité les éléments qui changent réellement une décision ou touchent à la sécurité :

- classe de poussière L, M ou H ;
- rôle exact d'un aspirateur de sécurité ;
- débit d'air et dépression, avec le point de mesure lorsqu'il est connu ;
- capacité brute, nette et volume d'eau ;
- décolmatage manuel ou automatique ;
- prise asservie / démarrage avec outil ;
- système antistatique ;
- raccords et compatibilités avec les outils ;
- plateformes batterie et incompatibilités entre gammes ;
- filtres, sacs, consommables et disponibilité ;
- eau/poussière versus poussières dangereuses ;
- poids, mobilité et volume quand ils modifient l'usage ;
- statut réel du modèle ou de la génération.

## Règles de prudence

- Ne jamais déduire une classe de sécurité à partir d'un filtre HEPA, d'une puissance ou d'un débit.
- Ne pas comparer deux chiffres fabricants comme s'ils étaient directement équivalents lorsque le protocole ou le point de mesure diffère.
- Ne pas présenter une fonction fabricant comme un résultat mesuré par la rédaction.
- Pour une poussière potentiellement dangereuse, garder une formulation qui renvoie au risque, aux prescriptions applicables et à la classe requise, sans transformer la page en conseil réglementaire personnalisé.

---

# 4. Adéquation au rôle de page

Le type de page est une grille de risque, pas un template.

Types possibles : `DIRECTORY`, `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB`, `ALTERNATIVES`.

Sur l'architecture actuelle du site, les URLs `/marques/<slug>/` sont principalement des `BRAND_HUB`. Les produits détaillés se trouvent plutôt sous `/modeles/` : ne pas dupliquer une fiche modèle dans une page marque.

Pour un `BRAND_HUB`, vérifier notamment :

- le vrai principe de lecture de la gamme ;
- les familles ou technologies qui changent le choix ;
- l'écosystème utile : outils, batteries, coffrets, raccords, filtres et consommables ;
- les limites concrètes ;
- les usages pour lesquels la marque est ou non cohérente ;
- la prochaine page logique du site.

Aucune section n'est obligatoire uniquement parce qu'elle existe chez une autre marque.

---

# 5. Contrôle de similarité structurelle du cluster

C'est un gate majeur sur ce dépôt.

Comparer :

- H2/H3 et leur ordre ;
- forme de l'introduction et de l'`answer-box` ;
- répétition des blocs gamme / écosystème / forces / limites / pour qui / éviter ;
- emplacement systématique des tableaux et CTA ;
- paragraphes de transition recyclés ;
- mêmes arguments génériques appliqués à plusieurs marques ;
- même conclusion ou même routage interne avec simple substitution du nom de marque.

Une cohérence visuelle est souhaitable. Un squelette éditorial identique ne l'est pas.

### FAIL structurel

La page mérite `DEEP_REWRITE` lorsque l'architecture semble dictée par `_generate_brands.py` plutôt que par les questions propres à la marque.

Signaux forts :

- mêmes rôles de sections dans le même ordre sur plusieurs marques ;
- phrases génériques identiques d'une page à l'autre ;
- blocs « pour qui / à éviter » produits par obligation plutôt que par besoin ;
- tableau de gamme présent alors qu'une autre représentation serait plus utile ;
- contenu que l'on peut permuter entre deux marques sans changer le raisonnement.

---

# 6. Ton of voice et mise en avant

La page doit rester cohérente avec aspirateurs-chantier.fr :

- expertise pratique et vocabulaire précis ;
- ton sobre, comparatif et non promotionnel ;
- réponse utile rapidement, sans intro marketing ;
- distinction claire entre données fabricant et interprétation éditoriale ;
- limites visibles au même niveau que les avantages ;
- pas de faux test ni de première personne d'expérience si aucun hands-on n'existe ;
- formulations compréhensibles pour un bricoleur exigeant sans perdre la précision utile aux pros.

Conserver le design system existant : `answer-box`, tableaux dans `table-wrap` lorsque nécessaires, encadrés associés et sidebar. La cohérence visuelle ne doit pas forcer la même architecture éditoriale.

---

# 7. Contrôle des preuves

Hiérarchie par défaut :

1. fabricant, documentation et manuel officiel ;
2. distributeur officiel ;
3. retailer fiable pour disponibilité ou information commerciale complémentaire ;
4. tests et médias spécialisés indépendants nommés ;
5. plusieurs sources utilisateurs lorsqu'un pattern d'expérience est réellement étudié.

Statuts : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

`UNKNOWN` et `CONTRADICTED` ne peuvent pas devenir une certitude rédactionnelle.

Pour les marques, vérifier la fraîcheur des gammes et modèles : la présence chez un revendeur ne suffit pas toujours à établir qu'un produit fait encore partie de la gamme actuelle.

---

# 8. Décision finale AUDIT / CLUSTER_AUDIT

### `KEEP`
Page forte, actuelle, distincte et utile.

### `LIGHT_UPDATE`
Corrections ciblées : faits, sources, liens, formulations ou faiblesse locale sans changement fondamental d'architecture.

### `DEEP_REWRITE`
Intent mal servi, architecture générique ou clonée, valeur marchande trop forte, preuves insuffisantes ou besoin de reconstruire le raisonnement.

### `MERGE`
Une autre URL couvre pratiquement la même intention et la distinction ne justifie pas deux pages.

### `NOINDEX`
La page n'a pas encore assez de valeur ou de justification pour être indexée.

Pour chaque décision fournir :

- confiance ;
- preuves utilisées ;
- unknowns ;
- blockers ;
- valeur déjà présente ;
- actions nécessaires ;
- prochaine étape.

Pour `DEEP_REWRITE`, passer la main à `brand-content-workflow`.

---

# 9. Mode PUBLISH_REVIEW

## Étape A — validation machine

Exécuter :

```bash
python3 _validate_brands.py
```

Le validateur machine vérifie uniquement des signaux structurels et d'intégrité observables. Il ne doit pas imposer un nombre de mots, de H2 ou de liens, ni un plan fixe.

## Étape B — gates substantiels

Vérifier au minimum :

- intention satisfaite ;
- valeur originale même sans affiliation ;
- claims importants sourcés ;
- sécurité des formulations L/M/H ;
- niveau de preuve honnête ;
- pas de faux test ;
- pas de merchant rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture propre à la marque ;
- absence de clonage structurel substantiel avec les pages sœurs ;
- title/H1/canonical/robots cohérents ;
- liens internes utiles ;
- design cohérent avec le site sans template éditorial forcé.

## Étape C — résultat

PASS :

`PASS — READY_FOR_HUMAN_VALIDATION`

FAIL :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le workflow approprié.

---

# 10. Indexation

Par défaut, conserver `noindex, follow`.

Conditions cumulatives avant une future indexation :

1. `_validate_brands.py` sans blocker ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 11. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quotas de mots ;
- quotas de headings ;
- quotas de liens ;
- score artificiel de qualité ;
- template fixe par marque ;
- obligation automatique d'un tableau, d'une FAQ, d'un bloc « forces » ou « à éviter » ;
- deuxième copie des règles génériques déjà couvertes par le workflow de récupération.

Sa valeur est l'orchestration, la décision et le contrôle inter-pages propre au cluster marques.