# Brand pages design fixes — 09/09/2026

Scope : `/marques/` + Bosch, Kärcher, Makita, Festool, DeWalt, Parkside, Nilfisk et Mirka uniquement.

Corrections appliquées avant nouveau review visuel :

- navigation mobile fonctionnelle avec `aria-expanded`, fermeture Escape et focus sur le premier lien ;
- menu mobile rendu à partir de la navigation existante, sans second arbre de liens ;
- sommaire déplacé avant l’article sur mobile et rendu repliable ;
- tableaux confinés dans `.table-wrap` avec scroll horizontal local au lieu d’un overflow de page ;
- contraste renforcé pour les petits textes des pages marques et du footer ;
- système `:focus-visible` + `:focus-within` pour navigation clavier ;
- largeur de lecture des paragraphes limitée sans brider les tableaux ;
- ajout d’un module de décision visuel propre à chaque marque, sans fausse photo ni décoration de marque artificielle ;
- couche design appliquée en dernier par `_generate_brand_content.py` pour survivre aux futures régénérations.

Indexation : `noindex, follow` inchangé.
