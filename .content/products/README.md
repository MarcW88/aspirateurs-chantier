# Registre produits — modules Amazon gardés

Ce dossier centralise les produits utilisés dans les modules de décision et les CTA affiliés Amazon.fr.

## Principes

1. Les caractéristiques éditoriales (`specs`, `best_for`) proviennent des fiches et comparatifs déjà vérifiés sur le site.
2. Un CTA Amazon n'est rendu que si l'ASIN de la référence exacte a été vérifié.
3. Le lien est construit sous la forme `https://www.amazon.fr/dp/ASIN/ref=nosim?tag=TRACKING_ID` à partir de `affiliate.json`.
4. Aucun prix, stock, remise ou promesse de disponibilité Amazon n'est stocké dans le dépôt.
5. Sans ASIN vérifié, le module conserve uniquement le lien vers l'analyse interne du site.
6. Les images Amazon ne sont jamais copiées ou scrapées. Une image produit ne peut être ajoutée que si sa provenance et ses droits sont explicites.
7. Les liens affiliés utilisent `rel="sponsored nofollow noopener noreferrer"`.
8. Les modules commerciaux restent secondaires : un module maximum par page, 2 à 3 produits, uniquement sur des pages de décision explicitement autorisées dans `placements.json`.

## Périmètre aspirateurs-chantier

Modules de recommandation : comparatifs sélectionnés, usages où une décision produit est réellement utile et guide général de choix.

CTA direct : uniquement sur les fiches modèles dont l'ASIN exact est vérifié. Les pages marques, hubs, accessoires, guides purement techniques et le comparatif industriel restent hors insertion automatique.

## Exécution

```bash
python apply_product_cards.py all
python validate_product_cards.py all
python apply_inline_affiliate_links.py
python validate_inline_affiliate_links.py
```

Les workflows GitHub réappliquent également les modules après les générateurs de contenu afin qu'une régénération éditoriale ne fasse pas disparaître les placements approuvés.
