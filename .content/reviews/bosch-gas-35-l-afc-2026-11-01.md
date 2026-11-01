# AUDIT — /modeles/bosch-gas-35-l-afc/

- Date : 2026-11-01
- Workflow : model-analysis-workflow, mode AUDIT ; gouvernance phase 1 audit_only.
- Décision : KEEP (confiance élevée)
- Valeur à préserver : positionnement clair entre SFC et AFC, classe L vs M et distinction capacité brute/nette/eau.
- Preuves : Bosch confirme 1 200 W nominal, 12,2 kg, 35/23/19,2 l, classe L, 6 150 cm², 74 l/s et 254 mbar à la turbine, avec AFC.
- Source : https://www.bosch-professional.com/fr/fr/products/gas-35-l-afc-06019C32W0 (consultée le 2026-11-01).
- Sécurité : la classe L est sourcée sur la référence exacte et n'est pas assimilée au GAS 35 M ; aucune promesse amiante/ATEX.
- Unknowns : adéquation à une poussière réelle dépend de l'évaluation du risque ; disponibilité commerciale non auditée.
- Blockers : aucun pour l'audit. Toute future correction resterait soumise à décision humaine tant que la phase 1 est active.
- Handoff : aucune correction proposée ; ne pas modifier la page ni `_generate_model_overrides.py`.
