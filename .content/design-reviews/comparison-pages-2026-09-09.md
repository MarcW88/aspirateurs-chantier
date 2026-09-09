# Design review — pages comparatifs — 2026-09-09

## Scope

Review Playwright du cluster comparatifs : hub `/comparatifs/` + 9 pages comparatives, aux viewports desktop `1440×1000` et mobile `390×844`.

## Verdict final

**PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX**

Le premier passage avait échoué sur des problèmes mobiles réels. Après correction, le run Playwright produit 20 captures et passe le gate renforcé sur l'ensemble du cluster. Les correctifs sont intégrés à la génération canonique ; ils ne reposent donc pas sur des patches HTML isolés.

## Baseline avant correction

Le premier review avait relevé : menu burger non fonctionnel ; overflow horizontal sur 6 pages mobiles ; sommaire après l'article jusqu'à ~8 000 px sur `/aspirateur-professionnel/` ; tableaux trop comprimés ; handoff inaccessible avant la fin de lecture ; homogénéité visuelle ; focus navigateur par défaut.

Le verdict initial était `FAIL — DESIGN FIXES REQUIRED — KEEP_NOINDEX`.

## Corrections validées

### Navigation mobile

La couche comparatifs gère l'ouverture/fermeture, `aria-controls`, `aria-expanded`, Escape, fermeture après activation d'un lien et retour du focus. Le Playwright confirme que le burger ouvre réellement la navigation sur le hub.

### Aucun overflow global

Les tableaux restent larges lorsque la donnée le justifie, mais scrollent dans leur propre `.table-wrap` / `.data-table-wrap`. Sur les 10 routes mobiles finales : `clientWidth = 390 px`, `scrollWidth = 390 px`, `horizontalOverflow = false`.

### Sommaire mobile utile

Sur les 9 pages article, la TOC est déplacée avant le contenu à `max-width:1024px` et devient repliable. Le gate vérifie `tocBeforeArticle = true`.

### Tableaux plus scannables

Largeur minimale cohérente, scroll horizontal local, affordance `Glisser horizontalement pour comparer →`, en-têtes plus lisibles, alternance de lignes et hiérarchie de la première colonne. Les tableaux restent des tableaux et ne sont pas convertis artificiellement en cartes e-commerce.

### Handoff mobile

Chaque page article reçoit exactement un handoff avant la lecture longue. Si la sidebar a déjà un CTA, il est réutilisé. `/aspirateur-professionnel/` utilise un handoff éditorial vers le guide de choix plutôt qu'un CTA commercial inventé.

### Modules de décision spécifiques

Chaque comparatif possède exactement un module visuel fonctionnel après l'answer box :

- meilleur : poussière → mode de travail → volume → comparatif spécialisé ;
- eau/poussière : sec → liquide → mixte → risque ;
- sans fil : plateforme → classe → déclenchement → autonomie ;
- sans sac : conception → déchets → protection filtre ;
- puissant : débit → dépression → point de mesure → usage ;
- professionnel : risque → mobilité → continuité → écosystème ;
- industriel : matière → cycle de service → mobilité → sécurité ;
- classe M : certification → mobilité → décolmatage → volume ;
- petit format : gabarit → masse → cuve utile → fonction.

### Focus clavier

Le focus visible est renforcé à `3 px`. Le gate exige au minimum `2 px`.

## Gate Playwright

Le dernier run vert avant finalisation vérifie : 20 page/viewports ; HTTP 200 ; aucun overflow global ; aucun target TOC cassé ; aucune erreur console/page ; wrappers responsive sur tous les tableaux ; un module de décision par article ; TOC avant article en mobile ; un handoff mobile ; focus renforcé ; burger mobile et dropdown Comparatifs desktop fonctionnels.

Le workflow marques est également resté vert après modification du runner partagé.

## Ce qui reste volontairement inchangé

- identité sobre, technique et éditoriale ;
- aucune photo décorative ajoutée par défaut ;
- affiliation secondaire ;
- longueur éditoriale conservée lorsque le raisonnement la justifie ;
- pages toujours `noindex, follow` jusqu'à validation humaine.

## État final

**PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX**
