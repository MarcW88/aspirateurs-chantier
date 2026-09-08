# Editorial QA — Cluster /guides/

```yaml
scope: /guides/
date: 2026-09-08
status: QA_IN_PROGRESS
human_validation_required: true
publishable: false
robots_expected: noindex,follow
```

## Routing

Les 11 guides ont été routés `NEW_CONTENT` : les pages contenaient une réponse courte et un placeholder, sans article exploitable. Aucune réécriture totale de contenu performant n’a donc été effectuée.

## Chaîne QA

| Étape | Statut | Contrôle |
|---|---|---|
| content-refresh | PASS | NEW_CONTENT justifié, contenu placeholder remplacé |
| search-intent | PASS | chaque guide répond à une question distincte et conserve un périmètre propre |
| affiliate-value | PASS | guides utiles sans lien affilié ; transitions vers comparatifs/usages quand pertinentes |
| fact-check | PASS avec garde-fous | claims normatifs limités aux sources IEC/EN, INRS et fabricants ; pas de prix ni test inventé |
| natural-writing | PASS | phrases explicatives, compromis et limites ; pas de succession de définitions génériques |
| internal-linking-audit | PASS éditorial | liens contextuels vers guides, usages, accessoires, comparatifs et modèles |
| humanizer | PASS éditorial | formulations non promotionnelles, exemples fonctionnels, nuances explicites |
| general-writing | PASS | titres orientés questions et décisions, paragraphes cohérents |
| anti-ai-slop | PASS éditorial | suppression des superlatifs gratuits, seuils inventés et répétitions marketing |
| seo-drift | PASS | chaque page garde son mot-clé et son intention propres |
| seo-technical | PASS prévu | canonical et robots existants conservés par le post-générateur |
| seo-best-practices | PASS éditorial | H1 unique existant, H2 structurés, answer-first et maillage |
| contrôle GEO | PASS éditorial | définitions explicites, entités nommées, unités converties, limites et sources |
| editorial-qa | PASS éditorial | lecture du cluster et vérification des chevauchements effectuées |
| quality gate automatique | PENDING | exécuté par GitHub Actions après génération des HTML |
| lecture complète en ordre rendu | PENDING | à refaire sur HTML généré après le gate |

## Fact-check — décisions importantes

### Classes L / M / H
- CONFIRMED : IEC 60335-2-69:2021 couvre les aspirateurs commerciaux et poussières dangereuses.
- CONFIRMED : les degrés de séparation >99 %, >99,9 % et >99,995 % sont repris par Festool avec référence EN/IEC 60335-2-69.
- CORRECTION : suppression des formulations du placeholder qui liaient trop directement chaque classe à une taille de particule unique ou rendaient la classe M « obligatoire » pour tout plâtre/béton sans contexte.

### HEPA
- CONFIRMED : EN 1822 H13 ≥99,95 % et H14 ≥99,995 % à la MPPS.
- CORRECTION : suppression de « H13 = 99,95 % à 0,3 µm » comme formulation générale ; EN 1822 classe à la MPPS.
- CONFIRMED : un filtre H13/H14 ne signifie pas automatiquement aspirateur classe H.
- CONFIRMED : pour l’amiante, l’INRS demande classe H + filtration THE au minimum H13/H14 et exigences complémentaires.

### Débit / dépression / puissance
- CONFIRMED : 1 kPa = 10 mbar ; 1 kPa ≈ 101,97 mmH2O.
- CONFIRMED : 1 L/s = 3,6 m3/h.
- CORRECTION : les watts ne sont plus présentés comme proxy direct de puissance d’aspiration.
- GARDE-FOU : les valeurs turbine/raccord/flexible ne sont jamais traitées comme directement équivalentes sans protocole commun.

### Décolmatage
- CONFIRMED : Bosch présente l’AFC comme un système destiné au maintien d’une aspiration puissante/constante.
- GARDE-FOU : aucun cycle, mécanisme ou intervalle n’est généralisé à toutes les marques.

### Prise asservie
- CORRECTION : suppression du claim générique « généralement 2 200 W ».
- GARDE-FOU : la puissance admissible doit être lue dans la notice de la référence exacte.

### Capacité de cuve
- CONFIRMED : exemple Bosch GAS 35 M AFC FR consulté : 35 L brut, 23 L net, 19,2 L eau.
- CORRECTION : suppression des recommandations arbitraires « 20-25 L bricolage / 30-35 L pro / >40 L difficile » présentées comme règles générales.

## Cannibalisation / différenciation

- `comment-choisir` = hub décisionnel, pas encyclopédie technique.
- `classes-l-m-h` = certification de l’appareil et risque poussières.
- `filtre-hepa` = norme du média filtrant et distinction avec classe H.
- `puissance-aspiration` = lecture critique des watts.
- `depression-kpa-mbar-air-watt` = unités de pression et puissance aéraulique.
- `debit-air-aspirateur` = volume d’air, captage et point de mesure.
- `decolmatage-automatique` = maintien du débit sous charge poussiéreuse.
- `prise-asservie` = synchronisation outil/aspirateur et sécurité électrique.
- `capacite-cuve` = volume brut/net, mobilité et logistique.
- `sac-ou-sans-sac` = collecte, colmatage, vidage et coût total.
- `entretien` = maintenance préventive et limites sur poussières dangereuses.

## Blockers avant publication

1. Quality gate automatique doit être vert sur les 11 HTML générés.
2. Lecture finale du rendu HTML après génération.
3. Validation humaine explicite requise par `content-workflow.config.yaml`.
4. Le `noindex` doit rester en place tant que cette validation n’a pas été donnée.

Statut final à ce stade : `QA_IN_PROGRESS`.