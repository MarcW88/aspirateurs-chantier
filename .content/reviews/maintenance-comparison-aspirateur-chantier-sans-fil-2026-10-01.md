# AUDIT — /comparatifs/aspirateur-chantier-sans-fil/ — 2026-10-01

- Décision : `KEEP` (confiance haute).
- Intention : choisir un système sans fil selon classe, plateforme, autonomie et coût de configuration.
- Valeur à préserver : classe avant voltage ; batteries/chargeur inclus dans le coût ; poids sans batterie distingué ; autonomies fabricants non converties en score ; déclenchement distinct d'une prise asservie.
- Preuves revérifiées le 1er octobre 2026 : Bosch GAS 18V-10 L (classe L, 4 min/Ah, 4,7 kg, 10/6 L) https://www.bosch-professional.com/om/en/products/gas-18v-10-l-06019C6302 ; Bosch GAS 18V-12 MC ; DeWalt DCV586M ; Kärcher WD 3-18 S sur leurs fiches officielles liées depuis la page.
- Sécurité : DCV586M et GAS 18V-12 MC restent classe M documentée ; WD 3-18 S n'est pas présenté comme alternative de sécurité. Aucune autonomie vécue inventée.
- UNKNOWN : autonomie réelle, prix et inclusion exacte du GCT 30-42 selon variante ; la page demande explicitement de vérifier la variante.
- Cannibalisation : rôle propre face à la page DeWalt, au comparatif professionnel et aux modèles.
- Blockers : aucun. Pas de test d'autonomie propriétaire ni GSC.
- QA : run-evidence existant valide ; `validate_comparison_skill_stack.py`, `validate_comparison_run_evidence.py --slug aspirateur-chantier-sans-fil --require-run` et `_validate_comparatifs.py` passent.
- Action : aucune modification éditoriale.

