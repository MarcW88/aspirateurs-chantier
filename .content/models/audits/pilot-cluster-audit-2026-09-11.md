# Model Analysis — Pilot cluster

Date : 11 septembre 2026  
Mode : `CLUSTER_AUDIT`  
Scope :

- `/modeles/bosch-gas-18v-10-l/`
- `/modeles/bosch-gas-35-m-afc/`
- `/modeles/karcher-wd2/`

## Décision cluster

**`DEEP_REWRITE` sur les 3 pages — confiance HIGH sur le problème structurel.**

Aucun `MERGE` n'est recommandé : les trois références répondent à des décisions distinctes. Le problème commun est que le renderer impose une architecture identique qui masque ces différences.

## Signature clonée détectée

Les trois pages utilisent exactement :

1. `Comment lire cette référence`
2. `Quand ce modèle est cohérent`
3. `Limites et garde-fous`
4. `Source fabricant`

Elles répètent aussi :

- le même paragraphe expliquant que la fiche sert à vérifier une référence ;
- la même mise en garde générique sur L/M/H ;
- le même bloc final « analyse documentaire, sans test physique » ;
- la même logique `best_for` / `limits` issue du générateur ;
- le même emplacement des liens liés et de la source fabricant.

Cette cohérence dépasse le design system : elle constitue une **architecture éditoriale clonée**.

## Pourquoi les trois plans devraient diverger

### Bosch GAS 18V-10 L

Décision principale : mobilité, parc 18 V / AMPShare, petite cuve, autonomie `4 min/Ah`, classe L et arbitrage face au GAS 18V-12 MC ou à un filaire.

### Bosch GAS 35 M AFC

Décision principale : classe M + AFC + position 35 L, avec une comparaison particulièrement forte face au GAS 35 L AFC qui partage presque toutes les valeurs principales, et face au GAS 55 M AFC pour le compromis volume/mobilité.

### Kärcher WD 2 Plus

Décision principale : savoir si un petit wet/dry Home & Garden suffit pour garage/voiture/petits travaux, avec filtre sec/humide sans changement, 15 L, 4,4 kg, fonction soufflerie et limite liée à l'absence de prise outil/classe documentée.

Ces trois décisions n'ont aucune raison de produire les mêmes quatre H2.

## Factualité

Les données primaires centrales ont été recontrôlées le 11/09/2026 sur les pages officielles Bosch Professional et Kärcher.

- GAS 18V-10 L : données principales cohérentes et référence toujours commercialisée.
- GAS 35 M AFC : données principales cohérentes et référence toujours présente au catalogue.
- WD 2 : données principales cohérentes ; la dénomination exacte `WD 2 / WD 2 Plus V-15/4/18/C` doit être normalisée.

Aucune correction urgente de classe L/M/H n'est requise sur ces trois pages pilotes.

## Valeur originale

**FAIL cluster.** Les pages individuelles sont factuellement plus sûres qu'avant, mais leur valeur originale est encore trop faible : la plupart des éléments viennent directement de `model-evidence.json` puis sont rangés dans un template commun.

Le comparatif sans fil, le comparatif classe M et les hubs de marque contiennent parfois déjà une analyse plus riche que les pages modèles vers lesquelles ils pointent.

## Cannibalisation

- GAS 18V-10 L : risque élevé avec le comparatif sans fil si la fiche ne devient pas une analyse de profondeur de la référence.
- GAS 35 M AFC : risque élevé avec le comparatif classe M, mais très bonne opportunité de distinction via GAS 35 L AFC / GAS 55 M AFC.
- WD 2 : risque plus faible avec le comparatif eau/poussière ; rôle autonome plausible mais valeur actuelle insuffisante.

## Ordre recommandé pour la phase de production

1. **GAS 35 M AFC** — meilleur test du workflow : angle décisionnel fort, faits vérifiables et comparaison sibling très claire.
2. **GAS 18V-10 L** — permet de tester une page modèle structurée par un système batterie et un workflow mobile.
3. **Kärcher WD 2** — permet de vérifier que le workflow sait rester simple et utile sur un produit moins complexe sans gonfler artificiellement le contenu.

## Règle pour la phase suivante

Ne pas modifier `_generate_model_overrides.py` pour simplement remplacer un template par un autre template.

Pour chaque pilote :

1. `model-content-workflow` ;
2. evidence brief propre à l'URL ;
3. outline avec `question`, `evidence_refs`, `decision_value` ;
4. body bespoke ;
5. run-evidence v2 ;
6. `model-analysis-workflow / PUBLISH_REVIEW` ;
7. comparaison inter-modèles avant toute généralisation du renderer.

Les trois pages restent `noindex, follow` jusqu'à PASS et validation humaine explicite.
