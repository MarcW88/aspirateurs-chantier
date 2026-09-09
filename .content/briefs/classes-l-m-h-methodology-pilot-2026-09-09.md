# Pilot 80/20 — /guides/classes-l-m-h/

Date : 2026-09-09
Mode : RECOVERY
Décision : **LIGHT_UPDATE**
Confiance : élevée

## Pourquoi cet article

Ce guide est un bon stress test pour la méthodologie 80/20 : l’intention est informationnelle, mais plusieurs affirmations touchent à la prévention des poussières dangereuses. La couche générique doit donc gérer intention, conservation, structure, fact-check, natural writing, maillage, SEO et QA ; la couche aspirateurs-chantier doit imposer la prudence sur L/M/H, HEPA, captage, colmatage, débit et maintenance.

## Intention

Question principale : comprendre ce que signifient les classes L, M et H d’un aspirateur de chantier et comment déterminer la classe à examiner sans confondre classe d’appareil, filtre HEPA et simple nom de matériau.

Rôle : guide technique de décision, en amont du comparatif `/comparatifs/aspirateur-classe-m/` et des pages usages.

## Valeur existante à conserver

- Réponse rapide déjà présente.
- Distinction appareil complet vs filtre HEPA.
- Référence à EN/IEC 60335-2-69.
- Seuils de séparation L/M/H correctement présentés.
- Prudence sur le fait qu’un matériau ne définit pas toujours à lui seul la classe pertinente.
- Bon passage sur captage à la source et silice.
- Bon passage amiante : classe H + filtre THE.
- Maintenance/vidage déjà intégrés au raisonnement.
- Liens internes vers plâtre, bois, classe M, HEPA, débit, décolmatage et entretien.
- Sources IEC, INRS et fabricant.

## Problèmes constatés

### 1. Réponse initiale perfectible

La formulation « de nombreux poussières » contient une faute et l’ouverture peut être plus nette sur le point central : L/M/H concernent l’appareil complet, pas seulement le filtre.

### 2. Lecture décisionnelle trop linéaire

Le contenu explique correctement les classes mais oblige le lecteur à reconstruire lui-même le repère L/M/H. Ajouter un tableau synthétique apporte une vraie valeur sans transformer la page en catalogue.

### 3. Risque d’association trop mécanique matériau → classe

Le texte est déjà prudent, mais certains exemples (bois, plâtre, béton) peuvent être lus comme des affectations universelles. La révision doit distinguer exemples fabricants et exigence réelle issue du risque, de la composition, de la VLEP et du procédé.

### 4. Opportunité de fraîcheur 2026

L’INRS a publié en 2026 une communication sur l’évolution des performances d’aspirateurs M et H en cours d’utilisation. Sur les appareils étudiés, les versions H se colmatent plus vite, mais présentent une meilleure efficacité de filtration et moins de relargage au décolmatage. L’étude est limitée à deux modèles comparés en M/H et ne doit pas être généralisée.

## Sources vérifiées le 09/09/2026

- IEC 60335-2-69:2021 — https://webstore.iec.ch/en/publication/64777
- Festool, catégories de poussières L/M/H — https://www.festool.fr/campagnes/microsites/aspiration
- INRS, prévention du risque amiante — https://www.inrs.fr/risques/amiante/prevention-risque-amiante.html
- INRS, silice cristalline — https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir.html
- INRS 2026, évolution des performances en cours d’utilisation — https://www.inrs.fr/inrs/recherche/etudes-publications-communications/doc/communication.html?refINRS=NOETUDE%2FC2026-013

## Fact-check

- `CONFIRMED` — EN/IEC 60335-2-69 est la référence utilisée pour les classes de poussières des extracteurs commerciaux.
- `CONFIRMED` — degrés de séparation couramment repris : >99 % L, >99,9 % M, >99,995 % H.
- `CONFIRMED` — HEPA H13/H14 est une classification de filtre distincte de la classe H de l’aspirateur.
- `CONFIRMED` — pour l’amiante, l’INRS demande classe H selon IEC 60335-2-69 et filtre THE au minimum H13/H14, avec exigences complémentaires.
- `CONFIRMED` — l’INRS recommande le captage à la source et le raccordement des outils aspirants à une aspiration haute dépression pour la silice.
- `CONFIRMED_WITH_LIMITATION` — étude INRS 2026 : colmatage plus rapide des H sur les modèles testés, meilleure filtration et moins de relargage ; ne pas généraliser à tous les aspirateurs H.

## Refresh plan

### Conserver

Environ 80–85 % du raisonnement existant : norme, prudence sur les matériaux, HEPA vs classe H, choix de classe, entretien, sources et maillage.

### Réécrire légèrement

- answer-box ;
- premier paragraphe de définition ;
- formulations pouvant suggérer une correspondance matériau → classe trop automatique ;
- passage sur le choix pour clarifier la séquence « classe requise d’abord, performance ensuite ».

### Ajouter

- tableau L/M/H de lecture rapide ;
- section courte sur l’étude INRS 2026 et le compromis colmatage/débit/filtration ;
- source INRS 2026.

### Supprimer

Aucune section de fond. Pas de suppression justifiée au-delà des répétitions reformulées.

## Maillage

Conserver les liens vers :

- `/comparatifs/aspirateur-classe-m/`
- `/guides/filtre-hepa-aspirateur/`
- `/guides/debit-air-aspirateur/`
- `/guides/decolmatage-automatique/`
- `/guides/prise-asservie/`
- `/guides/entretien-aspirateur-chantier/`
- `/guides/sac-ou-sans-sac/`
- `/usages/aspirateur-platre/`
- `/usages/aspirateur-bois-sciure-copeaux/`

## 80/20 appliqué

### Shared

`content-recovery-and-production-workflow`, `search-intent`, `content-audit`, `content-refresh`, `fact-check`, `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-technical`, `seo-best-practices`, `editorial-qa`.

### Custom aspirateurs-chantier

- classe d’appareil ≠ filtre ;
- pas d’inférence de classe depuis HEPA, watts ou débit ;
- matériau ≠ classe universelle ;
- captage à la source ;
- colmatage/décolmatage et maintien du débit ;
- maintenance/vidage comme partie du système de prévention ;
- prudence sur les recommandations relatives aux poussières dangereuses.

## Statut attendu après génération

`PASS — READY_FOR_HUMAN_VALIDATION`, tout en conservant `noindex, follow`.
