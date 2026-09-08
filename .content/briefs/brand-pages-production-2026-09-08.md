# Brief consolidé — Pages marques — 08/09/2026

## Scope

Pages `BRAND_HUB` : Kärcher, Bosch, Makita, Festool, DeWalt, Parkside, Nilfisk et Mirka.

## Intention

Chaque page doit répondre à une décision de marque : comprendre la gamme actuelle, identifier l'écosystème, savoir dans quels usages la marque est forte, connaître ses limites et rejoindre les bons modèles/comparatifs/guides. Une page marque ne doit pas devenir une histoire corporate ni une liste de produits sans contexte.

## Règles communes

- Entity Map avant rédaction.
- Gamme actuelle avant recommandation ; anciennes générations explicitement marquées.
- Sources primaires fabricants privilégiées.
- Aucune prétention de test physique ; desk research explicite.
- Les classes L/M/H ne sont jamais déduites d'un filtre HEPA, d'une puissance ou d'un débit.
- Les systèmes batterie et accessoires sont décrits au niveau de compatibilité réellement documenté.
- Au moins 7 H2, 3 sources, 6 liens internes et 5 cibles uniques ; le projet applique un gate plus strict de 9 H2, 1 100 mots, 8 liens et 7 cibles.
- `noindex, follow` conservé jusqu'à instruction séparée.

## Angles par marque

### Kärcher
Séparer Home & Garden WD et Professional NT. Mettre en avant Tact, classes M/H et ACD sans transformer ACD en promesse ATEX universelle. Traiter les anciennes variantes WD comme précédentes générations lorsque pertinent.

### Bosch
Séparer Bosch DIY et Bosch Professional. Expliquer Click & Clean, L-BOXX et la différence entre Power for All 18 V et Professional 18 V. AdvancedVac ≠ GAS classe M.

### Makita
Montrer la profondeur filaire + LXT/XGT. Expliquer Makpac/AWS et la complexité des suffixes. Vérifier VC4210 L/M au niveau de la référence exacte ; ne pas déduire la classe du nom abrégé.

### Festool
Positionner la marque comme système de travail : CLEANTEC, Systainer/T-LOC, Bluetooth, App et AUTOCLEAN. Distinguer CTL (L), CTM (M), CTH (H) et les solutions sans fil CTC/CTMC.

### DeWalt
Corriger l'ancien cadrage “DXV”. Le cœur actuel est XR/FLEXVOLT, DCV586M, DCV584L, TSTAK, AIRLOCK et Perform & Protect. Distinguer clairement classe L et M.

### Parkside
Traiter la gamme PWD actuelle, pas PNTS comme ligne principale. La disponibilité Lidl et les révisions de modèles font partie de l'information. Ne jamais confondre Airwatts / watts et classe de poussière.

### Nilfisk
Séparer Buddy/Multi (eau/poussière grand public) et ATTIX (professionnel). Mettre en avant InfiniClean et FlowSensor sur les variantes concernées.

### Mirka
Positionnement sanding-first. Mettre en avant DEXOS 1217/1230 M AFC, myMirka et l'intégration DEROS/DEOS. Anciennes DE 1230/1242 = legacy / génération précédente selon contexte.

## Handoff

Source éditoriale : `_generate_brands.py`.
Données persistantes : `.content/brands/<slug>.yaml`.
QA repo : `_validate_brands.py` + validator du skill.
