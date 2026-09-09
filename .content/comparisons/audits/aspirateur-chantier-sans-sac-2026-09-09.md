# AUDIT — `/comparatifs/aspirateur-chantier-sans-sac/`

Date: 2026-09-09
Mode: `AUDIT`
Decision: `DEEP_REWRITE`
Confidence: 85%
Indexing: `KEEP_NOINDEX`

## Intent

The query is commercially real and should not be merged away. Current retail category pages still expose `aspirateur de chantier sans sac` as a shopping/filter intent.

## Preserve

- the warning that `sans sac` does not mean `sans consommable` or better filtration;
- the disposal/maintenance trade-off for fine dust;
- Bosch GAS 18V-10 L as a strong evidence anchor because Bosch explicitly describes it as a bagless design.

## Blockers

1. **`Sans sac` is treated as a simple binary score even when manufacturer positioning differs.** An explicitly bagless/cyclonic design is not the same thing as a wet/dry vacuum that can sometimes be operated without a bag.
2. **Current Kärcher candidates need use-specific qualification.** The page should document when bagless operation is recommended, tolerated or undesirable for each waste type rather than scoring it 7/10 or 8/10 editorially.
3. **Disposal exposure is underweighted.** Fine dust may make a bag or disposal liner preferable even when direct tank collection is technically possible.
4. **The current score adds false precision** to filter management, emptying and bagless suitability.
5. **Legacy cloned structure** rather than a collection-mode/maintenance decision page.

## Current evidence signal

Bosch official source checked 2026-09-09:
https://www.bosch-professional.com/fr/fr/products/gas-18v-10-l-06019C6302/

Bosch explicitly documents a `conception sans sac` for the GAS 18V-10 L. This is a stronger evidence standard than simply inferring bagless suitability from a removable bag.

## Secondary improvements

- classify candidates as `designed bagless`, `manufacturer-documented direct collection`, or `bag recommended for the target dust`;
- separate liquids/coarse debris from fine dust;
- include filter-protection and emptying hygiene as first-class trade-offs;
- route safety-sensitive fine-dust users to the relevant class/usage guidance.

## Missing data

- model-by-model manufacturer instructions for bag/no-bag operation are not yet persisted for the current Kärcher candidates;
- no GSC data was available to quantify the exact query importance.

## Next step

Keep the URL but rebuild around collection mode and disposal, with explicit evidence for bagless suitability. Remove the generic ranking structure.
