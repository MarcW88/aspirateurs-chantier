# AUDIT — /marques/bosch/ — 2026-10-01

- Décision : `KEEP` (confiance haute).
- Intention : comprendre les gammes et écosystèmes Bosch avant de choisir une référence.
- Valeur à préserver : séparation Home & Garden / Professional filaire / Professional 18 V ; POWER FOR ALL distinct de Professional 18V/AMPShare ; comparaison 35 M/55 M par volume plutôt que faux gain de puissance ; filtre HEPA distinct de la classe machine.
- Preuves revérifiées le 1er octobre 2026 sur les fiches Bosch actuelles et pages plateformes. Le GAS 18V-10 L reste documenté à 4,7 kg sans batterie, 34 l/s, 115 mbar, 10/6 L et classe L : https://www.bosch-professional.com/om/en/products/gas-18v-10-l-06019C6302 ; GAS 35 M AFC : https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0
- Sécurité : pas d'inférence de classe depuis HEPA, débit ou couleur de gamme ; la classe doit suivre le risque. Aucune équivalence ATEX/ACD publiée.
- UNKNOWN : disponibilité par variante et prix du jour ; performances réelles filtre chargé ; autonomie réelle du sans-fil. Non utilisés comme certitudes.
- Distinctivité : la page organise une gamme et les parcs batteries ; elle ne remplace ni les pages modèles ni les comparatifs.
- Blockers : aucun ; pas de test physique ni GSC.
- QA : run-evidence existant valide ; `validate_brand_skill_stack.py`, `validate_brand_run_evidence.py --slug bosch --require-run` et `_validate_brands.py` passent.
- Action : aucune modification éditoriale.

