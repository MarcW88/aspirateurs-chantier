# AUDIT — /marques/dewalt/ — 2026-10-01

- Décision : `KEEP` (confiance haute).
- Intention : comprendre l'écosystème DeWalt extraction/batterie/raccord/rangement.
- Valeur à préserver : DCV586M classe M sans fil distinct du DCV584L hybride classe L ; FLEXVOLT, AIRLOCK et TSTAK reliés à des frictions réelles ; coût machine nue qualifié.
- Preuves revérifiées le 1er octobre 2026 : https://www.dewalt.fr/fr-fr/produit/dcv586mn-xj/aspirateur-tstak-xr-flexvolt-54v-brushless-eau-et-poussieres-classe-m ; https://www.dewalt.fr/fr-fr/produit/dcv584l-qw/aspirateur-sur-secteur-ou-batterie-xr-et-xr-flexvolt-1854v-classe-l-sans ; https://prod.dewalt.fr/fr-fr/solutions-chantier/perform-protect
- Sécurité : filtre HEPA du DCV584L ne devient pas classe M ; classe avant plateforme batterie ; aucune équivalence AIRLOCK/certification.
- UNKNOWN : disponibilité et contenu exact des variantes, prix du système, autonomie réelle et comportement de filtration. Non affirmés.
- Distinctivité : architecture fondée sur l'écosystème sans fil, nettement différente de Bosch et des gammes filaires larges.
- Blockers : aucun ; pas de test physique ni GSC.
- QA : run-evidence existant valide ; `validate_brand_skill_stack.py`, `validate_brand_run_evidence.py --slug dewalt --require-run` et `_validate_brands.py` passent.
- Action : aucune modification éditoriale.

