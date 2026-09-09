# CLUSTER_AUDIT — `/comparatifs/`

Date: 2026-09-09
Scope: 9 comparison pages on `main`, including the rewritten `/comparatifs/aspirateur-professionnel/` as the current reference implementation.
Result: `FAIL — KEEP_NOINDEX`

## Executive conclusion

The comparison cluster contains nine URLs with mostly defensible keyword-level intents, but eight pages still run through the legacy shared ranking renderer. Their editorial architecture and recommendation logic are therefore too industrialized for the new comparison workflow.

The professional page is currently the only page with a bespoke, scenario-led evidence ledger and no mandatory ranking. It should remain the reference while the rest of the cluster is rebuilt in audited order.

## Blocker 1 — legacy structural cloning

`_generate_comparatifs.py` still renders the eight legacy pages through the same sequence:

1. answer box;
2. `Notre classement 2026`;
3. weighted score table;
4. `Notre méthode de comparaison`;
5. `Les modèles retenus et pourquoi`;
6. `Ce qui change réellement le choix`;
7. generic safety/limits section;
8. sources.

The same explanatory paragraphs about airflow/depression, filter loading, cost of bags/batteries and score confidence are reused across intents. This conflicts with the new rule that the architecture must follow the decision, not a page template.

## Blocker 2 — exact product cloning between general and powerful

`/comparatifs/meilleur-aspirateur-de-chantier/` and `/comparatifs/aspirateur-chantier-puissant/` use exactly the same three candidates:

- Bosch Professional GAS 35 M AFC;
- Kärcher NT 30/1 Tact Te M ACD;
- Kärcher WD 7 Control.

Only the criteria/weights and winner framing change. Product-universe overlap is therefore 100%. This is the clearest cluster-level example of a reweighted comparison rather than a distinct decision page.

## Blocker 3 — high overlap in the M/pro/industrial family

Before the professional pilot, general, professional, industrial and class-M pages recycled Bosch GAS 35 M AFC and Kärcher NT 30/1 Tact. The professional page has now broadened its scope, but the remaining legacy pages still show substantial overlap:

- general ↔ industrial: 2 of 3 selected products shared;
- general ↔ class M: 2 of 3 shared;
- industrial ↔ class M: 2 of 3 shared.

The overlap itself is not forbidden; the problem is that the pages still use near-identical ranking logic and product arguments.

## Blocker 4 — industrial intent is currently mis-scoped

The current industrial page defines industrial as a large-capacity mobile professional vacuum and compares Kärcher NT 50/1, NT 30/1 and Bosch GAS 35 M AFC.

Current manufacturer taxonomy is broader: industrial vacuuming includes mobile and stationary machines, continuous-duty/process use and dedicated ATEX/industrial families. Kärcher currently separates industrial IVC/IVR solutions from standard NT wet/dry safety vacuums.

Primary references checked:
- https://www.kaercher.com/fr/professional/aspirateurs-industriels.html
- https://www.kaercher.com/be-fr/professional/solutions-industrielles-aspiration-et-depoussierage/aspirateurs-industriels/aspirateurs-industriels-solides-poussieres/ivc-60-24-2-tact2-m-15761050.html
- https://www.kaercher.com/be-fr/professional/solutions-industrielles-aspiration-et-depoussierage/aspirateurs-industriels/aspirateurs-industriels-solides-poussieres/ivr-60-30-sc-m-acd-99906430.html

The URL may remain strategically useful, but its current product universe cannot support the industrial intent.

## Blocker 5 — hub labels do not always match page scope

The `/comparatifs/` hub currently labels:

- `Les plus puissants` as `Dépression > 25 kPa`, while the page also relies on airflow and filter endurance and the threshold is not a robust cross-brand definition;
- `Petit format` as `< 15 litres`, while the current selection includes Kärcher WD 3 at 17 L and Festool CTM MIDI at 15 L;
- `Industriel` as `Grande capacité`, which is narrower than the actual industrial vacuum universe;
- `Classe M` as `Poussières dangereuses modérées`, a shorthand that should be replaced by a precise class/risk description.

## Blocker 6 — candidate coverage is uneven

Examples already visible from the site's own evidence or current manufacturer ranges:

- class M omits Makita VC4210MX, already documented in the local model evidence and currently class M with InfiniClean;
- cordless omits the current DeWalt DCV586M 54 V FLEXVOLT class M, a materially different professional cordless option;
- general uses only three products and two are Kärcher;
- eau/poussière uses two Kärcher WD models out of three candidates;
- bagless mixes an explicitly bagless Bosch design with machines whose bagless use needs model/use-specific qualification.

Candidate coverage does not need to be exhaustive, but obvious candidates that can change the recommendation must be considered or explicitly excluded.

## Product-overlap signals

| Pair | Shared products | Signal |
| --- | ---: | --- |
| General ↔ Powerful | 3 / 3 | Critical — exact same universe |
| General ↔ Industrial | 2 / 3 | High |
| General ↔ Class M | 2 / 3 | High |
| Industrial ↔ Class M | 2 / 3 | High |
| Sans sac ↔ Petit format | 2 / 3 | High, but intents can remain distinct |

## Role map to preserve

- `meilleur-aspirateur-de-chantier` = broad orientation by major use case / constraint, not one universal score;
- `aspirateur-professionnel` = professional working scenarios across L/M, mobility and workflow;
- `aspirateur-classe-m` = class M is the entry gate;
- `aspirateur-industriel` = actual industrial vacuum universe, not a synonym for professional/high-capacity NT;
- `aspirateur-chantier-puissant` = explain what “powerful” means and only rank directly comparable measurements;
- `aspirateur-eau-poussiere` = wet/dry decision;
- `aspirateur-chantier-sans-fil` = battery platform, runtime and cordless workflow;
- `aspirateur-chantier-sans-sac` = collection mode, filter protection and disposal trade-offs;
- `petit-aspirateur-de-chantier` = compactness/mobility, defined by dimensions and handling rather than an arbitrary litre cut-off.

## Recommended audit decisions

| URL | Decision | Confidence |
| --- | --- | ---: |
| `/comparatifs/aspirateur-professionnel/` | KEEP | High |
| `/comparatifs/meilleur-aspirateur-de-chantier/` | DEEP_REWRITE | High |
| `/comparatifs/aspirateur-eau-poussiere/` | DEEP_REWRITE | High |
| `/comparatifs/aspirateur-chantier-sans-fil/` | DEEP_REWRITE | High |
| `/comparatifs/aspirateur-chantier-sans-sac/` | DEEP_REWRITE | Medium-high |
| `/comparatifs/aspirateur-chantier-puissant/` | DEEP_REWRITE | Very high |
| `/comparatifs/aspirateur-industriel/` | DEEP_REWRITE | Very high |
| `/comparatifs/aspirateur-classe-m/` | DEEP_REWRITE | High |
| `/comparatifs/petit-aspirateur-de-chantier/` | DEEP_REWRITE | High |

`DEEP_REWRITE` does not mean discarding all facts. Several pages have sound intent framing and useful manufacturer evidence. The blocker is usually the combination of candidate scope + forced scoring + cloned architecture.

## Recommended rollout order

1. industrial — wrong product universe / highest intent risk;
2. powerful — exact duplicate candidate universe + measurement comparability risk;
3. general — must become the true umbrella decision page after powerful is separated;
4. class M — high-value clear intent, but obvious candidate gaps and unnecessary score precision;
5. cordless — strong intent, missing materially different current candidates;
6. eau/poussière — clear intent but narrow/Kärcher-heavy scope;
7. sans sac — valid query, needs a more rigorous collection-mode definition;
8. petit format — fix compactness definition and break the legacy template.

After these changes, rerun `CLUSTER_AUDIT` before any indexation decision. Keep every page `noindex, follow` during rollout.
