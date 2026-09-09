---
name: brand-content-workflow
description: Workflow de production et de refonte des pages /marques/ d'aspirateurs-chantier.fr. Produit un contenu d'affiliation utile, sourcé, fact-checké, non templatisé et sans faux test. La structure éditoriale doit découler de l'intention, des preuves et des enjeux propres à chaque marque, tout en conservant le ton et le design system du site.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: bloc-notes-numeriques.fr/brand-content-workflow
---

# Brand Content Workflow — aspirateurs-chantier.fr

## Rôle

C'est le workflow de production à utiliser pour créer ou réécrire une URL sous `/marques/`.

Il reprend la logique du workflow de `bloc-notes-numeriques.fr`, mais l'adapte au marché des aspirateurs de chantier, aux sources de vérité du dépôt et au style éditorial du site.

Principe central :

> **Pas de plan avant l'intention et les preuves. Pas de claim important sans source. Pas de template éditorial par marque.**

Le but est de produire une page qui aide réellement à choisir entre des familles, systèmes et usages, pas un catalogue constructeur réécrit.

---

# 1. Entrées obligatoires

Lire :

- `brand-workflow.config.yaml` ;
- `_generate_brands.py`, source de vérité actuelle ;
- page cible et contenu existant ;
- pages sœurs `/marques/` ;
- pages `/modeles/`, `/comparatifs/`, `/guides/` et `/usages/` pertinentes ;
- `.content/brands/` et `.content/reviews/` ;
- données GSC, sémantiques ou historiques disponibles ;
- sources actuelles nécessaires à la vérification.

Pour une page existante, commencer obligatoirement par :

`.agents/skills/brand-analysis-workflow/SKILL.md` en mode `AUDIT`.

Ne pas lancer une réécriture profonde si l'audit conclut `KEEP`, `LIGHT_UPDATE`, `MERGE` ou `NOINDEX` sans raison documentée.

Ne jamais modifier uniquement le HTML généré si `_generate_brands.py` reste capable de l'écraser au prochain build.

---

# 2. Pré-analyse et récupération

Réutiliser en priorité `.agents/skills/content-recovery-and-production-workflow/SKILL.md` pour l'intention, le diagnostic de récupération, le fact-check, la valeur affiliée, le maillage, la QA éditoriale et SEO.

Lorsque les skills spécialisés cités par ce workflow sont disponibles dans l'environnement, les exécuter selon leur rôle : `search-intent`, `content-refresh`, `affiliate-value`, `fact-check`, `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-technical`, `seo-best-practices` et `editorial-qa`.

Pour une page existante :

- conserver les passages concrets et toujours valides ;
- conserver les liens utiles ;
- conserver un tableau seulement s'il réduit réellement une ambiguïté ;
- supprimer les phrases génériques recyclées entre marques ;
- ne pas remplacer une information précise par une prose plus fluide mais plus vague.

---

# 3. Intention avant architecture

Avant de proposer un plan, établir :

- requête/topic principal ;
- intention ;
- décision ou problème concret du lecteur ;
- rôle de la page marque par rapport aux fiches `/modeles/` ;
- prochaine question logique ;
- risque de cannibalisation.

Sur l'architecture actuelle, une page `/marques/<slug>/` sert surtout de `BRAND_HUB`. Elle ne doit pas refaire les fiches modèles ni les comparatifs génériques.

Exemples de vraies questions de marque :

- comment lire la gamme ;
- quelles familles sont réellement différentes ;
- quel écosystème outils/batteries/raccords/consommables est impliqué ;
- quelles technologies changent l'usage ;
- dans quels cas la marque est rationnelle ou moins adaptée ;
- vers quel modèle, comparatif ou guide poursuivre.

---

# 4. Recherche et evidence brief

La recherche précède le plan.

Construire un registre des affirmations nécessaires avec au minimum :

| Question / claim | Source | Date | Status | Utilité pour la décision |
|---|---|---|---|---|

Hiérarchie de sources :

1. fabricant, documentation ou manuel officiel ;
2. distributeur officiel ;
3. retailer fiable pour disponibilité ou information commerciale complémentaire ;
4. tests et médias spécialisés indépendants nommés ;
5. plusieurs sources utilisateurs lorsqu'un pattern d'expérience est réellement étudié.

Statuts : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

Ne jamais utiliser la mémoire du modèle pour combler `UNKNOWN`.

---

# 5. Claims métier à traiter avec prudence

Pour aspirateurs-chantier.fr, vérifier en priorité :

- classe de poussière L, M ou H ;
- filtre et niveau de filtration sans les confondre avec une classe de sécurité ;
- débit d'air et dépression avec le point de mesure lorsqu'il est connu ;
- décolmatage automatique ou manuel ;
- prise asservie et démarrage avec outil ;
- antistatique ;
- cuve brute/net/volume eau ;
- batteries et compatibilité réelle entre plateformes ;
- raccords et compatibilité avec les outils ;
- sacs, filtres et consommables ;
- poids, mobilité et volume ;
- statut actuel d'un modèle ou d'une génération.

Une donnée constructeur reste une donnée constructeur. Ne jamais écrire qu'un produit a été « puissant », « silencieux », « pratique » ou « efficace lors de notre usage » sans expérience documentée.

Pour les poussières potentiellement dangereuses, expliquer la différence entre familles et classes sans transformer la page en conseil réglementaire personnalisé.

---

# 6. Valeur originale avant plan

Identifier ce que la page apporte au-delà du fabricant et des marchands.

Cela peut être :

- décoder une nomenclature complexe ;
- distinguer une gamme bricolage d'une gamme professionnelle ;
- expliquer pourquoi deux modèles avec des chiffres proches n'ont pas le même rôle ;
- révéler une incompatibilité batterie ou accessoire ;
- montrer le coût réel d'un écosystème ;
- distinguer mobilité et gros volume ;
- identifier le modèle ou la famille disproportionnée pour un usage ;
- expliquer quand une autre marque est plus logique ;
- remettre les chiffres fabricant dans le contexte d'un usage précis.

Test obligatoire : **la page reste-t-elle utile si tous les liens affiliés disparaissent ?**

---

# 7. Construction libre mais justifiée du plan

Le plan est construit après l'intention, l'evidence brief et la valeur originale.

Pour chaque section :

1. quelle question du lecteur résout-elle ?
2. quelles preuves permettent de l'écrire ?
3. quelle décision améliore-t-elle ?
4. pourquoi mérite-t-elle une section autonome ?

Si les réponses sont faibles, supprimer ou fusionner.

## Interdiction de template

Ne pas imposer :

- un nombre fixe de H2/H3 ;
- l'ordre « distinction → gamme → écosystème → forces → limites → pour qui → éviter → alternatives » ;
- un tableau de gamme obligatoire ;
- une FAQ automatique ;
- un bloc « forces » ou « à éviter » obligatoire ;
- un minimum de mots ou de liens.

Deux marques peuvent partager des composants visuels sans partager la même architecture éditoriale.

Exemples :

- Bosch peut être structuré autour de la séparation DIY / Professional et des deux univers 18 V ;
- Festool peut être structuré autour du système d'aspiration connecté à l'outil, des classes et du workflow Systainer/CLEANTEC ;
- Kärcher peut être structuré autour de la différence WD / NT et du passage du nettoyage eau/poussière aux aspirateurs de sécurité.

Ces exemples sont des angles de recherche, pas des templates.

---

# 8. Ton of voice du site

La rédaction doit rester cohérente avec aspirateurs-chantier.fr :

- expert mais lisible ;
- pratique et décisionnelle ;
- sobre, sans superlatifs commerciaux inutiles ;
- directe : répondre rapidement au point central ;
- précise sur les limites ;
- capable de vulgariser une différence technique sans la déformer ;
- claire sur la provenance des données ;
- pas de jargon SEO/GEO dans la prose finale.

Éviter particulièrement :

- « excellent », « incontournable », « meilleur » sans critères ;
- transitions passe-partout répétées sur plusieurs marques ;
- « le bon produit est celui qui... » et autres phrases applicables à toute marque ;
- conclusions qui répètent l'introduction ;
- listes symétriques écrites pour remplir une structure.

---

# 9. Mise en avant et design system

Respecter l'interface du site au lieu de créer un nouveau langage visuel.

Réutiliser lorsque pertinent :

- `answer-box` pour une réponse initiale courte ;
- `table-wrap` lorsqu'un tableau réduit réellement une ambiguïté ;
- `related-box` pour la suite du parcours ;
- sidebar et sommaire ;
- encadré affiliation existant ;
- styles de liens, titres et composants de `style.css`.

Le sommaire doit refléter les vrais H2 de la page, pas une liste fixe héritée du générateur.

La cohérence visuelle ne justifie jamais un plan éditorial identique entre marques.

---

# 10. Rédaction depuis les preuves

Règles :

- chaque claim important doit être relié à une source ou présenté comme déduction ;
- aucune donnée, classe, prix, génération, compatibilité, date ou performance ne peut être inventée ;
- expliquer la conséquence pour le lecteur au lieu de paraphraser le fabricant ;
- afficher les limites aussi clairement que les avantages ;
- ne pas écrire une section uniquement pour placer un mot-clé ou un lien ;
- ne jamais simuler d'expérience utilisateur ;
- ne pas faire varier le verdict selon la commission.

La prose finale ne parle pas de SEO, GEO, maillage, intention, page type, evidence ledger ou stratégie éditoriale.

---

# 11. Fact-check post-draft

Après rédaction :

1. réextraire les claims vérifiables ;
2. comparer avec l'evidence brief ;
3. recontrôler les formulations ajoutées ;
4. corriger `OUTDATED` ou `CONTRADICTED` ;
5. qualifier ou supprimer `UNKNOWN` ;
6. s'assurer qu'une donnée fabricant n'est pas devenue une observation propre au site.

---

# 12. Finition éditoriale

Appliquer la chaîne QA du workflow de récupération et, lorsque disponibles, les passes `humanizer`, `general-writing` puis `anti-ai-slop`.

La finition peut modifier la structure si elle semble mécanique, mais elle ne peut ajouter aucun fait absent des preuves.

Contrôler particulièrement :

- même rythme sur toutes les sections ;
- rule of three artificielle ;
- intro qui reformule le H1 ;
- mêmes paragraphes de transition sur plusieurs marques ;
- headings interchangeables ;
- structure trop symétrique ;
- surpromesse commerciale.

---

# 13. Maillage

Ajouter uniquement les liens qui servent la prochaine question logique :

- modèle pertinent ;
- comparatif adapté ;
- guide technique ;
- usage ;
- autre marque lorsque la comparaison est directement utile.

Aucun quota de liens ni de destinations.

---

# 14. SEO et QA

Vérifier :

- title et H1 ;
- canonical ;
- robots ;
- breadcrumbs ;
- liens ;
- structured data honnête ;
- absence de cannibalisation ;
- cohérence entre HTML rendu et source de vérité.

Aucun nombre de mots, headings, tableaux ou liens n'est un KPI de qualité.

---

# 15. Gate final

Une fois le draft stable, appeler :

`.agents/skills/brand-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Le gate :

- exécute `python3 _validate_brands.py` ;
- recontrôle preuves, intention et claims métier ;
- compare la structure aux pages sœurs ;
- cherche l'industrialisation éditoriale ;
- vérifie le ton et le design system.

Résultat attendu :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

---

# 16. Persistance

Conserver dans `.content/brands/` ou `.content/reviews/` selon le cas :

- cadrage de l'intention ;
- research/evidence brief ;
- statut des claims ;
- sources et date de vérification ;
- valeur originale recherchée ;
- justification du plan ;
- résultat de l'audit et du `PUBLISH_REVIEW`.

Le HTML final ne doit pas être l'unique endroit où les preuves sont documentées.

---

# 17. Indexation

Par défaut, conserver `noindex, follow`.

Conditions cumulatives avant une future indexation :

1. `_validate_brands.py` sans blocker ;
2. `brand-analysis-workflow / PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 18. Résumé

```text
PAGE EXISTANTE
  brand-analysis-workflow / AUDIT
        ↓
intention + récupération
        ↓
recherche → evidence brief
        ↓
valeur originale
        ↓
PLAN PROPRE À LA MARQUE
        ↓
rédaction depuis les preuves
        ↓
fact-check post-draft
        ↓
QA éditoriale + anti-AI-slop
        ↓
maillage contextuel
        ↓
SEO technique
        ↓
brand-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le workflow orchestre la production ; il ne transforme pas les pages marques en variantes d'un même template.