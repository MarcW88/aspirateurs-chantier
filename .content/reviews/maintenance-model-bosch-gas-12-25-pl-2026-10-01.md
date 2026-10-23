# AUDIT — /modeles/bosch-gas-12-25-pl/ — 2026-10-01

- Décision : `KEEP` en `audit_only` (confiance haute).
- Intention : arbitrer GAS 12-25 PL contre GAS 35 L AFC sans confondre prise outil, classe et décolmatage.
- Valeur à préserver : SFC semi-automatique distinct d'AFC ; 25 L brut/21 L net/15 L eau ; chiffres turbine contextualisés ; rôle autonome fondé sur compacité et classe L.
- Preuves revérifiées le 1er octobre 2026 : https://www.bosch-professional.com/be/fr/products/gas12-25-12-25ps-060197C100 ; https://www.bosch-professional.com/be/fr/products/gas-35-l-afc-06019C32W0 ; https://www.bosch-diy.com/be/fr/p/advancedvac-20-06033d1200
- Sécurité : classe L explicitement documentée, jamais déduite de SFC, débit ou gamme Professional.
- UNKNOWN : disponibilité et prix de chaque variante, comportement réel en poussière fine, gains pratiques AFC sans test. La page ne les transforme pas en certitudes.
- Blockers : aucun besoin de correction identifié ; pas de test physique.
- Validation : `validate_model_skill_stack.py` et `validate_model_run_evidence.py --slug bosch-gas-12-25-pl --require-run` passent.
- Handoff : aucune modification automatique ; page et `_generate_model_overrides.py` restent inchangés. Toute évolution modèle nécessite une décision humaine et une tâche renderer séparée.

