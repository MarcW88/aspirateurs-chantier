---
name: brand-editorial-publish-gate
description: Gate éditorial final obligatoire pour les pages /marques/ de aspirateurs-chantier.fr. Évalue l'intention, la valeur originale, les preuves, la confiance/E-E-A-T, la qualité GEO, la pertinence métier chantier, le ton français, les signaux de contenu générique ou AI-slop, le SEO éditorial et la préparation à la publication. Ne réécrit pas automatiquement une page en échec.
---

# Brand Editorial Publish Gate — Aspirateurs de chantier

## Rôle

Ce skill est la dernière barrière éditoriale avant publication ou indexation d'une page sous `/marques/` sur aspirateurs-chantier.fr.

Il ne sert pas à produire davantage de texte. Il sert à décider si la page mérite d'être publiée.

Une page `FAIL` reste en `noindex, follow` et retourne uniquement vers la phase de correction concernée. Une page ne peut devenir indexable qu'après `PASS` de ce gate et validation humaine explicite.

## Principe central

Évaluer la page comme un lecteur qui doit choisir un aspirateur pour un atelier, une rénovation ou un chantier — pas comme un livrable SEO.

La page doit aider à comprendre une marque, ses gammes, ses compromis et ses usages sans expliquer sa propre stratégie éditoriale. Le texte visible ne doit pas parler de « hub », de « maillage », de « contenu », de « SEO », de « GEO », d'« intention de recherche », de « workflow éditorial » ou de la manière dont la page a été construite, sauf lorsqu'une information méthodologique est réellement utile au lecteur, par exemple pour préciser qu'une analyse repose sur de la documentation et non sur un test physique.

La présence de H2, tableaux, liens internes ou mots-clés n'est jamais une preuve de qualité en soi.

---

# Entrées obligatoires

Lire avant l'audit :

- `brand-workflow.config.yaml` ;
- `.agents/skills/brand-content-workflow/SKILL.md` ;
- la page cible complète ;
- sa source éditoriale dans `_generate_brands.py` ;
- les données associées dans `.content/brands/<marque>.yaml` ;
- les pages voisines dans `/marques/`, `/modeles/`, `/comparatifs/`, `/guides/` et `/usages/` susceptibles de chevaucher la même décision ;
- les sources primaires utilisées pour les affirmations susceptibles d'évoluer.

Réutiliser, lorsqu'ils existent dans le repo, les skills pertinents. Ne jamais supposer qu'un skill absent est disponible.

Architecture actuelle du site :

- `/marques/` : directory marques ;
- `/marques/<marque>/` : `BRAND_HUB` ;
- `/modeles/` : pages modèles ;
- `/comparatifs/` : arbitrages multi-produits ;
- `/guides/` : explications techniques ;
- `/usages/` : choix par contexte d'utilisation.

Le gate doit respecter cette séparation. Une page marque ne doit pas devenir une fiche modèle détaillée, un guide complet sur les classes de poussières ou un classement multi-marques.

---

# Gate 0 — Contrat de page

Identifier avant toute évaluation :

- type : `DIRECTORY` ou `BRAND_HUB` dans l'architecture actuelle ;
- question ou décision principale du lecteur ;
- ce que cette URL apporte que les pages modèles, comparatifs, guides et usages n'apportent pas ;
- niveau de preuve disponible : documentation fabricant, normes ou sources institutionnelles, sources tierces fiables, retours utilisateurs sourcés, test réel documenté.

Un `BRAND_HUB` doit pouvoir être résumé ainsi :

> Comprendre comment la gamme de la marque est structurée, quels modèles/familles sont actuels, quelles technologies et compatibilités comptent, où sont les limites et pour quels usages la marque est ou n'est pas cohérente.

FAIL si le rôle ne peut pas être formulé clairement ou si la page chevauche essentiellement un comparatif, un guide ou une fiche modèle existante.

---

# Gate 1 — Intention et pertinence

PASS lorsque :

- l'information attendue arrive tôt ;
- la différence de positionnement de la marque est compréhensible rapidement ;
- chaque grande section répond à une question réelle du lecteur ou modifie une décision ;
- la page reste centrée sur la marque et sa gamme ;
- les caractéristiques techniques sont expliquées par leurs conséquences pratiques ;
- les renvois vers `/modeles/`, `/comparatifs/`, `/guides/` et `/usages/` servent de prochaines étapes naturelles.

FAIL lorsque :

- le texte dérive vers un guide général « comment choisir un aspirateur » ;
- il reproduit un comparatif complet entre marques ;
- il devient une fiche constructeur exhaustive ;
- une section existe uniquement pour placer un mot-clé, un lien ou un sous-titre.

Questions de contrôle :

1. Que comprend ou décide le lecteur après cette section ?
2. Si la section disparaît, la page perd-elle réellement de la valeur ?
3. Le passage parle-t-il du besoin du lecteur ou du travail de l'éditeur ?

Tout métadiscours éditorial inutile dans le contenu utilisateur est un blocker.

---

# Gate 2 — Valeur originale et utilité

Appliquer le principe :

> La page doit rester utile si tous les liens affiliés disparaissent.

PASS lorsque la page apporte une interprétation au-delà des fiches fabricant, notamment :

- différence réelle entre gamme grand public, atelier et professionnelle ;
- conséquence d'une classe L, M ou H lorsque cette classe est réellement documentée ;
- impact du décolmatage automatique sur un usage avec poussières fines ;
- intérêt ou limite d'une prise asservie ;
- compatibilité flexible / raccord / outil ;
- implications d'une plateforme batterie ;
- différence entre volume brut, net et eau lorsque le fabricant les distingue ;
- compromis mobilité / capacité / filtration / accessoires / consommables ;
- position d'un modèle actuel face à une génération précédente ;
- alternative pertinente avec raison explicite.

FAIL si la page est essentiellement :

- une reformulation de fiches officielles ;
- un catalogue de modèles ;
- une liste générique d'avantages/inconvénients ;
- une succession de tableaux sans interprétation.

Ne jamais inventer une expérience, une mesure, un consensus utilisateur, un niveau d'aspiration ou une précision non sourcée pour créer artificiellement de la valeur.

---

# Gate 3 — Preuves et factualité

Classer les affirmations importantes :

- `VERIFIED` : source primaire ou documentation officielle ;
- `SUPPORTED` : source fiable mais indirecte ;
- `INFERRED` : interprétation éditoriale raisonnable à partir de faits vérifiés ;
- `UNKNOWN` : non vérifié ;
- `OUTDATED` : ancien ou non applicable ;
- `CONTRADICTED` : contredit par une meilleure source.

PASS lorsque les éléments décisionnels sont vérifiés ou correctement qualifiés.

## Contrôles métier obligatoires

### Classes L / M / H

- Ne jamais déduire une classe L, M ou H à partir des watts, Air Watts, débit, dépression, présence d'un filtre HEPA ou formulation marketing.
- Une classe d'aspirateur doit être explicitement documentée pour la référence concernée.
- Ne pas réduire L/M/H à une simple taille de particule.
- Ne pas présenter une classe comme suffisante pour n'importe quelle poussière : le choix dépend du risque, du matériau, de l'opération et des exigences applicables.

### HEPA vs classe H

- Ne jamais confondre un filtre HEPA H13/H14 avec un aspirateur de classe H.
- Les performances d'un filtre selon EN 1822 ne prouvent pas à elles seules la conformité de l'aspirateur complet à une classe de poussière selon EN/IEC 60335-2-69.

### Débit, dépression et puissance

- Les watts électriques ne sont pas une mesure directe de la puissance d'aspiration.
- Débit d'air et dépression doivent être comparés avec unités et contexte de mesure compatibles.
- Ne pas présenter comme équivalents un chiffre à la turbine et un chiffre mesuré à l'extrémité du flexible ou de l'outil.
- Les conversions d'unités doivent être correctes.

### Cuve et capacité

- Distinguer capacité brute, capacité nette poussière et capacité eau lorsque le fabricant publie plusieurs valeurs.
- Ne pas transformer une capacité nominale en volume utile sans preuve.

### Prise asservie et charge outil

- Vérifier la présence réelle de la prise sur la référence et le marché concernés.
- La puissance admissible de l'outil branché est spécifique au modèle / marché : ne pas généraliser.

### Décolmatage et filtration

- Distinguer nettoyage manuel, semi-automatique et automatique.
- Ne pas traiter un nom marketing de système comme une norme universelle.
- Expliquer l'effet pratique sans inventer une fréquence ou une efficacité non publiée.

### Atmosphères explosibles / ACD / ATEX / Z22

- Ne jamais assimiler automatiquement `ACD`, antistatique ou « poussières combustibles » à une certification ATEX ou à une aptitude universelle en zone 22.
- Toute aptitude à une zone ou un risque spécifique doit être vérifiée sur la référence précise.

### Poussières dangereuses

Pour amiante, silice cristalline, plomb ou autres poussières à risque :

- privilégier fabricant + source institutionnelle ou normative ;
- ne pas donner de raccourci du type « prenez simplement un classe H/M » ;
- signaler que la méthode de travail, les équipements et les règles applicables comptent aussi.

### Statut produit et disponibilité

- Distinguer modèle actuel, génération précédente, discontinué et disponibilité dépendante du marché.
- Ne pas exposer les codes internes (`CURRENT`, `PREVIOUS_GENERATION`, etc.) dans le texte visible lorsque des formulations naturelles suffisent.

FAIL si une affirmation importante reste `UNKNOWN`, `OUTDATED` ou `CONTRADICTED` sans qualification claire.

---

# Gate 4 — Trust / E-E-A-T observable

Ne pas fabriquer de signaux d'autorité.

Évaluer uniquement des éléments observables :

- responsabilité éditoriale identifiable au niveau du site ou de la page ;
- sources importantes traçables ;
- niveau de preuve honnête ;
- affiliation transparente ;
- limites aussi visibles que bénéfices ;
- analyse documentaire jamais présentée comme un test physique ;
- expérience utilisateur tierce jamais transformée en expérience propre ;
- recommandations fondées sur des critères compréhensibles ;
- précautions renforcées sur les sujets de sécurité et poussières dangereuses.

Une phrase méthodologique sobre est acceptable, par exemple pour préciser que les performances citées sont celles du fabricant. Elle ne doit pas devenir un paragraphe d'auto-justification répété mécaniquement sur toutes les pages.

FAIL en cas de faux test, fausse expérience, autorité fabriquée ou méthodologie trompeuse.

---

# Gate 5 — GEO / qualité des entités

Le GEO ne justifie ni FAQ artificielle ni répétition de définitions.

PASS lorsque :

- marque, gamme, familles et modèles sont nommés sans ambiguïté ;
- les relations utiles sont explicites : `marque -> gamme`, `gamme -> modèle`, `modèle -> classe`, `modèle -> technologie`, `modèle -> usage`, `modèle -> plateforme batterie`, `accessoire -> compatibilité`, `marque -> alternative` ;
- les distinctions entre générations sont claires ;
- les notions potentiellement ambiguës sont précisées : classe M, HEPA, AFC/Tact/InfiniClean, prise asservie, débit, dépression, ACD, antistatique ;
- les phrases importantes restent compréhensibles hors contexte immédiat ;
- faits et conséquences sont reliés explicitement.

FAIL si l'optimisation GEO produit du texte artificiel, télégraphique, répétitif ou écrit pour un moteur plutôt que pour une personne.

---

# Gate 6 — Ton, registre et pertinence éditoriale

Voix cible pour aspirateurs-chantier.fr :

- français naturel ;
- média pratique spécialisé atelier / rénovation / chantier ;
- précis, concret et sobre ;
- technique quand nécessaire, mais explicatif ;
- compétent sans posture d'expert auto-proclamé ;
- utile à quelqu'un qui doit choisir un aspirateur en fonction d'une poussière, d'un outil, d'un volume de travail et d'un niveau de mobilité ;
- ni discours de consultant SEO, ni brochure fabricant, ni catalogue marchand.

FAIL notamment pour :

- « cette page doit », « ce hub », « le maillage », « pour le SEO/GEO » ;
- commentaires destinés au propriétaire du site ;
- codes éditoriaux ou statuts internes visibles sans utilité lecteur ;
- superlatifs promotionnels sans critères ;
- abstractions vagues ;
- transitions de remplissage ;
- répétition mécanique du même patron entre toutes les marques.

Préférer une conséquence de chantier concrète à une formule abstraite.

---

# Gate 7 — Anti-AI-slop et naturalité

Rechercher notamment :

- introductions qui reformulent le H1 ;
- paragraphes applicables à n'importe quelle marque ;
- structures strictement identiques d'une marque à l'autre ;
- séries systématiques de trois ou quatre points sans raison ;
- symétrie artificielle forces / limites ;
- surusage de « cohérent », « pertinent », « essentiel », « clé », « se distingue », « écosystème », « workflow » ;
- conclusions qui résument sans aider à décider ;
- listes créées uniquement pour donner une impression de structure ;
- phrases de prudence répétées mot pour mot sur toutes les pages ;
- jargon technique accumulé sans conséquence pratique.

La correction doit préserver les faits, l'intention, les liens utiles et le niveau de preuve. Elle ne doit jamais ajouter de faux détails pour rendre le texte « plus humain ».

FAIL si des signaux `HIGH` restent dans le corps principal.

---

# Gate 8 — SEO éditorial

Contrôler sans quota artificiel :

- title, H1 et sujet principal cohérents ;
- réponse alignée sur l'intention ;
- H2/H3 correspondant à de vrais sous-problèmes ;
- absence de keyword stuffing ;
- absence de section créée uniquement pour un synonyme ;
- ancres internes descriptives et contextuelles ;
- liens vers modèles, comparatifs, guides et usages réellement utiles ;
- risque de cannibalisation traité ;
- données structurées cohérentes avec le contenu visible ;
- canonical, robots et métadonnées corrects.

Ne jamais imposer un minimum de mots, de H2, de tableaux ou de liens internes comme preuve de qualité éditoriale. Les seuils techniques du `brand-content-workflow` servent de garde-fous de production, pas de verdict de publication.

---

# Gate 9 — Fit par type de page

## DIRECTORY `/marques/`

Le lecteur doit comprendre les différences générales entre marques et savoir où poursuivre. Ne pas transformer le directory en classement exhaustif ou en répétition des hubs.

## BRAND_HUB `/marques/<marque>/`

La page doit expliquer :

- logique de gamme ;
- familles actuelles ;
- générations importantes ;
- séparation grand public / pro lorsqu'elle existe ;
- technologies réellement différenciantes ;
- compatibilités d'outils, flexibles, batteries ou coffrets si elles changent l'achat ;
- classes de poussière uniquement lorsqu'elles sont vérifiées ;
- limites qui changent le choix ;
- usages pour lesquels la marque est cohérente ou moins adaptée ;
- prochaines étapes vers modèles, comparatifs, guides ou usages.

Elle ne doit pas expliquer qu'elle « sert de hub ».

## Frontière avec `/modeles/`

Les caractéristiques détaillées d'une référence précise, son avis et son adéquation à un besoin particulier doivent être approfondis sur la page modèle lorsqu'elle existe.

## Frontière avec `/comparatifs/`

Les classements multi-marques, scores et arbitrages exhaustifs appartiennent aux comparatifs.

## Frontière avec `/guides/`

Les explications générales sur classes L/M/H, HEPA, débit, dépression, décolmatage ou prise asservie appartiennent aux guides. La page marque n'en reprend que ce qui est nécessaire pour comprendre la gamme.

---

# Gate 10 — Publication

Statuts possibles :

- `PASS`
- `FAIL`

Aucun score moyen ne compense un blocker.

## Blockers absolus

- faux test ou fausse expérience ;
- affirmation importante non vérifiée présentée comme certaine ;
- classe L/M/H déduite sans preuve ;
- confusion HEPA H13/H14 avec classe H ;
- conseil dangereux ou simpliste sur amiante, silice ou poussières à risque ;
- ACD/ATEX/Z22 confondus ;
- métadiscours éditorial manifeste dans le contenu utilisateur ;
- contenu essentiellement dérivé d'un marchand/fabricant sans valeur ajoutée ;
- cannibalisation forte non résolue ;
- intention principale non satisfaite ;
- signaux anti-AI-slop `HIGH` non corrigés ;
- page indexable avant validation humaine explicite.

## Output obligatoire

```md
# Brand editorial publish gate

URL: ...
Page type: DIRECTORY | BRAND_HUB
Status: PASS | FAIL

## Blockers
- ...

## Gate results
- Intent & relevance: PASS | FAIL
- Original value: PASS | FAIL
- Evidence & factuality: PASS | FAIL
- Trust / E-E-A-T: PASS | FAIL
- GEO / entities: PASS | FAIL
- Tone & editorial relevance: PASS | FAIL
- Anti-AI-slop: PASS | FAIL
- SEO editorial: PASS | FAIL
- Page-type fit: PASS | FAIL

## Chantier-specific checks
- Dust class L/M/H: PASS | FAIL | N/A
- HEPA vs whole-vacuum class: PASS | FAIL | N/A
- Airflow / vacuum / watts: PASS | FAIL | N/A
- Tank capacity semantics: PASS | FAIL | N/A
- Tool socket / compatibility: PASS | FAIL | N/A
- Filter cleaning terminology: PASS | FAIL | N/A
- ACD / ATEX / Z22: PASS | FAIL | N/A
- Hazardous dust safety: PASS | FAIL | N/A
- Current model / market status: PASS | FAIL | N/A

## Required corrections
1. ...

## Residual risks
- ...

## Publication decision
KEEP NOINDEX | READY FOR HUMAN VALIDATION
```

Un `FAIL` ne déclenche pas automatiquement une réécriture complète. Corriger uniquement les gates en échec, puis relancer le publish gate.

## Règle d'indexation du projet

Le site et les pages marques sont actuellement en `noindex, follow`. Un `PASS` signifie uniquement `READY FOR HUMAN VALIDATION` ; il ne retire jamais automatiquement le `noindex`.
