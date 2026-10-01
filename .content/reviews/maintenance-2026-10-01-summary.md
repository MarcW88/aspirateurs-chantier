# Maintenance éditoriale — 1er octobre 2026

## Périmètre et exécution

- Base : `main` au commit `b11401c1e78ec1da7d90238fc1b903b48cca4933`, récupérée dans un checkout neuf.
- Préparation : `python scripts/maintenance_orchestrator.py prepare --max-pages 10` — 48 pages inventoriées, 10 sélectionnées.
- PR de maintenance ouverte avant le run : aucune.
- Les cinq analysis-workflows et les skills spécialisés appelés ont été lus et appliqués en mode AUDIT.
- Les dix audits ont été enregistrés avec `record` avant toute éventuelle correction. Comme toutes les décisions sont KEEP, aucun content-workflow et aucun PUBLISH_REVIEW post-correction ne sont requis.

## Décisions

| URL | Type | Décision | Motif principal |
|---|---|---|---|
| `/comparatifs/aspirateur-chantier-puissant/` | comparaison | KEEP | Les mesures restent contextualisées ; aucun faux classement cross-brand ni claim de sécurité. |
| `/guides/capacite-cuve/` | guide | KEEP | Brut/net/eau correctement séparés et exemple Bosch actuel. |
| `/marques/bosch/` | marque | KEEP | Gammes et plateformes batteries distinctes ; classes explicitement sourcées. |
| `/modeles/bosch-advancedvac-20/` | modèle audit_only | KEEP | Rôle clair face au GAS 12-25 PL ; aucune classe déduite. |
| `/usages/aspirateur-atelier/` | usage | KEEP | Job autonome fondé sur les postes et le captage, sans podium produit. |
| `/comparatifs/aspirateur-chantier-sans-fil/` | comparaison | KEEP | Classe et parc batterie avant voltage ; autonomie non normalisée. |
| `/guides/classes-l-m-h/` | guide | KEEP | Classe appareil, filtre HEPA, amiante et silice traités avec les limites requises. |
| `/marques/dewalt/` | marque | KEEP | DCV586M M et DCV584L L distingués ; coût système et variantes qualifiés. |
| `/modeles/bosch-gas-12-25-pl/` | modèle audit_only | KEEP | SFC/AFC et capacités brute/net/eau correctement distingués. |
| `/usages/aspirateur-bois-sciure-copeaux/` | usage | KEEP | Poussière fine/copeaux et mobile/fixe séparés ; captage à la source correctement priorisé. |

## Vérifications factuelles

Consultation le 1er octobre 2026 des sources officielles Bosch, DeWalt, Kärcher, Makita, IEC, INRS et HSE indiquées dans chaque audit. Les identités, variantes, plateformes, classes L/M, capacités et mesures publiées utilisées dans ces dix pages restent cohérentes avec ces sources. Les pages ne déduisent pas une classe depuis HEPA, puissance, débit ou décolmatage ; ACD n'est pas assimilé à ATEX/Zone 22 ; wet/dry n'est pas présenté comme une aptitude aux poussières dangereuses. Le guide classes conserve un langage prudent sur l'amiante et la silice et ne remplace pas l'évaluation des risques.

Unknowns conservés : prix/disponibilité et contenu exact de certaines variantes, autonomie réelle, comportement filtre chargé, dimensionnement d'un réseau d'atelier, classe requise pour une situation concrète. Aucun de ces éléments n'a été inventé ou publié comme certitude. Aucun test physique ou mesure propriétaire n'a été effectué.

## Fichiers et publication

Modifications de la branche : dix rapports `.content/reviews/`, ce résumé, `.content/maintenance/index.json` et l'historique daté. Aucun HTML, registre éditorial authored, run-evidence v2, canonical, robots, URL, redirection ou source de génération n'a été modifié. Les pages `/modeles/` et `_generate_model_overrides.py` sont inchangés.

Il n'y a donc aucun changement de contenu proposé mais non publié. Les seuls artefacts à fusionner sont les audits et leur historique, afin que la rotation mensuelle ne sélectionne pas de nouveau ces pages avant leur prochaine échéance.

## Validations

PASS : `validate_guide_workflow.py`, `validate_guide_quality.py`, `validate_usage_workflow.py`, `validate_brand_skill_stack.py`, `validate_comparison_skill_stack.py`, `validate_model_skill_stack.py`, `_validate_brands.py`, `_validate_comparatifs.py`, `validate_product_cards.py all`, `validate_inline_affiliate_links.py`, les run-evidence existants des deux comparatifs, des deux marques et des deux modèles avec `--require-run`, ainsi que `git diff --check`.

Limite : `_validate_comparatifs.py` émet un warning global de détection textuelle « no explicit desk-research disclosure » sur plusieurs comparatifs, dont `/comparatifs/aspirateur-chantier-puissant/`, alors que la page contient explicitement « Recherche documentaire ; aucune mesure propriétaire ni test physique ». Ce warning n'est pas masqué, mais ne constitue pas un échec du validateur. Aucun rendu visuel navigateur n'a été réalisé, car aucun HTML ni design n'a changé.

## Action humaine attendue

Examiner puis fusionner la PR pour persister les dix audits, le registre et l'historique. Aucun déploiement éditorial, changement d'indexation ou action structurelle n'est demandé.
