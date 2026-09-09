# Design review — pages comparatifs — 2026-09-09

## Scope

Review Playwright en lecture seule sur :

- `/comparatifs/`
- `/comparatifs/meilleur-aspirateur-de-chantier/`
- `/comparatifs/aspirateur-eau-poussiere/`
- `/comparatifs/aspirateur-chantier-sans-fil/`
- `/comparatifs/aspirateur-chantier-sans-sac/`
- `/comparatifs/aspirateur-chantier-puissant/`
- `/comparatifs/aspirateur-professionnel/`
- `/comparatifs/aspirateur-industriel/`
- `/comparatifs/aspirateur-classe-m/`
- `/comparatifs/petit-aspirateur-de-chantier/`

Viewports : desktop `1440×1000` et mobile `390×844`.

Aucun correctif frontend n'est appliqué dans ce review.

## Verdict

**FAIL — DESIGN FIXES REQUIRED — KEEP_NOINDEX**

La structure desktop est globalement solide et cohérente avec la direction éditoriale technique du site. Les principaux blockers sont mobiles : navigation non fonctionnelle, sommaire placé après l'article et débordements de tableaux sur 6 pages. Les pages comparatives restent aussi trop textuelles et leurs tableaux manquent de scanabilité, particulièrement sur les longues pages de décision.

## P0 — Navigation mobile non fonctionnelle

Le bouton burger est visible sur `/comparatifs/`, mais un clic ne modifie pas `aria-expanded` et n'affiche pas `.site-nav`.

Playwright :

- `burgerAriaExpanded = null`
- `mobileMenuVisibleAfterClick = false`

Cause structurelle observée : les pages comparatifs ne chargent que `style.css` et ne chargent aucun script de navigation ; les corrections mobile déjà développées pour les pages marques sont actuellement limitées au scope `.brand-page` / `brand-pages.js`.

**Impact : bloquant.** Sur mobile, la navigation principale disparaît derrière un contrôle sans action.

## P0 — Débordement horizontal sur 6 pages mobiles

Le viewport Playwright mesure `390 px`. Six pages élargissent le document au-delà du viewport :

| Page | largeur document | dépassement |
| --- | ---: | ---: |
| Eau et poussière | 428 px | +38 px |
| Sans fil | 416 px | +26 px |
| Sans sac | 438 px | +48 px |
| Industriel | 453 px | +63 px |
| Classe M | 543 px | +153 px |
| Petit format | 555 px | +165 px |

Les tableaux sont bien dans un élément `.table-wrap`, mais le style responsive robuste de `.table-wrap` existe aujourd'hui uniquement dans `brand-pages.css` sous `.brand-page`. Sur les comparatifs, plusieurs tableaux conservent donc une largeur intrinsèque supérieure au conteneur et agrandissent la page entière.

Les trois pages qui ne débordent pas sont `meilleur`, `puissant` et `professionnel`, mais même sur ces pages la présentation tabulaire devient très serrée sur 390 px.

**Impact : bloquant pour la lisibilité des données.**

## P1 — Sommaire mobile placé après l'article

À `max-width:1024px`, `.content-layout` passe en une colonne et `.content-sidebar` devient statique. Comme le sidebar est situé après `<article>` dans le DOM, le sommaire apparaît après tout le contenu.

Mesures Playwright du top du sidebar en mobile :

- meilleur : ~3 193 px
- eau/poussière : ~2 950 px
- sans fil : ~3 201 px
- sans sac : ~3 421 px
- puissant : ~3 286 px
- professionnel : ~7 997 px
- industriel : ~3 711 px
- classe M : ~3 257 px
- petit format : ~2 966 px

Le cas professionnel est le plus critique : le sommaire n'aide plus à naviguer, puisqu'il n'apparaît qu'après près de 8 000 px de lecture.

Les pages marques ont déjà résolu ce problème avec une TOC mobile déplacée/repliable ; les comparatifs n'héritent pas de cette correction.

**Impact : majeur.**

## P1 — Tableaux trop peu scannables

Même sur desktop, les tableaux comparatifs générés utilisent une présentation très nue : peu de séparation visuelle entre lignes, beaucoup de texte dans les cellules et aucune hiérarchie fonctionnelle comparable au composant `.data-table` déjà présent dans `style.css`.

Sur mobile, le problème devient plus fort :

- 4 colonnes compressées dans 342 px lorsque le tableau réussit à tenir ;
- textes très étroits et nombreuses ruptures de ligne ;
- aucune indication qu'un tableau est horizontalement scrollable lorsqu'il dépasse ;
- les critères importants (classe, usage, limite, compromis) ont la même densité visuelle.

Le design devrait privilégier soit un tableau réellement scrollable avec largeur minimale et affordance claire, soit un reflow en cartes/lignes de décision pour les tableaux les plus narratifs.

## P1 — CTA trop tardif sur mobile

Les pages comparatifs n'ont aucun CTA primaire dans `.content-main` (`primaryActionCount = 0`). Le bouton `Choisir mon aspirateur` vit dans la sidebar.

Sur desktop, le sidebar sticky rend ce choix acceptable. Sur mobile, comme le sidebar passe après l'article, le CTA arrive lui aussi tout en bas — jusqu'à ~8 000 px sur `/aspirateur-professionnel/`.

**Recommandation :** garder l'affiliation secondaire, mais prévoir un handoff éditorial contextuel ou un CTA de poursuite après la réponse initiale / le tableau principal, sans transformer la page en landing commerciale.

## P1 — Comparatifs trop textuels et visuellement homogènes

Les 10 routes ont `imageCount = 0`.

Ce n'est pas un défaut en soi au regard de `DESIGN.md`, qui privilégie l'éditorial technique. Mais sur des pages de comparaison de produits, l'absence totale de repères visuels combinée à la répétition `answer-box → tableau → H2 → texte → sources` rend les pages visuellement plus semblables que leurs nouvelles logiques éditoriales ne le sont réellement.

La bonne correction n'est pas d'ajouter des images décoratives. Il serait plus utile d'introduire des modules de décision propres à l'intention :

- classe M : matrice mobilité × volume × décolmatage ;
- sans fil : plateforme batterie × classe × déclenchement ;
- puissant : débit vs dépression + avertissement sur le point de mesure ;
- industriel : process / cycle de service / matière ;
- eau & poussière : sec / humide / vidange / protection filtre ;
- petit format : encombrement / masse / cuve plutôt qu'un simple tableau produit.

## P2 — Focus clavier encore générique

Sur les pages article, le premier lien testé conserve essentiellement le focus navigateur (`outline: auto 1px`). Le système de focus renforcé à `3px` existe dans `brand-pages.css`, mais uniquement sous `.brand-page`.

Ce n'est pas un blocage équivalent au menu mobile, mais il serait préférable de généraliser un focus visible au design system global plutôt que de le résoudre cluster par cluster.

## Ce qui fonctionne bien

### Desktop

- aucune page desktop ne déborde horizontalement ;
- le layout `contenu + sidebar sticky` fonctionne bien ;
- les `answer-box` donnent un point d'entrée rapide et cohérent ;
- les H1 sont informatifs et non décoratifs ;
- l'affiliation reste secondaire ;
- les sources sont visibles dans le contenu ;
- aucun pattern de score pseudo-scientifique n'est remis en scène visuellement ;
- le dropdown `Comparatifs` fonctionne au hover sur desktop ;
- aucun target de sommaire cassé ;
- aucune erreur JS/console relevée pendant les captures.

### Hub `/comparatifs/`

Le hub est propre, lisible et cohérent. Les 9 cartes expliquent maintenant leur rôle via une ligne de contexte (`usage et contrainte`, `autonomie et classe`, `process`, etc.), ce qui reflète bien le nouveau découpage sémantique.

Le hub reste volontairement sobre. Une différenciation légère par type de décision pourrait améliorer la lecture, mais ce n'est pas un blocker.

## Priorité de correction recommandée

1. **P0 — rendre la navigation mobile réellement fonctionnelle sur toutes les pages, pas uniquement `.brand-page`.**
2. **P0 — généraliser le comportement responsive de `.table-wrap` aux comparatifs et supprimer tout overflow de page.**
3. **P1 — placer une TOC repliable avant l'article sur mobile/tablette.**
4. **P1 — améliorer la scanabilité des tableaux, avec choix entre scroll contrôlé et reflow selon le type de données.**
5. **P1 — rendre le CTA/handoff utile avant la fin de très longues pages mobiles.**
6. **P1 — ajouter des modules de décision spécifiques aux intentions plutôt que des visuels décoratifs.**
7. **P2 — généraliser les états `:focus-visible` au design system global.**

## Etat d'indexation

Toutes les pages restent volontairement en `noindex, follow`.

## Artefact Playwright

Run : `Visual design review — comparisons`, 20 captures + `report.json`.

Le gate échoue pour les raisons fonctionnelles documentées ci-dessus ; l'échec est donc considéré comme un résultat valide du design review, pas comme une erreur d'infrastructure.
