# Cluster audit — Guides — 2026-09-11

Snapshot audité : `5b7c51375af68050328342f7fc25336a817a0099`

Mode : `guide-analysis-workflow / CLUSTER_AUDIT`

Portée : les 11 URLs sous `/guides/` déclarées dans `guide-workflow.config.yaml`.

Ce document enregistre des décisions d'audit uniquement. Il ne constitue ni un `PUBLISH_REVIEW`, ni une validation humaine, ni une autorisation d'indexation. Toutes les pages restent `noindex, follow`.

## Synthèse

Verdicts :

- `KEEP` : 1
- `LIGHT_UPDATE` : 9
- `DEEP_REWRITE` : 1
- `MERGE` : 0
- `NOINDEX` : 0

Le cluster a une vraie valeur éditoriale : aucune page n'est un simple placeholder ou une liste de mots-clés. Les frontières Guide / Usage / Comparatif sont globalement récupérables sans fusion. Le principal problème n'est pas la profondeur brute, mais l'héritage d'une production trop uniforme et une dette de génération qui pousse des sections en fonction d'un seuil de longueur.

## Findings transversaux

### 1. Le mécanisme `_guide_quality_supplements.py` est incompatible avec le nouveau contrat

Le script indique explicitement que ses suppléments sont ajoutés aux pages qui restent sous 900 mots. Le nouveau workflow interdit les quotas de mots comme proxy de qualité.

Décision : ne pas supprimer le contenu utile déjà présent pendant cet audit, mais retirer ce mécanisme lors du rollout. Une section supplémentaire ne doit exister que si l'intention, la preuve ou la décision du lecteur la justifie.

### 2. Les suppléments créent un défaut de sommaire

Les H2 injectés après `_generate_guides.py` ne sont pas intégrés au TOC généré avant eux. Exemples observés : `rentabilite`, `checklist-compatibilite`, `comparaison-exemple`, `exemple-conversion`, `diagnostic-debit`, `dimensionnement-exemple`, `achat-hepa`, `strategie-consommables`, `planning`.

Décision : lors de chaque update, intégrer toute section retenue dans la source éditoriale canonique et générer le TOC depuis la structure finale. Ne pas conserver un patch post-génération qui modifie le plan sans modifier le sommaire.

### 3. Trio fortement chevauchant : puissance / dépression / débit

Les trois URLs ont une intention distincte mais répètent actuellement une part importante du même raisonnement : watts != aspiration, débit + dépression doivent être lus ensemble, point de mesure, pertes de charge, filtre et flexible.

Décision : ne pas merger. Conserver trois tâches différentes :

- `puissance-aspiration` = ce que les watts permettent et ne permettent pas de conclure ;
- `depression-kpa-mbar-air-watt` = unités, conversion et interprétation de la pression / Air Watts ;
- `debit-air-aspirateur` = volume d'air, captage, point de mesure et diagnostic de perte de débit.

La page `puissance-aspiration` doit être la plus fortement reconstruite pour ne plus devenir un résumé des deux autres.

### 4. Paire proche mais légitime : L/M/H / HEPA

Les deux pages partagent volontairement la distinction `HEPA != classe H`, mais les jobs restent différents :

- `classes-l-m-h` = classification de l'appareil, risque, prévention et choix de classe ;
- `filtre-hepa-aspirateur` = classification du média filtrant, H13/H14, limites du marquage HEPA et vérification avant achat.

Décision : ne pas merger. La page L/M/H est le parent conceptuel ; HEPA doit éviter de réexpliquer longuement toute la classification machine.

### 5. Sources trop souvent réutilisées à l'identique

Plusieurs guides reposent sur le même petit noyau : IEC 60335-2-69, Bosch GAS 35 M AFC, INRS bois/silice/amiante, parfois MANN+HUMMEL. Ces sources sont utiles, mais une source exemple ne doit pas devenir la preuve par défaut de sujets différents.

Décision : pendant les updates, associer les sources au claim exact. Pour les procédures et compatibilités, privilégier la documentation de la fonction ou du modèle concerné ; pour les risques, les sources normatives / prévention ; pour les mesures physiques stables, une source technique adaptée.

### 6. Le shell visuel commun est acceptable ; le plan éditorial uniforme l'est moins

Answer box, sidebar, affiliation, sources et related links peuvent rester communs. En revanche, la cadence presque systématique `définition -> fonctionnement -> usage -> limites -> comment choisir -> supplément -> sources` doit disparaître là où elle ne suit pas la tâche réelle.

## Verdicts par URL

### `/guides/classes-l-m-h/` — KEEP

Type dominant : `HYBRID` (EXPLAINER + CHOICE)

Confiance : élevée.

Valeur à préserver :

- distinction machine complète vs filtre ;
- tableau L/M/H avec garde-fous ;
- frontière claire avec HEPA ;
- prudence sur matériau, VLEP, silice et amiante ;
- nuance issue de la communication INRS 2026 ;
- liens vers usages et comparatif classe M sans transformer le guide en classement.

Pourquoi KEEP : c'est la page la plus aboutie du cluster et elle a déjà bénéficié d'un pilote spécifique. Sa structure est propre à la question et son TOC est synchronisé.

Blockers : aucun blocker de cluster identifié. Un `PUBLISH_REVIEW` complet et un record de run restent requis avant tout READY.

### `/guides/comment-choisir-aspirateur-de-chantier/` — LIGHT_UPDATE

Type dominant : `CHOICE`.

Confiance : élevée.

Valeur à préserver : hiérarchie risque -> captage -> débit/dépression -> filtre -> connexion outil -> capacité/mobilité.

Corrections :

- rendre la page encore plus clairement orientée décision plutôt que mini-résumé de chaque guide technique ;
- remplacer une partie des explications détaillées par des règles de routing vers les guides spécialisés ;
- mieux distinguer ce qui élimine un appareil de ce qui constitue un compromis ;
- préserver la frontière avec le comparatif général : ici on définit le cahier des charges, le comparatif choisit entre modèles.

### `/guides/decolmatage-automatique/` — LIGHT_UPDATE

Type dominant : `HYBRID` (EXPLAINER + CHOICE).

Confiance : élevée.

Valeur à préserver : relation colmatage -> résistance -> baisse du débit, distinction automatique / semi-automatique / manuel, rôle en poussières fines.

Corrections :

- intégrer la section `rentabilite` dans la source canonique seulement si elle reste justifiée, avec TOC correspondant ;
- mieux documenter les différences de mécanisme entre systèmes au lieu d'utiliser un seul exemple Bosch comme illustration dominante ;
- distinguer clairement comportement documenté, promesse constructeur et comportement réel qui demanderait des essais comparables ;
- éviter toute généralisation de la cadence ou de l'efficacité d'un système à partir de son nom commercial.

### `/guides/prise-asservie/` — LIGHT_UPDATE

Type dominant : `HYBRID` (EXPLAINER + CHOICE).

Confiance : élevée.

Valeur à préserver : distinction outil filaire / outil batterie, limite de puissance spécifique au modèle, importance du raccord.

Corrections :

- intégrer `checklist-compatibilite` dans le plan réel et le TOC ;
- appuyer les points électriques / déclenchement sur des notices exactes plutôt que sur une source générique ;
- séparer nettement prise asservie, télécommande, Bluetooth et Wireless Tool Control ;
- conserver la règle : aucune puissance maximale « standard » inventée.

### `/guides/puissance-aspiration/` — DEEP_REWRITE

Type dominant : `EXPLAINER`.

Confiance : élevée.

Valeur à préserver : message central `watts moteur != puissance d'aspiration`, importance du contexte de mesure, exemple de comparaison.

Pourquoi DEEP_REWRITE : la page actuelle absorbe trop du rôle des guides `dépression` et `débit`. Une large part des H2 réexplique ces deux métriques au lieu de répondre à la question propre : « que signifie réellement la puissance annoncée et comment éviter de mal l'utiliser ? ».

Reconstruction recommandée :

- partir des différents usages du mot « puissance » dans les fiches ;
- séparer puissance absorbée, données turbine et performance aéraulique ;
- montrer ce qu'un chiffre en W permet réellement de conclure ;
- montrer les erreurs de comparaison ;
- renvoyer rapidement aux guides débit/dépression au lieu de les dupliquer ;
- conserver un protocole de lecture de fiche, sans ranking de produits.

### `/guides/depression-kpa-mbar-air-watt/` — LIGHT_UPDATE

Type dominant : `EXPLAINER`.

Confiance : élevée.

Valeur à préserver : conversions kPa/mbar/mmH2O, limites des Air Watts, point de mesure, exemple 25 kPa / 250 mbar.

Corrections :

- recentrer la page sur pression, unités et interprétation ;
- raccourcir les passages qui rejouent le guide débit ;
- intégrer l'exemple de conversion dans le plan/TOC final ;
- conserver l'interdiction de conclure à la performance réelle après une simple conversion d'unités.

### `/guides/debit-air-aspirateur/` — LIGHT_UPDATE

Type dominant : `EXPLAINER`.

Confiance : élevée.

Valeur à préserver : L/s <-> m3/h, captage à la source, turbine vs raccord, colmatage, diagnostic pratique.

Corrections :

- intégrer `diagnostic-debit` dans le plan et le TOC ;
- réduire le recouvrement avec `puissance` et `dépression` ;
- maintenir le refus d'un seuil universel de débit ;
- distinguer explicitement valeur constructeur et performance avec flexible/outil/filtre chargé.

### `/guides/capacite-cuve/` — LIGHT_UPDATE

Type dominant : `CHOICE`.

Confiance : élevée.

Valeur à préserver : brut vs net vs eau, mobilité, poids une fois chargé, dimensionnement par fréquence de vidage.

Corrections :

- intégrer `dimensionnement-exemple` au plan et au TOC ;
- conserver Bosch comme exemple, pas comme preuve universelle ;
- faire de la capacité un arbitrage logistique et non un proxy de gamme ou de puissance.

### `/guides/filtre-hepa-aspirateur/` — LIGHT_UPDATE

Type dominant : `EXPLAINER`.

Confiance : élevée.

Valeur à préserver : H13/H14 à la MPPS, pénétration 10x différente, HEPA != classe H, cas amiante, système complet.

Corrections :

- intégrer `achat-hepa` dans le plan et le TOC ;
- éviter de refaire le guide L/M/H au-delà de ce qui est nécessaire pour la distinction ;
- garder le focus sur le média filtrant, l'étanchéité, la compatibilité et la documentation de la référence vendue.

### `/guides/sac-ou-sans-sac/` — LIGHT_UPDATE

Type dominant : `CHOICE`.

Confiance : élevée.

Valeur à préserver : collecte, remise en suspension, protection du filtre, coût total, cas liquide et poussières dangereuses.

Corrections :

- intégrer `strategie-consommables` dans le plan/TOC ;
- rendre explicite la frontière avec `/comparatifs/aspirateur-chantier-sans-sac/` : le guide arbitre un mode de collecte, le comparatif sélectionne éventuellement des machines ;
- ne jamais recommander la suppression d'un sac ou d'un dispositif de collecte faisant partie d'une configuration certifiée.

### `/guides/entretien-aspirateur-chantier/` — LIGHT_UPDATE

Type dominant : `HOW_TO`.

Confiance : élevée.

Valeur à préserver : contrôle filtre/sac/flexible/joints, eau, surchauffe, prudence poussières dangereuses, absence de calendrier universel.

Corrections :

- intégrer `planning` dans le plan et le TOC ;
- distinguer clairement les gestes génériques sûrs des opérations qui doivent suivre la notice d'un modèle ;
- éviter de faire d'une procédure générique une instruction de maintenance sur machine classée ;
- renforcer le critère de vérification du résultat : retour du débit, absence d'obstruction, intégrité du filtre/joints, selon la notice.

## Hub `/guides/`

Le hub n'entre pas dans les 11 verdicts ci-dessus, mais nécessite une correction éditoriale lors du rollout : la phrase « questions que posent les vrais utilisateurs aux moteurs de recherche et aux assistants IA » n'apporte pas de valeur au lecteur et formule une affirmation non nécessaire. Le hub devrait plutôt organiser les guides par décision : sécurité / performance / connexion outil / collecte-maintenance.

## Ordre de rollout recommandé

1. `puissance-aspiration` — DEEP_REWRITE ; clarifie ensuite les frontières du trio métriques.
2. `depression-kpa-mbar-air-watt` — LIGHT_UPDATE.
3. `debit-air-aspirateur` — LIGHT_UPDATE.
4. `decolmatage-automatique` — LIGHT_UPDATE.
5. `prise-asservie` — LIGHT_UPDATE.
6. `sac-ou-sans-sac` — LIGHT_UPDATE.
7. `entretien-aspirateur-chantier` — LIGHT_UPDATE.
8. `capacite-cuve` — LIGHT_UPDATE.
9. `filtre-hepa-aspirateur` — LIGHT_UPDATE.
10. `comment-choisir-aspirateur-de-chantier` — LIGHT_UPDATE final pour router vers les guides stabilisés.
11. `classes-l-m-h` — KEEP ; PUBLISH_REVIEW uniquement sauf nouveau fait à corriger.

## Dette de génération à traiter pendant le rollout

- retirer la logique de seuil `< 900 mots` de `_guide_quality_supplements.py` ;
- déplacer les suppléments réellement utiles dans la source éditoriale de la page ;
- produire le TOC à partir de la structure finale ;
- éviter d'empiler `_generate_guides.py` + patch de longueur + normalisation comme substitut à une architecture éditoriale propre ;
- conserver `_generate_guides.py` comme source canonique tant que le rollout n'introduit pas une source par page justifiée ;
- ne créer un record `.content/guides/<slug>.json` qu'au moment du vrai AUDIT / content workflow de cette URL ;
- ne jamais attribuer `READY_FOR_HUMAN_VALIDATION` depuis ce cluster audit.

## Conclusion

Aucune fusion ni suppression n'est recommandée à ce stade. Les 11 intents sont défendables. Le cluster doit surtout être désindustrialisé : un DEEP_REWRITE ciblé sur `puissance-aspiration`, neuf mises à jour légères et un KEEP pour `classes-l-m-h`.
