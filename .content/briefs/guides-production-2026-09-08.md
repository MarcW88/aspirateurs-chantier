# Content Briefs — Cluster /guides/

```yaml
mode: NEW_CONTENT
status: BRIEF_READY
quality_reference: /guides/comment-choisir-aspirateur-de-chantier/
created: 2026-09-08
scope: 11 guides
source_of_truth: _generate_guides.py
```

## Contexte commun

Les 11 pages existent mais leur article est vide ou limité à une réponse courte et un placeholder. Elles sont donc routées en `NEW_CONTENT`. L’objectif est de créer un cluster informationnel différencié qui aide à choisir un aspirateur de chantier sans transformer les guides en pages de vente, avec des transitions naturelles vers comparatifs, usages, modèles et accessoires.

Principes éditoriaux : réponse answer-first, 5 H2 substantiels minimum, au moins 4 liens internes contextuels vers 3 cibles différentes, au moins 3 sources externes, pas de prix ni de test inventé, pas de seuil de performance présenté comme universel sans source, distinction systématique entre classe de filtre et classe de l’appareil.

## Evidence register commun

| Claim | Source | Consulté le | Stabilité | Statut |
|---|---|---:|---|---|
| IEC 60335-2-69:2021 couvre les aspirateurs commerciaux eau/poussière et les machines manipulant des poussières dangereuses | https://webstore.iec.ch/en/publication/64777 | 2026-09-08 | élevée | CONFIRMED |
| Classes L/M/H : degrés de séparation >99 %, >99,9 %, >99,995 % et domaines d’usage associés | https://www.festool.fr/produits/aspirateurs/aspirateurs-de-chantier/577891---ctl-36-ei-ac-renofix | 2026-09-08 | élevée | CONFIRMED |
| GAS 35 M AFC : nettoyage automatique destiné à maintenir l’aspiration ; 74 L/s et 254 mbar à la turbine sur la variante FR consultée | https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0/ | 2026-09-08 | moyenne (variante produit) | CONFIRMED |
| Pour la silice, l’INRS recommande le captage à la source et le raccordement des outils aspirants à des systèmes haute dépression | https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir.html | 2026-09-08 | élevée | CONFIRMED |
| Pour l’amiante, l’INRS demande un aspirateur classe H selon IEC 60335-2-69, avec filtration THE au minimum H13/H14 et exigences complémentaires | https://www.inrs.fr/risques/amiante/prevention-risque-amiante.html | 2026-09-08 | élevée | CONFIRMED |
| EN 1822 : H13 ≥99,95 % et H14 ≥99,995 % à la MPPS | https://airfiltration.mann-hummel.com/en-uk/insights/filter-classification/din-en-1822.html | 2026-09-08 | élevée | CONFIRMED |
| Pour le bois, le captage/transport/filtration et l’aspiration des machines portatives doivent être pensés comme un système | https://www.inrs.fr/media.html?refINRS=ED+6052 | 2026-09-08 | élevée | CONFIRMED |

## 1. /guides/comment-choisir-aspirateur-de-chantier/
- Mot-clé principal : comment choisir un aspirateur de chantier
- Variantes : critères aspirateur chantier, quel aspirateur chantier, choisir aspirateur eau poussière
- Intention : guide décisionnel global, milieu de funnel
- Question centrale : quels critères éliminent réellement les mauvais choix ?
- Concepts : classes L/M/H, captage à la source, débit, dépression, colmatage, cuve, raccords
- Entités : IEC 60335-2-69, INRS, Bosch, Festool
- Différenciation : hiérarchiser les critères par risque et usage, pas par watts ou prix
- Architecture : priorités → classe → performance → équipements → cuve → cas d’usage → erreurs
- Maillage : classes L/M/H, débit, dépression, prise asservie, comparatif général, pages usages
- Risques : recommandations trop générales ; éviter les seuils universels
- Niveau : NEW

## 2. /guides/classes-l-m-h/
- Mot-clé principal : classe L M H aspirateur
- Variantes : aspirateur classe M, différence classe L M H, classe poussière aspirateur
- Intention : comprendre une classification de sécurité avant achat
- Question centrale : quelle classe correspond au risque réel ?
- Concepts : degré de séparation, VLEP, poussières dangereuses, certification de l’appareil
- Entités : IEC/EN 60335-2-69, INRS, Festool
- Différenciation : distinguer clairement matériau, risque, VLEP et classe ; ne pas transformer des exemples en obligation universelle
- Architecture : norme → différences → matériaux → HEPA vs classe H → méthode de choix → maintenance
- Maillage : HEPA, plâtre, bois, classe M, entretien
- Risques : réglementation et amiante ; claims sourcés uniquement
- Niveau : NEW

## 3. /guides/decolmatage-automatique/
- Mot-clé principal : décolmatage automatique aspirateur
- Variantes : AFC aspirateur, nettoyage automatique filtre, auto clean aspirateur
- Intention : comprendre l’intérêt fonctionnel et décider si l’option vaut le surcoût
- Concepts : perte de charge, gâteau de poussière, maintien du débit, filtre
- Entités : Bosch AFC, systèmes auto-clean
- Différenciation : expliquer que les technologies varient et que le bénéfice est le maintien du débit, pas un filtre « toujours propre »
- Architecture : colmatage → technologies → usages → limites → comparaison → entretien
- Maillage : débit, ponceuse, plâtre, Bosch GAS 35 M AFC
- Risques : ne pas inventer de fréquence ou mécanisme unique pour toutes les marques
- Niveau : NEW

## 4. /guides/prise-asservie/
- Mot-clé principal : prise asservie aspirateur chantier
- Variantes : prise outil aspirateur, démarrage automatique aspirateur, prise électroportatif
- Intention : comprendre fonctionnement, compatibilité et sécurité électrique
- Question centrale : quand la prise asservie change-t-elle réellement l’usage ?
- Concepts : détection de consommation, temporisation, puissance admissible, raccord outil
- Différenciation : supprimer le faux seuil générique de 2 200 W ; renvoyer à la notice de chaque appareil
- Architecture : principe → usages → puissance/sécurité → sans-fil → raccord → critère d’achat
- Maillage : ponceuse, scie, adaptateurs, sans-fil, décolmatage
- Risques : valeur de puissance variable selon modèle/pays
- Niveau : NEW

## 5. /guides/puissance-aspiration/
- Mot-clé principal : puissance aspirateur de chantier
- Variantes : watts aspirateur chantier, puissance aspiration, aspirateur chantier puissant
- Intention : décoder les métriques marketing
- Question centrale : pourquoi les watts ne suffisent-ils pas ?
- Concepts : puissance absorbée, rendement, débit, dépression, point de fonctionnement
- Différenciation : enseigner une lecture de fiche technique plutôt que fournir un seuil arbitraire
- Architecture : watts → dépression → débit → interaction → point de mesure → choix selon usage
- Maillage : dépression, débit, comparatif puissants, guide de choix
- Risques : ne pas comparer des données turbine et flexible comme équivalentes
- Niveau : NEW

## 6. /guides/depression-kpa-mbar-air-watt/
- Mot-clé principal : kPa mbar aspirateur
- Variantes : dépression aspirateur, air watts aspirateur, mmH2O aspirateur
- Intention : conversion et interprétation technique
- Concepts : Pa, kPa, mbar, mmH2O, pression, débit, puissance aéraulique
- Facts : 1 kPa = 10 mbar ; 1 kPa ≈ 101,97 mmH2O
- Différenciation : insister sur les conditions de mesure et le point de fonctionnement
- Architecture : définition → conversions → Air Watts → relation au débit → fiches fabricants → usages
- Maillage : débit, puissance, comparatif, guide de choix
- Risques : ne pas présenter Air Watts comme une métrique normalisée et disponible partout
- Niveau : NEW

## 7. /guides/debit-air-aspirateur/
- Mot-clé principal : débit air aspirateur chantier
- Variantes : L/s aspirateur, m3/h aspirateur chantier, débit aspiration ponceuse
- Intention : comprendre le captage à la source
- Concepts : débit volumique, pertes de charge, flexible, capot, colmatage
- Facts : 1 L/s = 3,6 m3/h
- Différenciation : distinguer débit turbine et débit disponible au poste
- Architecture : définition → unités → captage → mesure → filtre → choix
- Maillage : bois, ponceuse, décolmatage, sac, dépression
- Risques : pas de seuil universel sans contexte outil/flexible
- Niveau : NEW

## 8. /guides/capacite-cuve/
- Mot-clé principal : capacité cuve aspirateur chantier
- Variantes : aspirateur 20 30 40 litres, volume cuve aspirateur
- Intention : dimensionnement pratique
- Concepts : brut/net, volume eau, poids rempli, sac, fréquence de vidage
- Evidence : GAS 35 M AFC = 35 L brut / 23 L net / 19,2 L eau sur variante FR consultée
- Différenciation : remplacer les recommandations arbitraires par une méthode de dimensionnement
- Architecture : brut/net → mobilité → type de déchets → eau → sac/filtre → méthode
- Maillage : petit format, gravats, atelier, eau/poussière, sac
- Risques : caractéristiques produit variables selon variante
- Niveau : NEW

## 9. /guides/filtre-hepa-aspirateur/
- Mot-clé principal : filtre HEPA aspirateur chantier
- Variantes : H13 H14 aspirateur, HEPA classe H, filtre absolu aspirateur
- Intention : distinguer norme filtre et certification de l’appareil
- Concepts : EN 1822, MPPS, H13, H14, IEC 60335-2-69, classe H
- Différenciation : corriger le raccourci « H13 = classe H »
- Architecture : HEPA → H13/H14 → classe H → utilité chantier → amiante → entretien
- Maillage : classes L/M/H, débit, filtres accessoires, entretien
- Risques : santé/amiante ; rester strictement sur sources INRS et normes
- Niveau : NEW

## 10. /guides/sac-ou-sans-sac/
- Mot-clé principal : aspirateur chantier sac ou sans sac
- Variantes : sac aspirateur chantier, aspirateur poussière sans sac, sac classe M
- Intention : arbitrage coût / filtration / vidage
- Concepts : préfiltration, colmatage, remise en suspension, collecte, liquide
- Différenciation : ne pas traiter le sac comme simple coût récurrent ; intégrer sécurité et temps de maintenance
- Architecture : rôle → sans-sac → poussières fines → M/H → coût réel → choix
- Maillage : décolmatage, classes, sacs, filtres, capacité, entretien
- Risques : ne pas généraliser la configuration des classes M/H ; suivre notice/certification
- Niveau : NEW

## 11. /guides/entretien-aspirateur-chantier/
- Mot-clé principal : entretien aspirateur de chantier
- Variantes : nettoyer filtre aspirateur chantier, maintenance aspirateur eau poussière
- Intention : prolonger durée de vie et maintenir performances
- Concepts : filtre, sac, joints, flexible, flotteur, humidité, refroidissement, maintenance dangereuse
- Différenciation : procédures concrètes + limites claires sur lavage/soufflage des filtres
- Architecture : après chantier → filtre → cuve/eau → flexible/joints → moteur → poussières dangereuses
- Maillage : décolmatage, sacs, sac/sans-sac, classes
- Risques : ne pas recommander de lavage ou air comprimé sans autorisation fabricant
- Niveau : NEW

## Décision de production

Tous les guides peuvent être rédigés sans test produit ni prix. Les claims réglementaires ou liés aux poussières dangereuses restent limités aux formulations confirmées par IEC/EN et INRS. Le contenu restera en `noindex,follow` et ne passera pas au statut `PUBLISHABLE` avant validation humaine.