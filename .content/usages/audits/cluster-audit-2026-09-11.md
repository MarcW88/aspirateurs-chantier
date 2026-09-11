# CLUSTER_AUDIT — `/usages/`

Date: 2026-09-11
Scope: 7 usage pages on `main`, audited against the new `usage-analysis-workflow`, the current Guides/Comparatifs boundaries and the 80/20 workflow governance.
Result: `FAIL — REQUIRES_WORKFLOW_RERUN — KEEP_NOINDEX`

## Executive conclusion

The `/usages/` cluster contains six defensible autonomous jobs and one URL whose current role is too broad.

The main cluster-level problem is not blatant keyword duplication. It is editorial industrialisation: almost every page follows the same cadence — answer box, four short criterion sections, one “Approfondir” link per section, then a generic sources/method block. The H2 labels differ, but the functional architecture is largely predetermined before the job analysis.

The new usage workflow requires the opposite: the job, circumstances, frictions and evidence must determine the architecture. The current pages also have no `.content/usages/<slug>.json` workflow records yet, so none can pass the new PUBLISH_REVIEW contract as-is.

No page is rewritten, redirected or indexed by this audit. All seven URLs remain `noindex, follow`.

## Cluster blocker 1 — structural cloning

The seven pages share a strongly repeated editorial rhythm:

1. one answer box;
2. four short H2 sections in most cases;
3. one paragraph of explanation per section;
4. one `Approfondir` link after each paragraph;
5. a generic `Sources et méthode` section using almost identical wording.

The visual shell can remain shared. The issue is that the editorial architecture is also shared, even when the jobs differ materially.

Examples:

- `/usages/aspirateur-atelier/` should reason about a mixed fixed-workspace system and the boundary between cleaning, mobile source extraction and stationary collection;
- `/usages/aspirateur-platre/` should branch by the actual operation/material and distinguish gypsum/joint-compound dust from other mineral substrates instead of behaving like a generic fine-dust page;
- `/usages/aspirateur-scie/` should change according to saw type, capture geometry and portable-vs-stationary workflow.

These decisions cannot all be expressed well through the same four-section skeleton.

## Cluster blocker 2 — the generic renovation page duplicates the general buying guide

`/usages/aspirateur-bricolage-renovation/` currently tells the reader to:

- list the real tasks;
- separate general wet/dry cleaning from dust-risk work;
- consider source capture and classes;
- compare the complete system cost.

The guide `/guides/comment-choisir-aspirateur-de-chantier/` already performs this role in substantially greater depth: it starts from contaminant + work mode, then covers class, airflow/depression, filter cleaning, tool connection, capacity/mobility and explicitly routes by plaster/sanding, wood, debris/water and workshop scenarios.

Without query/GSC evidence proving a separate renovation-specific job, the current usage URL adds little autonomous value. Recommended structural decision: `MERGE` into `/guides/comment-choisir-aspirateur-de-chantier/`, subject to human confirmation before any redirect/removal.

## Cluster blocker 3 — Plâtre and Ponceuse overlap, but should not be merged

These URLs cover adjacent situations but can serve distinct jobs:

- `/usages/aspirateur-platre/` = material/process risk and clogging behaviour across sanding, cutting and cleanup involving plaster/drywall/joint compound and potentially other substrates;
- `/usages/aspirateur-ponceuse/` = continuous source-capture workflow around a sander: hose flexibility, port fit, sustained airflow, filter cleaning, automatic start/remote and material-dependent dust class.

The current Plâtre page still leans heavily on generic “fine dust + class + declogging” guidance and sends the reader to Ponceuse for the most concrete tool workflow. To justify its own URL, it needs a more material/operation-led architecture and a clearer safety distinction between gypsum-based dust and other mineral dusts rather than implying that “plaster” itself equals a silica scenario.

The Ponceuse page already has a clearer autonomous role and only needs targeted reinforcement, not a full rebuild.

## Cluster blocker 4 — Bois and Scie overlap, but solve different decisions

`/usages/aspirateur-bois-sciure-copeaux/` has a defensible material-led job:

- fine wood dust versus sawdust/chips;
- source capture;
- high-vac mobile extractor versus higher-volume stationary collection/network;
- cleaning without resuspension.

`/usages/aspirateur-scie/` should instead be tool/workflow-led:

- circular/mitre/table saw capture geometry;
- one versus multiple extraction ports;
- portable versus fixed machines;
- hose diameter and chip transport;
- auto-start/remote;
- wood versus mineral cutting risk.

The current Scie page is too generic to express those differences and therefore needs a deeper rebuild. The Bois page already contains a sound role and can be strengthened through a limited update.

## Cluster blocker 5 — Atelier is too broad in its current form

The current Atelier page correctly distinguishes general cleaning from extraction at the machine, which is valuable and should be preserved.

However, it then returns to generic class, mobility and ecosystem advice. An autonomous workshop page should answer a different system-design question:

- which tasks need mobile high-vac extraction;
- which machines may need dedicated chip/dust collection or a fixed network;
- how many machines/work zones are served;
- hose reach and routing;
- frequency/volume of collection;
- noise and fixed-location trade-offs;
- wet cleanup versus dry source extraction;
- when a general wet/dry vacuum stops being the right architecture.

Because the current architecture does not yet cover that job deeply enough, this is a `DEEP_REWRITE`, not a merger with the general guide.

## Boundary with current Comparatifs

The rewritten comparison cluster now leaves useful room for Usage pages:

- `/comparatifs/aspirateur-eau-poussiere/` compares specific wet/dry workflows and product references; `/usages/aspirateur-gravats/` can remain about the situation itself: deposited debris, mineral-dust generation, liquid residue and cleanup sequence;
- `/comparatifs/aspirateur-classe-m/` assumes M is already the relevant gate and compares M configurations; Plâtre/Ponceuse must stay upstream and determine whether that gate is relevant at all;
- professional/industrial comparisons choose between machine architectures; Atelier/Bois should define the job before that handoff.

No additional merge with a comparison page is recommended.

## Recommended audit decisions

| URL | Decision | Confidence | Why |
| --- | --- | ---: | --- |
| `/usages/aspirateur-atelier/` | `DEEP_REWRITE` | High | Valid job, but current page is too generic and overlaps the general guide instead of designing the workshop extraction system. |
| `/usages/aspirateur-bois-sciure-copeaux/` | `LIGHT_UPDATE` | High | Strong autonomous material-led role; preserve source-capture and wood-dust evidence, deepen mobile extractor vs stationary chip/dust collection boundary. |
| `/usages/aspirateur-bricolage-renovation/` | `MERGE` → `/guides/comment-choisir-aspirateur-de-chantier/` | Medium-high | Current role is essentially a compressed general buying guide; no unique job is demonstrated yet. |
| `/usages/aspirateur-gravats/` | `LIGHT_UPDATE` | High | Clear situation-led role; strengthen debris-size/hosing/collection boundary and keep fine mineral dust separate from deposited rubble cleanup. |
| `/usages/aspirateur-platre/` | `DEEP_REWRITE` | High | Valid intent but insufficient autonomous material/process value; must separate operations and avoid conflating plaster with generic silica/mineral-risk guidance. |
| `/usages/aspirateur-ponceuse/` | `LIGHT_UPDATE` | High | Best-defined tool workflow in the cluster; preserve captage/raccord/décolmatage/trigger logic, strengthen evidence and distinctiveness. |
| `/usages/aspirateur-scie/` | `DEEP_REWRITE` | High | Valid tool intent, but “scie” is currently treated too generically; saw type/capture geometry/portable-vs-fixed workflow should drive the page. |

There is no `KEEP` under the new workflow because even the strongest current pages still require at least a workflow record, fresh evidence review and anti-template/PUBLISH_REVIEW pass before human validation.

## Value to preserve by page

### Atelier
- opening distinction between floor/general cleaning and direct machine extraction;
- mobility versus large-cuve trade-off;
- warning that ecosystem value only matters when it reduces real workflow friction.

### Bois / sciure / copeaux
- fine dust versus large chips distinction;
- INRS wood-dust prevention/source-capture evidence;
- warning against inferring machine class from filter type;
- aspiration rather than sweeping/blowing for cleanup.

### Bricolage / rénovation
If merged, preserve:
- distinction between ordinary wet/dry cleanup and source capture for hazardous/fine dust;
- full-system-cost idea (bags, filters, fittings, batteries/consumables).

### Gravats
- deposited rubble versus dust generated during cutting/grinding;
- liquid-capacity caveat;
- WD cleaning machine versus certified safety extractor distinction.

### Plâtre
- fine/clogging dust and sustained-flow problem;
- distinction between cleanup and source capture;
- declogging as a workflow feature, not a dust-class proxy.

### Ponceuse
- source capture before tank capacity;
- class depends on material, not tool brand;
- sustained airflow/filter loading;
- automatic start/Bluetooth/remote as workflow features rather than filtration features.

### Scie
- capture hood/port quality before nominal vacuum power;
- hose diameter/chip transport;
- automatic start as workflow improvement;
- material determines the risk, not the fact that a saw is used.

## Recommended rollout order

1. `aspirateur-bricolage-renovation` — human structural decision on the proposed MERGE before spending editorial effort;
2. `aspirateur-platre` — highest safety/role ambiguity among retained URLs;
3. `aspirateur-scie` — valid intent but current job definition is too broad;
4. `aspirateur-atelier` — broad system-design page that needs a bespoke architecture;
5. `aspirateur-ponceuse` — strong base, targeted update;
6. `aspirateur-bois-sciure-copeaux` — strong base, targeted update;
7. `aspirateur-gravats` — strong base, targeted update.

## Next gate

Do not rewrite anything automatically from this audit.

For each retained URL:

`usage-analysis-workflow / AUDIT` → create `.content/usages/<slug>.json` → `usage-content-workflow` only for LIGHT_UPDATE/DEEP_REWRITE → `usage-analysis-workflow / PUBLISH_REVIEW` → human validation.

For the proposed MERGE, wait for explicit human confirmation before redirecting/removing anything.

Keep all seven pages `noindex, follow` during the rollout.