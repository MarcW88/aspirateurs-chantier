# Design review — pages comparatifs — 2026-09-09

## Scope

Review Playwright du cluster comparatifs :

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

## Verdict final

**PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX**

Le premier passage avait échoué sur des problèmes mobiles réels. Après correction, le run Playwright final produit 20 captures et passe le gate renforcé sur l'ensemble du cluster. Les correctifs sont intégrés à la génération canonique ; ils ne reposent donc pas sur des patches HTML isolés.

## Baseline avant correction

Le premier review avait relevé :

- menu burger visible mais non fonctionnel ;
- débordement horizontal de page sur 6 comparatifs mobiles ;
- sommaire placé après l'article sur mobile, jusqu'à ~8 000 px sur `/aspirateur-professionnel/` ;
- tableaux trop comprimés et sans affordance de scroll ;
- CTA/handoff inaccessible avant la fin de la lecture mobile ;
- pages très textuelles et visuellement homogènes ;
- focus clavier principalement laissé au style navigateur.

Le verdict initial était `FAIL — DESIGN FIXES REQUIRED — KEEP_NOINDEX`.

## Corrections validées

### 1. Navigation mobile

Une couche d'interaction dédiée aux comparatifs gère désormais :

- ouverture/fermeture du menu ;
- `aria-controls` et `aria-expanded` ;
- fermeture avec `Escape` ;
- fermeture après activation d'un lien mobile ;
- retour du focus vers le burger ;
- menu plein écran lisible sous le header.

Le Playwright final confirme sur `/comparatifs/` :

- `burgerAriaExpanded = true` après clic ;
- navigation réellement visible après clic.

### 2. Aucun overflow global sur mobile

Les tableaux restent larges quand le contenu le nécessite, mais leur largeur est maintenant contenue dans `.table-wrap` / `.data-table-wrap` avec scroll horizontal local.

Sur les 10 routes mobiles finales :

- `clientWidth = 390 px` ;
- `scrollWidth = 390 px` ;
- `horizontalOverflow = false`.

Cela corrige notamment les anciens dépassements de Classe M (+153 px) et Petit format (+165 px).

### 3. Sommaire mobile avant l'article

Sur les 9 pages article, le sommaire est désormais déplacé avant le contenu à `max-width:1024px` et rendu repliable.

Le gate vérifie explicitement `tocBeforeArticle = true` pour les 9 pages mobiles.

Le sommaire redevient donc un outil de navigation au lieu d'apparaître après plusieurs milliers de pixels de lecture.

### 4. Tableaux plus scannables

La couche comparatifs ajoute :

- largeur minimale cohérente plutôt que compression forcée ;
- scroll horizontal contrôlé ;
- indication mobile `Glisser horizontalement pour comparer →` ;
- en-têtes sombres plus lisibles ;
- alternance légère des lignes ;
- état hover desktop ;
- première colonne davantage hiérarchisée.

Les tableaux restent des tableaux lorsque la donnée s'y prête ; ils ne sont pas artificiellement transformés en cartes e-commerce.

### 5. Handoff mobile avant la lecture longue

Chaque page article reçoit un seul handoff mobile avant le contenu long.

Lorsque la sidebar possède déjà un CTA, celui-ci est réutilisé. `/aspirateur-professionnel/`, qui n'en possédait pas, utilise volontairement un handoff éditorial vers le guide de choix plutôt qu'un bouton commercial inventé.

Le gate final vérifie `mobileHandoffCount = 1` sur les 9 pages article.

### 6. Modules de décision propres aux intentions

Chaque comparatif possède désormais exactement un module visuel fonctionnel, injecté après l'answer box :

- meilleur aspirateur : poussière → mode de travail → volume → comparatif spécialisé ;
- eau/poussière : sec → liquide → usage mixte → risque ;
- sans fil : plateforme → classe → déclenchement outil → autonomie ;
- sans sac : conception → déchets → protection filtre ;
- puissant : débit → dépression → point de mesure → usage ;
- professionnel : risque → mobilité → continuité → écosystème ;
- industriel : matière → cycle de service → mobilité → sécurité ;
- classe M : certification → mobilité → décolmatage → volume ;
- petit format : gabarit → masse → cuve utile → fonction.

Ces modules différencient les pages sans créer neuf thèmes graphiques ni ajouter des images décoratives.

### 7. Focus clavier

Les comparatifs disposent maintenant d'un `:focus-visible` renforcé de `3 px`, cohérent avec la correction déjà utilisée sur les pages marques.

Le gate Playwright vérifie que le premier élément interactif testé a un outline visible d'au moins `2 px` ; le run final mesure `3 px`.

## Résultat Playwright final

`Visual design review — comparisons` : **SUCCESS**.

Le gate final vérifie notamment :

- 20 page/viewports capturés ;
- HTTP 200 ;
- aucun overflow global ;
- aucun target TOC cassé ;
- aucune erreur console/page ;
- tous les tableaux dans un wrapper responsive ;
- exactement un module de décision par page article ;
- TOC avant article en mobile ;
- exactement un handoff mobile par page article ;
- focus renforcé ;
- burger mobile fonctionnel ;
- dropdown Comparatifs desktop fonctionnel.

Le workflow visuel des pages marques a également été relancé et reste **SUCCESS**, ce qui confirme que l'évolution du runner partagé n'a pas créé de régression sur le cluster déjà corrigé.

## Ce qui reste volontairement inchangé

- L'identité globale reste sobre, technique et éditoriale.
- Les pages n'ajoutent pas de photos ou illustrations décoratives par défaut.
- L'affiliation reste secondaire.
- Les longues pages restent longues lorsque le raisonnement éditorial le justifie ; le travail a porté sur leur navigation et leur scanabilité, pas sur une réduction artificielle du contenu.
- Les comparatifs restent `noindex, follow` jusqu'à validation humaine et décision de publication.

## État final

**PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX**
