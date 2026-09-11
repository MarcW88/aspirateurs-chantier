# CLUSTER_AUDIT v2 — `/comparatifs/`

Date : 2026-09-11  
Scope : 9 URLs `/comparatifs/` sur `main`  
Workflow : `comparison-analysis-workflow / CLUSTER_AUDIT` — contrat evidence-led v2  
Gouvernance : >=80 % shared / <=20 % custom  
Résultat : **FAIL — REQUIRES_WORKFLOW_RERUN — KEEP_NOINDEX**

> Cet audit remplace le verdict éditorial du post-rollout du 09/09/2026. Le rapport du 09/09 reste conservé comme historique, mais son `READY_FOR_HUMAN_VALIDATION` n'est plus suffisant sous le contrat v2.

## 1. Conclusion exécutive

Le rollout du 09/09 a corrigé plusieurs défauts importants : les 9 URLs ont désormais des rôles plus distincts, le scoring universel a disparu, le périmètre industriel a été redéfini, les pages classe M / sans fil / wet-dry couvrent mieux les candidats évidents et les pages conservent des garde-fous utiles contre les fausses équivalences.

Mais le cluster n'est pas encore au niveau éditorial attendu pour publication.

Le principal problème n'est plus un clonage exact de H2. Il est devenu **fonctionnel** : une majorité de pages suit encore la cadence suivante, avec de petites variations de vocabulaire :

1. answer box ;
2. `comparison-decision-module` ;
3. tableau de 4 ou 5 profils / références ;
4. trois à cinq H2 courts expliquant les critères ;
5. sources fabricants.

Cette cadence donne des pages propres mais trop souvent minces, prévisibles et interchangeables dans leur façon de raisonner. Le générateur a donc réussi à casser le vieux template de ranking sans encore produire partout la profondeur attendue d'un vrai workflow `seo-keyword → JTBD → evidence-based-reviews → affiliate-value → brief → content-and-copy → fact-check → humanizer → QA`.

Autre blocker majeur : **aucune des 9 pages ne possède encore de run-evidence v2**. Le dossier `.content/comparisons/runs/` ne contient que son README de contrat. Par conséquent, aucune page ne peut prétendre avoir réellement exécuté la chaîne partagée et toutes doivent rester `REQUIRES_WORKFLOW_RERUN` + `noindex, follow`.

Enfin, une frontière de cluster doit être corrigée avant rollout : `/comparatifs/aspirateur-chantier-sans-sac/` et `/guides/sac-ou-sans-sac/` servent actuellement pratiquement la même décision. Le guide est plus approfondi sur le rôle du sac, poussières fines, classes M/H, coût réel et stratégie consommables. Maintenir deux URLs aussi proches crée une cannibalisation éditoriale inutile.

---

# 2. Ce qu'il faut préserver

Le nouveau passage ne doit pas jeter les améliorations déjà présentes.

## A. Rôles d'URL désormais plus propres

- `meilleur-aspirateur-de-chantier` = orientation générale / triage vers le bon type d'appareil ;
- `aspirateur-professionnel` = workflow professionnel L/M, filaire/sans fil, outil et mobilité ;
- `aspirateur-classe-m` = M comme gate avant les autres arbitrages ;
- `aspirateur-industriel` = process industriel, continu, poussières, huiles et copeaux ;
- `aspirateur-chantier-puissant` = lecture débit/dépression et puissance réellement utile ;
- `aspirateur-chantier-sans-fil` = plateforme batterie, classe, runtime et déclenchement ;
- `aspirateur-eau-poussiere` = usage humide/sec et gestion du liquide ;
- `petit-aspirateur-de-chantier` = mobilité/encombrement plutôt qu'un seuil arbitraire de litres.

## B. Bons garde-fous déjà présents

À conserver :

- pas de gagnant universel artificiel ;
- pas de score 100 points obligatoire ;
- classe M ≠ puissance / HEPA ;
- wet & dry ≠ certification poussières dangereuses ;
- débit/dépression non comparés aveuglément quand le point de mesure diffère ;
- pas de faux test physique ;
- affiliation explicitement exclue du ranking ;
- limites visibles pour les recommandations.

## C. `/aspirateur-professionnel/` reste la meilleure base éditoriale du cluster

La page va plus loin que les autres : elle distingue professionnel et classe M, développe plusieurs arbitrages en H3, traite chaque référence avec ses limites et explique davantage le workflow outil. Elle ne doit cependant plus rester `KEEP` par héritage : elle doit elle aussi passer le contrat v2 et revalider ses preuves avant de retrouver un PASS.

---

# 3. Blockers cluster-level

## Blocker 1 — aucune preuve d'exécution v2

Aucun `.content/comparisons/runs/<slug>.json` n'existe encore.

Conséquence :

- impossible de prouver que `seo-keyword`, `jobs-to-be-done`, `evidence-based-reviews`, `affiliate-value`, `content-brief-authoring`, `content-and-copy`, `humanizer`, `anti-ai-slop`, `editorial-qa`, etc. ont réellement produit la page ;
- l'existence des skills dans le repo n'est plus considérée comme une preuve d'exécution ;
- les anciens PASS du 09/09 ne sont plus recevables.

Décision : **workflow rerun obligatoire pour les 9 URLs**.

## Blocker 2 — cadence éditoriale fonctionnellement clonée

Les H2 sont différents, mais plusieurs pages réutilisent la même architecture abstraite :

`réponse immédiate → 3/4 repères → tableau profils/références → explication de 3/4 critères → sources`.

Ce pattern est particulièrement visible sur :

- général ;
- puissant ;
- classe M ;
- sans fil ;
- eau/poussière ;
- petit format ;
- dans une moindre mesure industriel.

Le problème n'est pas l'usage d'un tableau ou d'un composant partagé. Le problème est que le tableau devient trop souvent le cœur de l'analyse, tandis que les sections suivantes ne font qu'expliciter brièvement ses colonnes.

Décision : le nouveau brief doit être dérivé des questions et preuves de chaque intention. Le `comparison-decision-module` devient optionnel.

## Blocker 3 — evidence layer trop fabricant-led

Les pages actuelles reposent principalement sur des fiches fabricants. C'est suffisant pour :

- classe déclarée ;
- capacité ;
- poids ;
- débit/dépression publiés ;
- batterie ;
- fonctions documentées.

Ce n'est pas suffisant à lui seul pour :

- ergonomie réelle ;
- maintien des performances filtre chargé ;
- facilité de vidage ;
- qualité du raccord outil ;
- pertinence du format en escaliers/véhicule ;
- comparaison d'autonomie dans des conditions différentes ;
- exposition/qualité du vidage ;
- jugement de coût d'usage ;
- dimensionnement industriel.

Les nouvelles pages devront utiliser sources d'autorité, tests indépendants ou retours d'usage lorsque le claim l'exige, sans transformer chaque comparatif en revue Reddit.

## Blocker 4 — valeur ajoutée trop souvent limitée au tri de specs

Les tableaux sont plus intelligents qu'avant, mais la valeur originale doit aller plus loin :

- cas où un produit apparemment supérieur devient un mauvais choix ;
- incompatibilités / coûts de configuration ;
- critères dominants selon le chantier ;
- conséquences pratiques d'un choix de cuve, batterie ou décolmatage ;
- alternatives hors shortlist ;
- critères qu'on ne peut pas comparer honnêtement ;
- situations où l'utilisateur ne devrait pas acheter dans cette catégorie.

## Blocker 5 — cannibalisation `sans sac`

`/comparatifs/aspirateur-chantier-sans-sac/` explique déjà :

- conception réellement sans sac ;
- collecte directe en cuve ;
- poussières fines ;
- protection du filtre ;
- coût des consommables.

`/guides/sac-ou-sans-sac/` traite les mêmes questions avec davantage de profondeur, y compris classes M/H, stratégie de consommables, entretien et coût réel.

Il n'y a pas aujourd'hui deux jobs suffisamment distincts pour justifier les deux URLs.

Décision : **MERGE proposé**, sous validation humaine. Ne pas rediriger ni supprimer automatiquement pendant l'audit.

---

# 4. Décisions par URL

| URL | Décision | Confiance | Motif principal |
| --- | --- | ---: | --- |
| `/comparatifs/meilleur-aspirateur-de-chantier/` | **DEEP_REWRITE** | Haute | Bonne fonction umbrella, mais trop peu de profondeur après le tableau d'orientation ; valeur originale insuffisante pour une requête aussi large et transactionnelle. |
| `/comparatifs/aspirateur-professionnel/` | **LIGHT_UPDATE** | Haute | Meilleure page actuelle ; structure et arbitrages à préserver. Besoin surtout d'un vrai run v2, d'une revalidation des preuves et d'un enrichissement ciblé plutôt que d'une nouvelle architecture. |
| `/comparatifs/aspirateur-classe-m/` | **DEEP_REWRITE** | Très haute | Sujet de sécurité à forte valeur : fabricant-only insuffisant pour l'ensemble du raisonnement ; manque de profondeur sur collecte, alarmes/surveillance, décolmatage, workflow de décontamination et critères qui font basculer un M. |
| `/comparatifs/aspirateur-chantier-puissant/` | **DEEP_REWRITE** | Très haute | Bonne prudence sur les mesures, mais la page ressemble davantage à une mini-leçon métrique qu'à une comparaison réellement utile. Il faut une méthodologie de comparabilité plus riche et relier puissance utile aux scénarios réels. |
| `/comparatifs/aspirateur-industriel/` | **DEEP_REWRITE** | Haute | Périmètre produit enfin correct, mais le dimensionnement process/continu/poussières/liquides/copeaux/ACD-ATEX reste trop condensé pour une intention industrielle. |
| `/comparatifs/aspirateur-chantier-sans-fil/` | **DEEP_REWRITE** | Haute | Les quatre profils sont pertinents mais la décision batterie reste superficielle : configuration réelle, batteries nécessaires, runtime, recharge, poids en ordre de marche, parc existant et déclenchement outil doivent devenir le cœur de la page. |
| `/comparatifs/aspirateur-eau-poussiere/` | **LIGHT_UPDATE** | Moyenne-haute | Intention claire et shortlist raisonnable. La structure peut rester ; enrichir transitions sec/humide, capacité liquide utile, vidange, filtres/sacs et variantes réellement disponibles. |
| `/comparatifs/petit-aspirateur-de-chantier/` | **LIGHT_UPDATE** | Haute | Bonne correction du vieux seuil en litres. Il faut surtout enrichir dimensions/portage/rangement/poids prêt à travailler et revalider les preuves ; pas besoin de reconstruire le rôle de la page. |
| `/comparatifs/aspirateur-chantier-sans-sac/` | **MERGE** vers `/guides/sac-ou-sans-sac/` | Haute | Job utilisateur et substance trop proches ; le guide est déjà plus complet. Décision structurelle à valider humainement avant toute action technique. |

Aucune URL n'obtient `KEEP` aujourd'hui parce qu'aucune ne dispose encore du run-evidence v2 exigé par la nouvelle gouvernance.

---

# 5. Détail des priorités de réécriture

## 5.1 Classe M — priorité 1

Pourquoi d'abord :

- forte intention transactionnelle ;
- sécurité et conformité ;
- erreurs potentielles coûteuses ;
- nombreux arbitrages réellement différenciants.

Le nouveau workflow doit notamment distinguer :

- classe certifiée vs filtre ;
- alarme / surveillance de débit ;
- antistatique ;
- collecte/élimination ;
- décolmatage ;
- raccord outil ;
- capacité et mobilité ;
- filaire vs batterie ;
- coût réel de configuration ;
- contexte de poussière, sans prétendre prescrire une classe à la place de l'évaluation du risque.

## 5.2 Industriel — priorité 2

Le nouveau brief doit partir du process, pas du catalogue :

- matière aspirée ;
- charge / débit de matière ;
- intermittence vs continu ;
- monophasé/triphasé ;
- mobilité/stationnaire ;
- vidage et récupération ;
- poussières combustibles / zones ;
- filtration ;
- raccordement au process.

L'objectif n'est pas de créer un pseudo-sélecteur industriel universel mais de montrer quand chaque famille devient pertinente et quand une étude fabricant/intégrateur est nécessaire.

## 5.3 Puissant — priorité 3

Préserver la prudence actuelle, mais dépasser la simple opposition débit/dépression.

La page doit aider à choisir selon :

- gros débris / gravats ;
- poussière fine ;
- longueur/diamètre du flexible ;
- usage avec outil ;
- filtre propre vs chargé ;
- décolmatage ;
- mesures réellement comparables ou non.

Si aucune comparaison quantitative cross-brand honnête n'est possible, l'expliquer et recommander par scénarios plutôt que fabriquer un podium.

## 5.4 Général — priorité 4

Le général doit devenir le meilleur point d'entrée du cluster : un diagnostic de besoin qui évite de refaire neuf mini-comparatifs dans une seule page.

La valeur doit être :

- identifier le type de poussière/déchet ;
- déterminer si une classe est un gate ;
- définir mobilité/outil/eau ;
- estimer cadence/volume ;
- router vers le comparatif spécialisé ;
- proposer quelques références repères uniquement lorsque cela accélère réellement la décision.

## 5.5 Sans fil — priorité 5

L'écosystème batterie doit devenir une variable économique et opérationnelle, pas seulement une ligne de tableau :

- machine nue vs kit ;
- batterie(s) nécessaire(s) ;
- poids avec batterie ;
- autonomie documentée et protocole ;
- recharge/rotation ;
- compatibilité outil ;
- auto-start/télécommande ;
- classe L/M.

---

# 6. Pages LIGHT_UPDATE

## Professionnel

Préserver :

- frontière professionnel ≠ M ;
- six scénarios ;
- arbitrages en H3 ;
- limites par modèle.

À faire : revalider les références au 11/09/2026, enrichir uniquement les preuves qui soutiennent un jugement pratique, créer le run v2, puis PUBLISH_REVIEW.

## Eau/poussière

Préserver le rôle et la shortlist. Ajouter uniquement ce qui change le choix : capacité eau utile, vidange, gestion sac/filtre lors de la transition, arrêt flotteur quand documenté, raccord outil et variantes.

## Petit format

Préserver la définition multidimensionnelle du compact. Ajouter dimensions/empreinte/rangement, poids prêt à travailler lorsque disponible, maniabilité transport et fréquence de vidage. Éviter de transformer la page en long catalogue.

---

# 7. MERGE proposé — Sans sac

Cible recommandée : `/guides/sac-ou-sans-sac/`.

À préserver de la page comparatif lors d'une consolidation éventuelle :

- exemple du Bosch GAS 18V-10 L explicitement conçu sans sac ;
- distinction entre conçu sans sac / peut collecter en cuve / système de collecte conseillé ;
- exemples produits lorsqu'ils apportent une vraie valeur d'achat.

Le guide doit devenir la ressource canonique sur la décision avec/sans sac, éventuellement enrichie d'un petit bloc de références concrètes. Aucun redirect, canonical ou suppression ne doit être appliqué sans validation humaine explicite.

---

# 8. Ordre de rollout recommandé

1. `aspirateur-classe-m` — DEEP_REWRITE
2. `aspirateur-industriel` — DEEP_REWRITE
3. `aspirateur-chantier-puissant` — DEEP_REWRITE
4. `meilleur-aspirateur-de-chantier` — DEEP_REWRITE
5. `aspirateur-chantier-sans-fil` — DEEP_REWRITE
6. `aspirateur-professionnel` — LIGHT_UPDATE
7. `aspirateur-eau-poussiere` — LIGHT_UPDATE
8. `petit-aspirateur-de-chantier` — LIGHT_UPDATE
9. `aspirateur-chantier-sans-sac` — MERGE decision / human structural review

Après chaque page : vrai run-evidence v2, validation machine, `PUBLISH_REVIEW`, maintien du `noindex`.

Après les 8 pages éditoriales + décision humaine sur le merge : nouveau `CLUSTER_AUDIT` avant toute indexation.

---

# 9. Verdict final

**FAIL — REQUIRES_WORKFLOW_RERUN — KEEP_NOINDEX**

Le cluster possède maintenant une meilleure architecture conceptuelle qu'avant le rollout du 09/09, mais il ne doit plus être déclaré READY simplement parce que les H2 diffèrent et que les fiches fabricants sont correctes.

Sous le contrat v2 :

- les skills partagés doivent réellement être exécutés ;
- leur output doit être persisté ;
- la valeur originale doit être démontrée par page ;
- l'anti-template doit contrôler la fonction des sections ;
- les 9 URLs restent `noindex, follow` ;
- aucune indexation automatique n'est autorisée.
