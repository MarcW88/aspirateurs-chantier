# PUBLISH_REVIEW — `/comparatifs/aspirateur-professionnel/`

Date: 2026-09-09
Mode: `PUBLISH_REVIEW`
Result: `PASS — READY_FOR_HUMAN_VALIDATION`
Indexing: `KEEP_NOINDEX`

## 1. Intent

PASS.

The page serves `aspirateur chantier professionnel` as a scenario-led decision page rather than a duplicate of `/comparatifs/aspirateur-classe-m/`.

The decision order is explicit: dust risk / required class first, then workflow, filter cleaning, mobility and capacity.

## 2. Scope and recommendation logic

PASS.

Six current representative references cover distinct professional situations across Bosch Professional, Makita, Festool and Kärcher. They are not presented as an exhaustive market census or a numerical 1–6 ranking.

Each recommendation is conditional and includes a material trade-off.

## 3. Evidence and factuality

PASS for the pilot evidence basis.

Hard product facts are persisted from primary manufacturer sources in `.content/models/model-evidence.json` and mirrored into `.content/comparisons/aspirateur-professionnel.json`.

The page distinguishes:
- class L/M from filter type, power and airflow;
- filter cleaning systems from safety certification;
- manufacturer specifications from editorial recommendations;
- desk research from physical testing.

No first-hand test language is used.

## 4. Measurement comparability

PASS.

Airflow/depression are not used to create a cross-brand podium when equivalent measurement points/protocols are not documented. Bosch turbine maxima are explicitly treated as manufacturer-context measurements rather than universal ranking inputs.

## 5. Affiliate value

PASS.

The page remains useful without affiliate links because it explains:
- when class M matters and when it does not;
- why a lighter class-L or cordless machine can be preferable;
- the role of automatic/manual filter cleaning;
- tool workflow and ecosystem trade-offs;
- capacity vs mobility;
- when to leave this comparison for a class-M, cordless, usage or technical guide page.

Affiliate commission is documented as not influencing selection or recommendation.

## 6. Editorial structure / anti-template

PASS.

The pilot does not use the legacy `method → weighted criteria → ranking → product cards → conclusion` structure. It uses a scenario table, conditional choices, asymmetrical product limitations and a dedicated measurement caveat.

The global cluster validator was updated to check the semantic intent boundary and scenario diversity rather than exact H2 wording.

## 7. Internal linking

PASS.

The page routes to:
- `/comparatifs/aspirateur-classe-m/`;
- `/comparatifs/aspirateur-chantier-sans-fil/`;
- relevant `/usages/` pages;
- `/guides/classes-l-m-h/`;
- `/guides/decolmatage-automatique/`;
- `/guides/prise-asservie/`;
- relevant model pages.

## 8. SEO / technical

PASS for draft state.

- unique title and meta description;
- one H1;
- canonical preserved;
- `noindex, follow` preserved;
- sidebar table of contents matches actual H2 sections;
- primary-source box present;
- no fake Review/test claim introduced.

## 9. Machine validation

PASS on PR #16 head after the structure-agnostic cluster-gate correction:

- `Validate comparison skill stack`: SUCCESS;
- `Validate global navigation`: SUCCESS;
- `Validate audited content cluster`: SUCCESS.

The bespoke generator was also compiled and executed successfully in the pilot action before PR review; ledger, cluster integrity, noindex and whitespace passed.

## Final verdict

`PASS — READY_FOR_HUMAN_VALIDATION`

The page must remain `noindex, follow` until explicit human approval and a separate explicit instruction to index it.
