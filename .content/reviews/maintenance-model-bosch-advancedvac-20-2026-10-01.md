# AUDIT — /modeles/bosch-advancedvac-20/ — 2026-10-01

- Décision : `KEEP` en `audit_only` (confiance haute).
- Intention : décider si l'AdvancedVac 20 suffit ou si la classe L du GAS 12-25 PL change le besoin.
- Valeur à préserver : prise outil déjà présente sur le DIY ; chiffres turbine contextualisés ; absence de classe L/M/H explicitement visible ; tableau limité au vrai arbitrage.
- Preuves revérifiées le 1er octobre 2026 : fiches Bosch AdvancedVac 20 et GAS 12-25 PL. https://www.bosch-diy.com/be/fr/p/advancedvac-20-06033d1200 ; https://www.bosch-professional.com/be/fr/products/gas12-25-12-25ps-060197C100
- Sécurité : flexible antistatique, débit et puissance ne sont pas utilisés pour déduire une classe. Le GAS est présenté classe L uniquement d'après sa documentation.
- UNKNOWN : disponibilité des variantes, prix, comportement réel en colmatage et compatibilités d'accessoires non documentées sur la page.
- Blockers : aucun besoin de correction identifié. Tests physiques et mesures comparables absents.
- Validation : `validate_model_skill_stack.py` et `validate_model_run_evidence.py --slug bosch-advancedvac-20 --require-run` passent.
- Handoff : aucune modification automatique ; page et `_generate_model_overrides.py` restent inchangés conformément à la phase 1. Toute future correction modèle exige une tâche humaine séparée.

