---
name: site-design-review
description: Auditer et améliorer le design et l’implémentation frontend d’aspirateurs-chantier.fr afin de détecter les interfaces génériques, les défauts UX, les problèmes de confiance éditoriale, d’accessibilité et de cohérence. Utiliser pour les audits de pages, composants, previews et pull requests frontend. Ne pas utiliser pour les contenus SEO seuls ou le backend sans interface.
---

# Audit design du site

Effectuer une revue exigeante et contextualisée du frontend. Le but n’est pas de maximiser la décoration, mais de produire un média technique spécialisé crédible, distinctif et utile.

Avant l’audit, lire `DESIGN.md` et inspecter les composants, styles et tokens réellement présents. `style.css` est la source de vérité visuelle du projet : éviter de disperser les corrections dans des feuilles de style par page. Si le site peut être lancé, analyser les rendus réels plutôt que le code seul.

## Portée

Déterminer si la demande concerne :

- une page ou un composant ;
- une pull request ou un diff ;
- une revue globale ;
- une capture d’écran ou une preview ;
- une validation avant publication.

Ne pas étendre l’audit à tout le site lorsqu’une modification locale suffit.

## Vérification visuelle

Lorsque l’environnement le permet :

1. lancer le site avec les commandes définies par le projet ;
2. examiner au minimum un viewport mobile et un viewport desktop ;
3. parcourir les états interactifs importants ;
4. vérifier le reflow, le focus clavier, les débordements et les contenus tronqués ;
5. comparer la page aux règles de `DESIGN.md`.

Si aucun rendu n’est disponible, signaler explicitement que les conclusions sont limitées au code et au HTML généré.

## Axes d’audit

### Identité

- La page évoque-t-elle un média technique consacré aux aspirateurs de chantier et à la maîtrise des poussières ?
- Possède-t-elle une direction reconnaissable sans copier une marque d’outillage ?
- La composition est-elle intentionnelle ou ressemble-t-elle à un assemblage de composants standards ?
- La donnée technique aide-t-elle la décision au lieu de transformer la page en dashboard ?

### Signes de design générique

Chercher les patterns décrits dans la section « Règles anti-design générique » de `DESIGN.md`. Ne pas considérer un pattern isolé comme une preuve. Évaluer leur accumulation, leur manque de justification et leur répétition.

Ne jamais affirmer qu’une interface a été créée par IA. Dire plutôt qu’elle présente des conventions génériques fréquemment observées dans des interfaces assemblées automatiquement.

### Hiérarchie et UX

- L’objectif de la page est-il immédiatement compréhensible ?
- L’action principale est-elle claire sans écraser le contenu ?
- Les comparaisons permettent-elles une décision réelle ?
- Les tableaux restent-ils lisibles sur petit écran ?
- La navigation, les filtres et les liens ont-ils des libellés explicites ?
- Le lecteur distingue-t-il information technique, jugement éditorial et action commerciale ?

### Confiance éditoriale et affiliation

- Le niveau de preuve est-il visible ?
- Les avantages et limites sont-ils équilibrés ?
- Les liens affiliés sont-ils identifiables ?
- Les prix et dates de vérification sont-ils contextualisés ?
- Le design crée-t-il une urgence ou une autorité artificielle ?
- Les termes « test », « mesuré » ou « vérifié » correspondent-ils réellement à la méthode utilisée ?

### Craft et accessibilité

- Cohérence des tokens, espacements, rayons, bordures et typographies.
- Contraste, focus visible, navigation clavier, textes alternatifs et HTML sémantique.
- États hover, focus et active lorsque pertinents.
- Menu mobile réellement utilisable au clavier et au tactile.
- Absence de contenu tronqué, de débordement ou de rupture responsive.
- Performance visuelle raisonnable : mouvements limités et stabilité du layout.

## Priorisation

Classer les constats :

- **Bloquant** : empêche l’usage, trompe le lecteur ou crée un problème sérieux d’accessibilité.
- **Majeur** : affaiblit nettement l’identité, la décision ou la crédibilité.
- **Mineur** : défaut local de cohérence ou de finition.
- **Suggestion** : amélioration facultative, dépendante d’un choix créatif.

Ne pas gonfler artificiellement le nombre de constats. Regrouper les symptômes qui proviennent d’une même cause.

## Format de restitution

Commencer par un verdict en deux ou trois phrases.

Puis fournir :

1. **Ce qui fonctionne** : maximum cinq observations concrètes.
2. **Problèmes prioritaires** : tableau avec sévérité, emplacement, preuve, impact et correction recommandée.
3. **Signaux de design générique** : uniquement ceux réellement constatés.
4. **Mobile et accessibilité** : résultats vérifiés et limites de la vérification.
5. **Ordre de correction** : liste courte, du plus important au plus cosmétique.

Citer les fichiers ou composants concernés. Pour une revue visuelle, associer les constats aux captures ou viewports examinés.

## Implémentation

Lorsque l’utilisateur demande explicitement d’optimiser ou de corriger le design :

1. corriger d’abord les problèmes bloquants et majeurs ;
2. privilégier les tokens et composants globaux de `style.css` ;
3. modifier les générateurs lorsque le même HTML est reproduit sur plusieurs pages ;
4. rendre les scripts de post-traitement idempotents ;
5. vérifier au minimum la homepage, un comparatif, un guide, une page marque et une fiche modèle ;
6. conserver les directives d’indexation existantes sauf demande explicite contraire ;
7. terminer par un gate QA documenté.

Sources d’inspiration méthodologique : Microsoft Frontend Design Review et Impeccable. Les règles propres au projet dans `DESIGN.md` prévalent.
