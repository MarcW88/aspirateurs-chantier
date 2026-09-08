# Editorial QA — Cluster /guides/

```yaml
scope: /guides/
date: 2026-09-08
status: DRAFT_READY
human_validation_required: true
publishable: false
robots_expected: noindex,follow
last_successful_quality_run: 34224377464
```

## Routing

Les 11 guides ont été routés `NEW_CONTENT` : les pages contenaient une réponse courte et un placeholder, sans article exploitable. Aucune réécriture totale de contenu performant n’a donc été effectuée.

## Chaîne QA

| Étape | Statut | Contrôle |
|---|---|---|
| content-refresh | PASS | NEW_CONTENT justifié, contenu placeholder remplacé |
| search-intent | PASS | chaque guide répond à une question distincte et conserve un périmètre propre |
| affiliate-value | PASS | guides utiles sans lien affilié forcé ; transitions vers comparatifs/usages quand pertinentes |
| fact-check | PASS avec garde-fous | claims normatifs limités aux sources IEC/EN, INRS et fabricants ; pas de prix ni test inventé |
| natural-writing | PASS | phrases explicatives, compromis et limites ; pas de succession de définitions génériques |
| internal-linking-audit | PASS | minimum structurel validé + liens contextuels vers guides, usages, accessoires, comparatifs et modèles |
| humanizer | PASS | formulations non promotionnelles, exemples fonctionnels, nuances explicites |
| general-writing | PASS | titres orientés questions et décisions, paragraphes cohérents |
| anti-ai-slop | PASS | suppression des superlatifs gratuits, seuils inventés et répétitions marketing |
| seo-drift | PASS | chaque page garde son mot-clé et son intention propres |
| seo-technical | PASS | canonical et robots existants conservés ; noindex vérifié automatiquement sur les 11 guides |
| seo-best-practices | PASS | H1 unique existant, H2 substantiels, answer-first et maillage |
| contrôle GEO | PASS | définitions explicites, entités nommées, unités converties, limites et sources |
| editorial-qa | PASS | lecture du cluster et vérification des chevauchements effectuées |
| quality gate automatique | PASS | run GitHub Actions 34224377464 : 900 mots min., 5 H2 min., 70 mots/section, 4 liens internes, 3 cibles uniques, 3 sources |
| idempotence génération | PASS | chaque guide est normalisé à exactement un bloc `article-answer` après régénération |
| lecture finale en ordre rendu | PASS | HTML généré relu après le gate ; duplication answer-first détectée puis corrigée sur tout le cluster |

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

## Blocker restant avant publication

La seule étape restante est la validation humaine explicite requise par `content-workflow.config.yaml`. Tant qu’elle n’est pas donnée, les pages restent en `noindex,follow` et le changement ne doit pas être fusionné sur `main` comme contenu publiable.

Statut final : `DRAFT_READY`.