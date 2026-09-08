# Direction visuelle — aspirateurs-chantier.fr

## Positionnement

Le site doit ressembler à un média technique spécialisé dans les aspirateurs de chantier, la gestion des poussières et l’aspiration à la source : précis, robuste, lisible et crédible.

Il ne doit pas ressembler à :

- une landing page SaaS ;
- un catalogue Amazon ;
- un faux laboratoire de test ;
- un dashboard industriel rempli de métriques décoratives ;
- un blog bricolage générique ;
- une interface manifestement assemblée automatiquement.

## Public et objectif

Le lecteur cherche à choisir un aspirateur adapté à une situation concrète : rénovation, plâtre, ponçage, sciure, gravats, atelier, outil électroportatif ou poussière nécessitant une classe particulière.

L’interface doit l’aider à comprendre les compromis entre sécurité poussière, maintien du débit, dépression, mobilité, capacité, compatibilité outil et coût total avant de l’envoyer vers un marchand.

## Identité visuelle

La direction doit évoquer la documentation technique et l’atelier sans copier les codes graphiques d’une marque d’outillage :

- fonds légèrement chauds plutôt qu’un blanc clinique ;
- bleu pétrole / acier comme couleur de structure ;
- orange sécurité utilisé comme accent, pas comme couleur publicitaire omniprésente ;
- données techniques en monospace uniquement lorsqu’elles gagnent réellement en lisibilité ;
- titres éditoriaux plus humains que les composants de dashboard ;
- bordures nettes et ombres très discrètes ;
- angles modérément arrondis ;
- tableaux et fiches techniques visuellement stables entre les pages.

## Palette

Les couleurs doivent être implémentées comme tokens dans `style.css`.

| Rôle | Couleur |
|---|---|
| Fond principal | `#F5F3EE` |
| Fond secondaire | `#EAE7E0` |
| Surface | `#FFFFFF` |
| Texte principal | `#1B252C` |
| Texte secondaire | `#5D676D` |
| Bleu pétrole principal | `#25516B` |
| Bleu pétrole sombre | `#193C52` |
| Accent orange sécurité | `#D36A2D` |
| Accent sombre | `#B6531F` |
| Bordure | `#D4D0C8` |
| Fond sombre | `#172029` |

Les couleurs des classes L, M et H restent sémantiques et ne doivent pas être remplacées par la palette de marque.

## Typographie

Direction recommandée :

- `Source Serif 4` pour les grands titres éditoriaux ;
- `Inter` pour le corps, les menus et les interfaces ;
- `JetBrains Mono` pour certaines données, classes, statuts et références techniques.

Le corps de texte doit rester à 16 px minimum sur desktop comme sur mobile. La longueur de ligne des articles doit rester confortable et ne pas utiliser toute la largeur disponible simplement parce qu’elle existe.

## Homepage

La homepage doit expliquer rapidement ce que le site permet de décider.

Le panneau de critères techniques ne doit pas simuler un dashboard ou une mesure scientifique avec des barres sans échelle explicite. Présenter les critères comme une fiche de référence est préférable.

Les sections « usages », « guides » et « marques » ne doivent pas toutes être des grilles de cartes identiques. Varier le rythme : lignes éditoriales, listes techniques, tableaux ou blocs de décision selon la nature de l’information.

## Pages éditoriales

Les guides, comparatifs et pages marques doivent privilégier :

- une largeur de lecture maîtrisée ;
- un verdict rapide clairement identifiable ;
- une hiérarchie forte entre H2, paragraphes, listes et tableaux ;
- des liens contextuels visibles sans transformer chaque phrase en CTA ;
- une date de vérification discrète mais lisible ;
- un sommaire utile et non décoratif ;
- des sources visuellement distinctes en fin de contenu.

## Comparatifs

Un comparatif doit permettre de décider avant de vendre.

Le tableau principal doit :

- rester lisible horizontalement sur mobile ;
- donner plus de poids visuel au modèle qu’au score ;
- présenter la limite principale avec autant de sérieux que l’avantage ;
- éviter l’apparence d’un classement pseudo-scientifique ;
- contextualiser les scores par la méthodologie.

## Fiches modèles

Les données techniques sont un atout distinctif. Leur traitement doit être plus proche d’une fiche de spécifications que d’une carte e-commerce.

Les blocs avantages / limites doivent rester équilibrés. Le design ne doit pas transformer une fiche modèle en argumentaire commercial.

## Navigation

- Navigation desktop utilisable à la souris et au clavier.
- Les dropdowns doivent s’ouvrir avec `:focus-within`, pas uniquement au hover.
- Le menu mobile doit fonctionner réellement, avec `aria-expanded`, fermeture par Échap et reflow correct.
- Le focus clavier doit toujours être visible.
- Un lien d’évitement vers le contenu principal est recommandé.

## Règles anti-design générique

Éviter notamment :

- les énormes titres centrés avec deux CTA et peu d’information ;
- les dégradés, glows et glassmorphism ;
- les ombres épaisses ;
- les coins très arrondis partout ;
- les badges décoratifs répétés ;
- les grilles systématiques de cartes identiques ;
- les icônes sans fonction informationnelle ;
- les barres de progression utilisées comme décoration ;
- les animations dispersées ;
- les faux témoignages et faux signaux d’urgence ;
- les notes globales sans méthode explicite ;
- les boutons d’achat répétés après chaque paragraphe ;
- la transformation de chaque section en carte autonome.

Une carte doit regrouper une information réellement autonome. Une bordure ou un fond ne sont pas nécessaires par défaut.

## Affiliation et confiance

- Identifier sans ambiguïté les liens affiliés.
- Ne pas masquer une publicité sous l’apparence d’un verdict éditorial.
- Présenter au moins une limite réelle pour chaque produit recommandé.
- Expliquer la méthodologie et les critères de classement.
- Ne pas prétendre avoir testé un appareil sans preuve documentée.
- Distinguer : testé, pris en main, analysé à partir de documentation, ou simplement comparé.
- Présenter les prix comme datés et susceptibles d’évoluer.

## Accessibilité et responsive

Une page n’est pas validée uniquement parce qu’elle s’empile sur mobile.

Vérifier :

- focus visible WCAG AA ;
- navigation clavier ;
- menu mobile ;
- contrastes ;
- tableaux scrollables sans casser le viewport ;
- boutons et liens avec zones tactiles suffisantes ;
- absence de texte sous 14 px pour une information importante ;
- réduction des animations lorsque `prefers-reduced-motion` est actif.

## Critères de validation

Une page est visuellement validée si :

1. son objectif et son action principale sont compris rapidement ;
2. elle paraît appartenir à un média technique spécialisé identifiable ;
3. la donnée technique sert la décision et ne ressemble pas à un dashboard décoratif ;
4. la hiérarchie reste claire sur mobile et desktop ;
5. les informations commerciales ne dominent pas l’éditorial ;
6. les composants sont cohérents sans rendre toutes les sections identiques ;
7. le contraste, le focus clavier et la structure sémantique sont corrects ;
8. le menu mobile est utilisable ;
9. aucun pattern anti-design générique important n’est présent.
