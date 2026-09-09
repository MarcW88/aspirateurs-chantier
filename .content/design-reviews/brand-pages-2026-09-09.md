# Design review — pages marques — 09/09/2026

## Scope

Review limité à :

- `/marques/`
- `/marques/bosch/`
- `/marques/karcher/`
- `/marques/makita/`
- `/marques/festool/`
- `/marques/dewalt/`
- `/marques/parkside/`
- `/marques/nilfisk/`
- `/marques/mirka/`

Aucun comparatif, guide, usage ou modèle n'est évalué ici, sauf lorsqu'un composant global partagé explique directement un problème visible sur ces pages.

## Méthode

- skill : `.agents/skills/site-design-review/SKILL.md`
- règles projet : `DESIGN.md`
- Playwright 1.63.0 / Chromium headless
- desktop : 1440 × 1000
- mobile : 390 × 844
- 18 captures pleine page + états navigation
- rapport machine : `.artifacts/design-review/brands/report.json`
- run GitHub Actions : `34369415673`
- artifact : `brand-design-review` (`10111281544`, rétention 14 jours)

Le rapport automatique sert de diagnostic. Les décisions ci-dessous viennent également de l'inspection visuelle des captures.

## Verdict

**Le socle desktop est cohérent et crédible, mais les pages marques ne sont pas encore visuellement validables en l'état.** Le principal blocker est fonctionnel : sur mobile, le bouton burger apparaît mais n'ouvre aucune navigation. Les pages individuelles souffrent aussi d'un sommaire mobile placé après l'intégralité du contenu, tandis que Bosch présente un débordement horizontal sur un tableau.

Le système visuel est sobre et évite beaucoup de conventions génériques décoratives, mais les huit pages restent presque entièrement textuelles et utilisent le même vocabulaire de composants. Leur contenu éditorial est désormais différencié ; leur expression visuelle l'est beaucoup moins.

## Ce qui fonctionne

1. **Hiérarchie desktop claire.** Hero compact, H1, lead, date de vérification et answer-box permettent de comprendre rapidement l'angle de chaque page.
2. **Sidebar desktop utile.** Les pages individuelles ont une sidebar sticky de 260 px ; tous les liens de sommaire correspondent aux vrais H2 et aucun target cassé n'a été détecté.
3. **Aucun overflow desktop.** Les neuf routes restent dans les 1440 px et aucun débordement horizontal global n'est détecté.
4. **Affiliation discrète.** Les huit pages individuelles affichent l'encadré d'affiliation sans multiplier les CTA commerciaux dans le corps de page.
5. **Direction sobre.** Pas de gradients génériques, glows, glassmorphism, faux scores ou répétition agressive de boutons d'achat. Le bleu/orange et les typographies techniques restent cohérents avec le positionnement du site.

## Problèmes prioritaires

| Sévérité | Emplacement | Preuve | Impact | Correction recommandée |
|---|---|---|---|---|
| **Bloquant** | Header mobile, toutes les pages marques | À 390 px, `.site-nav` est `display:none`, le burger est visible, mais après clic Playwright mesure `mobileMenuVisibleAfterClick:false` et aucun `aria-expanded` n'est présent. La capture `mobile/marques--burger-clicked.png` reste identique côté navigation. | Le lecteur mobile perd l'accès à la navigation principale. C'est un défaut fonctionnel et d'accessibilité, pas seulement visuel. | Implémenter un vrai menu mobile : état ouvert/fermé, `aria-expanded`, fermeture Escape/clic extérieur, focus management et liens accessibles au clavier. |
| **Majeur** | Sidebar / sommaire mobile des 8 pages individuelles | À `max-width:1024px`, la sidebar passe en `position:static` après `<article>`. Playwright la mesure à ~3956–7669 px du haut selon la page. | Le sommaire n'aide plus à naviguer : il n'apparaît qu'après avoir lu tout l'article. L'affiliation et le CTA sont également rejetés très bas. | Sur mobile, remonter le sommaire avant le contenu, idéalement sous forme de disclosure/collapsible compact. Garder affiliation/CTA plus bas si souhaité. |
| **Majeur** | Tableaux techniques, surtout Bosch mobile | Bosch mobile : page `scrollWidth=431` pour `clientWidth=390`. Un tableau mesure 407 px dans un parent de 342 px (`exceedsParent:true`, `exceedsViewport:true`). Les tableaux n'ont pas de traitement visuel fort et les colonnes sont comprimées sur petit écran. | Perte de lisibilité des données et scroll horizontal de toute la page. Les tableaux sont pourtant une composante centrale de la proposition de valeur technique. | Donner à `.table-wrap` un vrai comportement responsive (`overflow-x:auto`, containment), styliser `th/td`, et envisager un pattern mobile spécifique pour les tableaux à 4–5 colonnes. |
| **Majeur** | Expression visuelle des pages Bosch, Kärcher, Makita, Festool, DeWalt, Parkside, Nilfisk, Mirka | Playwright détecte `imageCount:0` sur toutes les pages. Les captures montrent le même rythme hero → answer-box → texte/H2 → tableau éventuel → sources → related-box → sidebar. | Les contenus sont différents mais la perception reste très templatisée et textuelle. Pour un site de choix produit, l'absence totale de repères visuels réduit l'identification des gammes et modèles. | Ne pas créer une skin couleur par marque. Ajouter plutôt 1–2 modules utiles et contextualisés : photo produit sourcée, schéma de gamme, carte d'écosystème, strip de références ou visuel de compatibilité selon la marque. |
| **Majeur accessibilité** | Métadonnées claires et footer | Le token `--color-text-light:#8C9BAA` sur blanc donne ~2,84:1, utilisé sur du petit texte. Le footer utilise notamment du blanc à 40 % (~3,81:1) et 25 % (~2,24:1) sur `#0F1923`. | Plusieurs petits textes restent sous le seuil WCAG AA de 4,5:1, particulièrement les métadonnées, labels et mentions de footer. | Rehausser les couleurs muted/light pour le petit texte et réserver les niveaux très faibles aux éléments réellement décoratifs/non essentiels. |
| **Mineur** | Corps desktop des pages individuelles | `.content-main` mesure 852 px et les paragraphes occupent cette largeur complète. Visuellement, certaines lignes deviennent longues, surtout dans les pages très textuelles. | Fatigue de lecture sur les longs articles et aspect plus « documentation brute » qu'éditorial technique. | Limiter la largeur des paragraphes à ~70–80 caractères / ~720–760 px, tout en laissant tableaux et modules techniques utiliser la largeur disponible. |
| **Mineur** | Focus / navigation clavier | Le projet ne définit pas de système `:focus-visible` cohérent. Le test obtient essentiellement le focus navigateur par défaut, avec un résultat déjà différent sur le hub mobile. Les dropdowns desktop sont pilotés par `:hover`. | Expérience clavier fragile et peu intentionnelle. | Ajouter un focus visible commun et `:focus-within` sur les dropdowns ; tester l'ordre de tabulation et l'accès aux sous-liens. |

## Signaux de design générique réellement constatés

Le site n'accumule pas les clichés visuels typiques (gradients, cartes 3×3, glows, badges décoratifs). Le signal générique vient plutôt de la **répétition du même squelette visuel** sur toutes les pages : même hero, même answer-box bleue, même colonne texte, même sidebar, même bloc sources et même related-box.

Ce n'est pas un problème de cohérence du design system. Le problème est que les spécificités éditoriales désormais fortes des marques ne sont pas encore traduites en composants de décision propres au sujet. Mirka devrait visuellement faire comprendre le workflow ponçage ; Bosch les trois univers et deux plateformes 18 V ; Kärcher WD vs NT ; Festool l'écosystème CLEANTEC/Systainer, etc.

## Mobile et accessibilité

### Vérifié

- les neuf routes répondent en HTTP 200 ;
- aucun target de sommaire cassé ;
- aucun H2/H3 sans ID sur les pages individuelles ;
- pas d'overflow global sur 8/9 routes mobiles ;
- Bosch est la seule route avec overflow horizontal détecté ;
- menu desktop Marques visible au hover ;
- burger mobile visible mais non fonctionnel ;
- sidebar correctement sticky en desktop et correctement remise dans le flux en mobile, mais à un mauvais emplacement UX ;
- aucun visuel `<img>` sur les pages auditées.

### Limite

Le workflow vérifie les états visuels et plusieurs mesures DOM mais ne remplace pas un audit WCAG exhaustif avec lecteur d'écran. Les ratios de contraste signalés ci-dessus proviennent des couleurs CSS effectivement utilisées.

## Ordre de correction

1. **Rendre la navigation mobile réellement fonctionnelle.**
2. **Repositionner le sommaire mobile avant le contenu.**
3. **Créer un vrai système de tableaux responsive et corriger l'overflow Bosch.**
4. **Ajouter des repères visuels utiles et spécifiques à chaque univers de marque, sans transformer les pages en catalogues.**
5. **Corriger les contrastes faibles et formaliser les focus clavier.**
6. **Affiner la largeur de lecture et, ensuite seulement, les détails cosmétiques.**

## Décision

**FAIL — DESIGN FIXES REQUIRED — KEEP_NOINDEX**

La structure éditoriale et le rendu desktop constituent une bonne base. La navigation mobile bloquante empêche cependant de considérer le cluster marques comme visuellement validé.
