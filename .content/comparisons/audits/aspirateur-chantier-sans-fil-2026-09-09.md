# AUDIT — `/comparatifs/aspirateur-chantier-sans-fil/`

Date: 2026-09-09
Mode: `AUDIT`
Decision: `DEEP_REWRITE`
Confidence: 95%
Indexing: `KEEP_NOINDEX`

## Intent

Strong and distinct intent: the user is choosing around mobility, runtime, battery ecosystem and the compromises of cordless extraction.

## Preserve

- battery-platform / ecosystem framing;
- the current warning that voltage alone does not determine performance or runtime;
- the idea that the cost of batteries/chargers can change the decision;
- the Bosch/Festool/Kärcher contrast as useful evidence that cordless products serve different jobs.

## Blockers

1. **Obvious current candidates are missing.** DeWalt currently sells the DCV586M 54 V FLEXVOLT class-M cordless extractor, materially different from the three current candidates and potentially decision-changing. Makita also maintains a broad cordless construction-vacuum range.
2. **The current weighted score compares heterogeneous runtime claims.** Runtime depends on battery capacity, suction setting, battery count and test conditions; current scores create more comparability than the evidence supports.
3. **Product roles are mixed without a clear gate.** The selection combines consumer wet/dry, compact class-L and premium ecosystem products under one numerical ranking.
4. **Legacy cloned structure** rather than a battery/platform-specific decision architecture.

## Current evidence signal

DeWalt official source checked 2026-09-09:
https://www.dewalt.fr/fr-fr/produit/dcv586mn-xj/aspirateur-tstak-xr-flexvolt-54v-brushless-eau-et-poussieres-classe-m

The current DCV586M is cordless, 54 V FLEXVOLT and class M with automatic filter cleaning. Its omission alone is enough to reopen candidate selection.

## Secondary improvements

- organize by platform/use: compact 18 V, larger wet/dry cordless, professional dust extraction, ecosystem-specific workflow;
- normalize runtime only when manufacturer conditions are comparable;
- show required batteries/chargers as configuration, not hidden purchase assumptions;
- distinguish class and dust-safety needs before runtime ranking.

## Missing data

- no persisted 2026 candidate screen across DeWalt/Makita/Bosch/Festool/Kärcher;
- no standardized runtime evidence table.

## Next step

Rebuild the cordless universe first, then produce conditional recommendations by battery ecosystem and task. Do not retain the current 1–3 score as the governing structure.
