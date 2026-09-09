---
name: comparison-content-workflow
description: Workflow unique de création et de réécriture des pages /comparatifs/ d'aspirateurs-chantier.fr. Orchestre principalement des skills réutilisables pour l'intention, l'audit, les preuves, le brief, la rédaction, le SEO et l'édition. La logique custom est limitée à la décision comparative et aux contraintes propres aux aspirateurs de chantier.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: MarcW88/bloc-notes-numerique/comparison-content-workflow
  orchestration_target: ">=80% existing/vendored skills"
  custom_scope: "orchestration + vacuum comparison decision logic"
---

# Comparison Content Workflow — Aspirateurs Chantier

## Rôle

C'est le **seul workflow de production** à utiliser pour créer ou réécrire une URL `/comparatifs/`.

Il orchestre des skills spécialisés plutôt que de fabriquer une méthode parallèle.

Principe central :

> **Intention → preuves → décision → brief → rédaction → review.**

Scoring, pondération, tableau, hard gate formel ou coût total détaillé sont optionnels. Ils ne sont utilisés que s'ils rendent la décision plus claire.

---

# 1. Entrées

Pour une page existante, lire d'abord le rapport récent du `comparison-analysis-workflow / AUDIT` et respecter son niveau de changement.

Lire selon pertinence :

- page cible et comparatifs voisins ;
- `comparison-workflow.config.yaml` ;
- `.content/comparisons/<slug>.json` ;
- GSC / analyse sémantique / historique ;
- SERP actuelle ;
- `/usages/`, `/marques/`, `/modeles/`, `/guides/` ;
- `.content/models/model-evidence.json` ;
- sources actuelles fabricants, manuels et sources secondaires utiles.

Ne pas refaire un audit complet si un handoff récent existe, sauf changement significatif de gamme, SERP ou données.

---

# 2. Chaîne principale — skills partagés obligatoires

## `seo-keyword`
Confirmer query/cluster, intention, format SERP, rôle unique de l'URL et risque de chevauchement.

## `jobs-to-be-done` — si pertinent
Pour professionnel, mobilité, petit format, budget, usage outil ou autre contexte réel. Traduire le job en contraintes sans inventer de persona.

## `seo-content-audit`
Pour une page existante, préserver ce qui fonctionne. Un `LIGHT_UPDATE` ne devient pas un deep rewrite sans découverte majeure documentée.

## `evidence-based-reviews`
Construire la base de preuve : specs officielles, expérience utilisateurs si nécessaire, tests indépendants nommés lorsque le jugement l'exige, hands-on seulement s'il existe réellement.

## `fact-check`
Vérifier classe, génération, fonctions, compatibilités, débit/dépression, capacité, poids, prix/disponibilité lorsqu'ils sont publiés.

## `affiliate-value`
Identifier la valeur originale : différences décisionnelles, limites, cas d'inadéquation, alternatives, coûts ou contraintes cachés pertinents. La page doit rester utile sans affiliation.

## `content-brief-authoring`
Construire le brief **avant** le draft : query, décision, scope, critères, preuves, arbitrages, angle, anti-patterns et outline spécifique.

## `content-and-copy`
Rédiger depuis le brief et les preuves : décision claire, substance, trade-offs, structure adaptée et voix naturelle.

---

# 3. Couche custom minimale — décision Aspirateurs Chantier

## 3.1 Scope / candidats

Identifier un ensemble raisonnable de produits réellement plausibles. Ne pas documenter tout le marché par principe ; ne pas omettre silencieusement un candidat évident susceptible de changer la conclusion.

## 3.2 Critères

Définir les critères **avant** la recommandation. Selon l'intention :

- classe L/M/H et niveau de risque lorsque pertinent ;
- maintien du débit / décolmatage ;
- débit et dépression avec contexte de mesure ;
- prise asservie / raccord outil ;
- antistatique ;
- capacité utile et type de cuve ;
- mobilité / poids / encombrement ;
- filaire vs batterie / plateforme / autonomie documentée ;
- flexibles, sacs, filtres et consommables ;
- eau/poussière ;
- coût de configuration si décisionnel.

## 3.3 Gates métier non négociables

- ne jamais déduire une classe L/M/H depuis un filtre HEPA, la puissance ou un débit élevé ;
- ne pas traiter AFC/Tact/InfiniClean/AUTOCLEAN comme une certification de sécurité ;
- ne pas comparer comme équivalentes des mesures prises à des points/protocoles différents sans l'expliquer ;
- ne pas confondre capacité brute, nette et eau ;
- ne pas supposer la compatibilité batterie sur la seule base du voltage ;
- ne pas transformer une fonction eau/poussière en aptitude aux poussières dangereuses ;
- ne pas publier d'autonomie réelle ou de sensation d'usage sans preuve appropriée.

## 3.4 Verdict

Le verdict doit être traçable aux critères et aux preuves. Favoriser :

- meilleur choix général **pour une situation définie** ;
- choisissez Y si votre priorité est… ;
- évitez Z si… ;
- verdict conditionnel si aucun gagnant universel n'est honnête.

## 3.5 Scoring — optionnel

N'utiliser un score que s'il clarifie les arbitrages. S'il existe : échelle stable, critères explicites, notes présentées comme jugements éditoriaux sauf mesure réelle, pas de décimales de fausse précision. L'absence de scoring n'est jamais un blocker.

## 3.6 Coût — proportionné

Comparer la configuration réellement nécessaire lorsqu'elle change la décision : batterie/chargeur, sacs/filtres, raccords ou accessoires indispensables. Ne pas imposer un TSC complexe à une page où le coût est secondaire.

---

# 4. Architecture éditoriale

Aucun template obligatoire par type de comparatif.

Interdit d'imposer :

- nombre fixe de H2/H3 ;
- nombre fixe de mots ou liens ;
- `méthode → critères → ranking → produit 1 → produit 2 → FAQ → conclusion` ;
- même longueur par produit ;
- tableau/FAQ/conclusion obligatoires ;
- sections symétriques « avantages / limites / pour qui » pour chaque machine.

Chaque section doit justifier sa présence par une question, décision, preuve ou arbitrage propre à l'URL.

---

# 5. Post-draft — skills partagés

1. `fact-check` — réextraire et corriger les claims.
2. `humanizer` — corriger structure/prose trop générique sans altérer les faits.
3. `general-writing` — clarté, précision, voix ; éditer le minimum nécessaire.
4. `anti-ai-slop` — détecter blocs interchangeables, transitions recyclées et structure clonée.
5. `seo-onpage` — title, meta, H1, headings, contenu, liens et schema honnête.
6. `seo-technical` — canonical, robots, crawlabilité, structured data et intégrité HTML lorsqu'applicable.
7. `internal-linking-audit` — router vers guides/usages/marques/modèles utiles.
8. `editorial-qa` — gate générique final.

---

# 6. Persistance

`.content/comparisons/<slug>.json` est un support méthodologique, **pas un formulaire obligatoire**.

Conserver uniquement les champs utiles, par exemple :

- intent/JTBD ;
- scope/candidats ;
- exclusions importantes ;
- critères ;
- evidence/sources ;
- recommendation logic ;
- notes de mesure/comparabilité ;
- price/configuration notes ;
- scores/weights **si utilisés** ;
- ranking **si la page utilise un ranking** ;
- research date ;
- status.

Ne jamais ajouter un champ uniquement pour satisfaire le workflow.

---

# 7. Frontières éditoriales du cluster

Le comparatif est un hub de décision. Il ne doit pas absorber le rôle des autres pages :

- `/modeles/` = évaluer une référence précise ;
- `/marques/` = comprendre gamme/écosystème d'une marque ;
- `/usages/` = expliquer le besoin non-brand et les contraintes d'une tâche ;
- `/guides/` = expliquer un critère technique ;
- `/comparatifs/` = arbitrer entre plusieurs options pour une décision donnée.

Le même modèle peut apparaître dans plusieurs comparatifs **si la logique de décision change réellement**. Réutiliser les mêmes arguments et le même classement sous une autre requête est un blocker potentiel.

---

# 8. Gate final

Une fois le draft stable, appeler :

`.agents/skills/comparison-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Résultat requis : `PASS — READY_FOR_HUMAN_VALIDATION`.

Sinon : `FAIL — KEEP_NOINDEX`.

Le gate final vérifie intention, décision, preuves, sécurité des claims métier, valeur, différenciation éditoriale, SEO et absence de faux hands-on — pas la présence d'une méthodologie chiffrée imposée.

---

# 9. Indexation

Conserver `noindex, follow` par défaut. Le workflow ne retire jamais `noindex` automatiquement.

Indexation seulement après validation machine, PUBLISH_REVIEW PASS, validation humaine explicite et instruction explicite d'indexer.

---

# 10. Orchestration 80/20

```text
PAGE EXISTANTE
  comparison-analysis-workflow / AUDIT
        ↓
seo-keyword
        ↓
jobs-to-be-done si pertinent
        ↓
seo-content-audit
        ↓
evidence-based-reviews + fact-check
        ↓
affiliate-value
        ↓
CUSTOM LÉGER : scope + critères + gates métier + logique de recommandation
        ↓
content-brief-authoring
        ↓
content-and-copy
        ↓
fact-check
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
seo-onpage + seo-technical + internal-linking-audit
        ↓
editorial-qa
        ↓
comparison-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le custom doit rester minoritaire et ne jamais réimplémenter les skills partagés.