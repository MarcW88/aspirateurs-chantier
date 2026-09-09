# CLUSTER_AUDIT — `/comparatifs/` — post-rollout

Date: 2026-09-09
Scope: 9 comparison URLs after the audited rewrite sequence.
Result: `PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX`

## Executive conclusion

The main blockers from the pre-rollout audit are resolved at cluster level.

The professional pilot remains the reference scenario-led page. The other eight comparison pages now use intent-specific evidence ledgers and bespoke decision architectures. No page is required to expose a numerical ranking, a 100-point weighting system or the legacy `ranking → method → products → generic limits` sequence.

All pages remain `noindex, follow` pending explicit human approval and a separate indexation decision.

## 1. Structural cloning

PASS.

The eight rewritten pages have distinct H2 signatures and distinct decision structures:

- industrial: product/process boundary → industrial process profiles → duty cycle → material stream → ACD/ATEX boundary;
- powerful: airflow vs vacuum → manufacturer values → filter loading → work scenarios → cases where power is the wrong question;
- general: scenario orientation → decision order → why a universal score is misleading → specialist handoffs;
- class M: M certification gate → five M profiles → filter cleaning → volume → measurement caveat;
- cordless: four battery/class profiles → L/M boundary → battery platform → runtime → tool activation;
- wet/dry: four wet/dry profiles → liquid handling → filter → tool integration → dust-safety boundary;
- bagless: three collection definitions → four examples → fine dust → total consumable/maintenance cost;
- compact: compactness definition → four references → work profiles → transport → dust-class boundary.

The machine semantic gate rejects identical H2 architectures across the eight rewritten pages.

## 2. General vs powerful overlap

PASS.

The former 100% candidate overlap is removed.

The general page now acts as an umbrella decision page across major scenarios and routes users toward specialist comparisons. The powerful page is a measurement-literacy page and does not convert non-equivalent manufacturer airflow/vacuum claims into a cross-brand podium.

## 3. Professional vs class M

PASS.

`/aspirateur-professionnel/` remains broader: L and M, corded and cordless, mobility and tool workflow.

`/aspirateur-classe-m/` now uses class M as an entry prerequisite and then distinguishes five materially different M profiles: cordless, compact, 30 L Tact/antistatic/ACD, 35 L AFC and 42 L InfiniClean.

## 4. Industrial intent

PASS.

The industrial page no longer equates `industrial` with a large-capacity NT/GAS construction vacuum.

Its evidence universe now includes:
- Kärcher IVC 60/24-2 Tact² M — mobile industrial / production-area cleaning;
- Kärcher IVR 60/30 Sc M ACD — 400 V continuous-duty/process profile;
- Nilfisk S3 L100 family — industrial hazardous-dust configurations;
- Nilfisk VHO200 — oils, liquids and chips.

The page explicitly routes ordinary tool-connected construction work back to the professional/class-M cluster.

## 5. Candidate coverage

PASS for representative editorial coverage.

The most material gaps identified in the audit are addressed:
- Makita VC4210MX is now in class M and relevant general/power profiles;
- Bosch GAS 18V-12 MC and DeWalt DCV586M expand the cordless M universe;
- Nilfisk is added to wet/dry coverage;
- general coverage is no longer limited to three products with two Kärcher references.

The selection remains intentionally representative rather than exhaustive. Any future market expansion should rerun `AUDIT` before changing recommendations.

## 6. Measurement comparability

PASS.

The powerful and class-M pages explicitly distinguish manufacturer measurement contexts. Bosch turbine maxima are not treated as automatically equivalent to values published by other manufacturers without the same measurement context.

No cross-brand airflow/vacuum score is used where equivalence is not established.

## 7. Bagless scope

PASS.

The page now separates:
1. an explicitly documented bagless design;
2. a wet/dry machine that can collect directly in the tank for appropriate materials;
3. cases where a bag/collection system remains preferable for filter protection or safer disposal.

Bosch's current official GAS 18V-10 L page is persisted as primary evidence for its explicitly documented bagless design.

## 8. Compact scope

PASS.

The old `<15 L` definition is removed. Compactness is now treated through weight, dimensions/handling, power source and useful capacity. The comparison hub no longer advertises the stale litre threshold.

## 9. Comparison hub

PASS.

The misleading labels identified in the first audit have been replaced:
- `Dépression > 25 kPa` → contextualised airflow/depression;
- `< 15 litres` → mobility/encombrement;
- `Grande capacité` → process/continuous/oils/chips;
- `Poussières dangereuses modérées` → class-M certification.

The hub description now reflects intent/evidence rather than claiming every comparison is primarily a metrics table.

## 10. Canonical generation

PASS.

The legacy `_generate_comparatifs.py` is no longer part of the canonical comparison generation path because importing it also invokes the old global site generator and can rewrite unrelated clusters.

Canonical order is now:
1. comparison skill-stack validation;
2. professional scenario override;
3. eight audited comparison overrides;
4. editorial polish;
5. comparison-only normalization;
6. machine-integrity validation;
7. semantic rollout validation.

This keeps comparison generation isolated from brands, usages, guides and model pages.

## Final verdict

`PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX`

The cluster is structurally and semantically ready for human review. This is not an instruction to index the pages. All nine comparison URLs must remain `noindex, follow` until an explicit separate indexation decision.
