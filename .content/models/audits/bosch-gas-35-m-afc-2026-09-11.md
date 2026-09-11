# Model Analysis — `/modeles/bosch-gas-35-m-afc/`

Date : 11 septembre 2026  
Mode : `AUDIT`  
Type : `MODEL`

## Décision

**`DEEP_REWRITE` — confiance HIGH**

La référence a une forte raison d'être en page autonome, mais la page actuelle reste trop proche d'une fiche constructeur condensée et du squelette générique des autres `/modeles/`. Elle ne traite pas assez le vrai choix : pourquoi prendre précisément le GAS 35 M AFC plutôt qu'un GAS 35 L AFC, un autre M ou un modèle plus volumineux.

La page reste `noindex, follow`.

## Valeur déjà présente

- classe M correctement documentée ;
- 35 L brut / 23 L net / 19,2 L eau correctement distingués ;
- 74 l/s et 254 mbar correctement qualifiés comme valeurs à la turbine ;
- AFC identifié comme automatique ;
- poids de 12,4 kg ;
- lien vers le comparatif classe M, l'usage ponceuse et le hub Bosch ;
- transparence sur l'absence de test physique.

## Vérification factuelle — source primaire actuelle

Source vérifiée le 11/09/2026 :

`https://www.bosch-professional.com/be/fr/products/gas-35-m-afc-06019C31W0`

Bosch confirme notamment :

- puissance nominale 1 200 W ;
- poids 12,4 kg ;
- 35 L brut / 23 L net / 19,2 L eau ;
- classe M ;
- surface filtrante 6 150 cm² ;
- 74 l/s max. à la turbine ;
- 254 mbar max. à la turbine ;
- nettoyage automatique du filtre AFC ;
- usage eau/poussière ;
- flexible antistatique sur la variante documentée.

Statut : `VERIFIED`. La référence est toujours présente dans le catalogue Bosch consulté.

## Intention et rôle autonome

La page doit répondre à une décision précise :

> **Le GAS 35 M AFC est-il le bon Bosch classe M filaire pour mon workflow, et qu'est-ce que je gagne réellement face au GAS 35 L AFC ou à un modèle M plus volumineux ?**

Elle ne doit pas refaire le classement de `/comparatifs/aspirateur-classe-m/` ni expliquer toute la gamme Bosch.

## Cannibalisation

### Avec `/comparatifs/aspirateur-classe-m/`

**Risque ÉLEVÉ si la page reste actuelle.** Le comparatif apporte déjà plus de valeur : maintien du débit, décolmatage, surveillance, collecte, mobilité et mise en contexte inter-modèles.

La fiche modèle doit donc devenir la page de profondeur sur la référence exacte.

### Avec `/marques/bosch/`

**Risque MODÉRÉ.** Le hub Bosch explique déjà que GAS 35 M AFC et GAS 55 M AFC partagent 74 l/s et 254 mbar à la turbine, et que le choix se joue davantage sur volume et mobilité. La page modèle doit développer cette conséquence plutôt que répéter les chiffres.

### Avec le GAS 35 L AFC

**Opportunité majeure.** Bosch publie pour le GAS 35 L AFC les mêmes 35 L brut / 23 L net / 19,2 L eau, 6 150 cm², 74 l/s et 254 mbar, avec un poids de 12,2 kg contre 12,4 kg pour le M. La fiche M doit expliquer que la différence décisive n'est donc pas un podium de puissance mais la classe/certification et l'équipement associé à la référence exacte.

## Evidence-based review

Aucun faux hands-on détecté. Les affirmations de spécification sont Tier 1.

Pour toute conclusion sur confort, bruit, facilité de vidage, efficacité AFC en poussière fine ou qualité d'usage, utiliser Tier 2/3 ou qualifier la phrase comme déduction. Ne pas transformer la promesse Bosch de « pouvoir aspirant constant » en mesure indépendante.

## Structure / AI-slop

**FAIL.** Même architecture que les autres pages pilotes :

1. `Comment lire cette référence`
2. `Quand ce modèle est cohérent`
3. `Limites et garde-fous`
4. `Source fabricant`

La structure ne reflète pas le point distinctif de cette référence : classe M + AFC + position intermédiaire 35 L dans l'écosystème Bosch.

## Blockers

1. architecture éditoriale clonée ;
2. aucune comparaison décisionnelle directe avec le GAS 35 L AFC alors qu'ils partagent presque toutes les valeurs principales ;
3. différenciation insuffisante face au GAS 55 M AFC ;
4. AFC mentionné mais pas expliqué comme conséquence de workflow ;
5. « ponçage et poussières fines » reste trop générique sans distinguer classe requise, captage et limites ;
6. la page ne crée pas encore plus de valeur que la ligne correspondante du comparatif classe M.

## Direction de réécriture

Le brief devrait tester notamment :

- pourquoi la classe M est ici plus structurante que les maxima de débit/dépression ;
- GAS 35 M AFC vs GAS 35 L AFC : ce qui est réellement identique et ce qui change ;
- GAS 35 M AFC vs GAS 55 M AFC : volume, masse, fréquence de vidage et mobilité ;
- ce que fait AFC et ce qu'il ne garantit pas ;
- rôle de la prise outil, du flexible antistatique et de Click & Clean dans un workflow réel ;
- situations où 35 L est un meilleur compromis que 55 L ;
- limites de la classe M et nécessité de partir du risque réel.

## Prochaine étape

`model-content-workflow` en `DEEP_REWRITE`, puis `model-analysis-workflow / PUBLISH_REVIEW`.

Priorité pilote : **1/3**. C'est le meilleur modèle pour valider le nouveau workflow parce que la distinction avec le GAS 35 L AFC donne un angle décisionnel très fort et vérifiable.
