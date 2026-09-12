# Requêtes d'images éditoriales

Ce dossier pilote les images éditoriales générées via Black Forest Labs (BFL / FLUX.2).

Aucune page n'obtient une image automatiquement parce qu'elle existe. La décision éditoriale est prise avec `.agents/skills/editorial-image-planner/SKILL.md`.

Le moteur ne traite que les requêtes qui ont simultanément :

- `required: true`
- `allow_ai_generation: true`
- `truth_risk: LOW`
- `status: PENDING` ou `REGENERATE`

Les statuts `NOT_NEEDED` et `BLOCKED` sont ignorés.

## Cycle

1. Décider si une image générique apporte une vraie valeur.
2. Créer `.content/image-requests/<slug>-<slot>.json`.
3. Choisir un `marker` stable déjà présent dans la source et le HTML généré, ou ajouter un commentaire dédié.
4. Le workflow GitHub valide la requête.
5. Sur `main`, il appelle BFL avec le secret GitHub `BLF_API_KEY`, exposé au script sous `BFL_API_KEY`.
6. L'image est enregistrée sous `assets/generated/`.
7. Le script insère un `<figure>` à l'emplacement prévu.
8. Le JSON passe à `GENERATED`.
9. Si une régénération de contenu retire le `<figure>`, le workflow réinsère l'image existante sans nouvel appel API.

## Présentation

Les images générées n'affichent pas de légende visible sous le visuel. Le contexte éditorial est donné par le texte de la page et l'accessibilité par l'attribut `alt`. Le template de requête ne contient donc plus de champ `caption`; les anciennes légendes sont également masquées par le design V2 pour garantir la cohérence du site.

## Garde-fous

Ne pas générer de représentation fidèle d'un modèle précis, logo, accessoire propriétaire, certification L/M/H, interface, benchmark, résultat de mesure ou faux test hands-on. Ces besoins doivent être `BLOCKED` et alimentés par une vraie photo ou une source officielle.

Par défaut, viser zéro ou une image IA par page.

## Couverture éditoriale actuelle

Le workflow a été utilisé pour neuf scènes à faible risque de vérité :

- organisation de plusieurs postes dans un atelier ;
- ponceuse raccordée à une aspiration générique ;
- ponçage de plâtre/enduit avec captage à la source ;
- atelier bois : aspiration mobile et collecte fixe ;
- nettoyage de petits gravats après retrait des gros morceaux ;
- rénovation : captage à la source pendant perçage/découpe ;
- scie portative raccordée à une aspiration ;
- prise asservie : câble d'alimentation et flexible d'aspiration ;
- entretien : inspection simple du flexible et des raccords, machine débranchée.

Les fiches modèles, pages marques, comparatifs produit, classes L/M/H, HEPA et pages de métriques restent volontairement sans image IA lorsqu'une représentation exacte ou une vraie source fabricant est préférable.

## Paramètres par défaut

- endpoint : `https://api.bfl.ai/v1/flux-2-pro-preview`
- 1024 × 672 px
- `prompt_upsampling: true`
- `seed: null`
- formats : PNG, JPEG ou WebP selon `output_path`
