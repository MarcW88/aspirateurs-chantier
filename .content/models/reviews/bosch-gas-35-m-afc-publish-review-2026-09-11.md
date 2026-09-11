# Publish review — Bosch GAS 35 M AFC

Date : 11 septembre 2026  
Mode : `model-analysis-workflow / PUBLISH_REVIEW`  
Page : `/modeles/bosch-gas-35-m-afc/`

## Résultat

**PASS — READY_FOR_HUMAN_VALIDATION**

La page reste `noindex, follow`. Ce PASS n'autorise pas l'indexation automatique.

## Pourquoi le pilote passe

### Intention

PASS. La page répond désormais à une décision précise : choisir ou non le GAS 35 M AFC dans l'écosystème Bosch, en particulier face au GAS 35 L AFC et au GAS 55 M AFC.

### Rôle MODEL

PASS. La page reste centrée sur une référence. Elle renvoie au comparatif classe M pour le choix inter-marques au lieu de reproduire ce classement.

### Factualité et référence exacte

PASS. Les valeurs centrales ont été revérifiées le 11/09/2026 sur les pages officielles Bosch Professional :

- GAS 35 M AFC : 1 200 W, 12,4 kg, 35 L brut / 23 L net / 19,2 L eau, classe M, 6 150 cm², 74 l/s et 254 mbar à la turbine, AFC ;
- GAS 35 L AFC : mêmes volumes, 6 150 cm², 74 l/s et 254 mbar, classe L, 12,2 kg ;
- GAS 55 M AFC : classe M, 55 L brut / 43 L net / 40 L eau, 16,2 kg, 6 150 cm², 74 l/s et 254 mbar à la turbine.

Sources :

- https://www.bosch-professional.com/be/fr/products/gas-35-m-afc-06019C31W0
- https://www.bosch-professional.com/be/fr/products/gas-35-l-afc-06019C32W0
- https://www.bosch-professional.com/be/fr/products/gas-55-m-afc-06019C3300

### Niveau de preuve

PASS. La page distingue les faits fabricant des déductions documentaires. Elle ne prétend pas avoir mesuré le maintien du débit, la maniabilité, le bruit ou la facilité de vidage.

`evidence-based-reviews` est `N/A` : aucun jugement subjectif sur qualité, fiabilité, ergonomie ou performance observée n'est nécessaire au draft final.

### Valeur sans affiliation

PASS. Même sans lien marchand, la page apporte trois éléments que la fiche fabricant ne formule pas directement :

1. le GAS 35 M n'est pas plus puissant que le GAS 35 L selon les maxima publiés ;
2. le choix 35 M vs 55 M porte principalement sur volume utile et masse ;
3. l'AFC est expliqué comme fonction de workflow sans être transformé en résultat de test.

### Distinctivité inter-modèles

PASS. Le squelette legacy `Comment lire / Quand choisir / Limites / Source` a disparu. Le plan est spécifique au conflit de décision de cette référence :

1. 35 M vs 35 L ;
2. AFC et niveau de preuve ;
3. 35 M vs 55 M ;
4. workflow où le 35 M devient cohérent ;
5. limites ;
6. sources.

### Cannibalisation

PASS. Le rôle avec `/comparatifs/aspirateur-classe-m/` est clarifié : le comparatif choisit entre plusieurs références ; la page modèle approfondit le GAS 35 M AFC.

Le hub `/marques/bosch/` conserve son rôle de lecture de gamme.

### Maillage

PASS. Liens contextuels vers :

- `/comparatifs/aspirateur-classe-m/` ;
- `/guides/decolmatage-automatique/` ;
- `/marques/bosch/`.

### SEO technique

PASS.

- canonical inchangée ;
- `noindex, follow` conservé ;
- title spécifique ;
- meta description spécifique ;
- H1 unique sur la référence ;
- sommaire aligné sur les H2 bespoke ;
- date de vérification spécifique au pilote : 11/09/2026.

### Editorial QA / anti-AI

PASS. Pas de FAQ automatique, conclusion générique, quota de sections ou répétition du plan des autres modèles pilotes. Les tableaux servent deux décisions concrètes et ne dupliquent pas simplement la spec sheet du hero.

## Limites encore assumées

- pas de test physique ;
- pas de synthèse utilisateurs ;
- pas de benchmark indépendant de colmatage/AFC ;
- pas de prix ou disponibilité marchande, volontairement exclus du socle éditorial pérenne.

Ces limites sont explicites et ne bloquent pas une page documentaire de référence.

## Gate

**PASS — READY_FOR_HUMAN_VALIDATION**

Étape suivante : validation humaine du rendu et de la stratégie avant toute instruction d'indexation ou déploiement du workflow aux autres `/modeles/`.
