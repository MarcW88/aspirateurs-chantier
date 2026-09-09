# AUDIT — `/comparatifs/petit-aspirateur-de-chantier/`

Date: 2026-09-09
Mode: `AUDIT`
Decision: `DEEP_REWRITE`
Confidence: 90%
Indexing: `KEEP_NOINDEX`

## Intent

The compact/small-format intent is valid and distinct from cordless: some users want a machine that is easy to carry/store even when filaire is acceptable.

## Preserve

- the idea that compactness is a trade-off with tank volume and workflow;
- three different roles are already visible: simple/light wet-dry, cordless compact and professional class-M compact;
- the warning that safety requirements can justify accepting more weight.

## Blockers

1. **The hub definition contradicts the page.** `/comparatifs/` labels `Petit format` as `< 15 litres`, but the current shortlist includes Kärcher WD 3 at 17 L and Festool CTM MIDI at 15 L.
2. **Compactness is scored without a stable dimensional definition.** Tank litres are not a reliable proxy for footprint, storage height, carrying ergonomics or vehicle fit.
3. **The page overlaps strongly with `sans sac`.** Bosch GAS 18V-10 L and Kärcher WD 3 are used in both pages; the arguments need to be distinct rather than reweighted.
4. **Current candidates mix consumer, cordless professional and class-M premium machines under one score.** That can be useful as profile coverage, but not as a universal compactness podium.
5. **Legacy cloned architecture** remains the same as the other old comparisons.

## Secondary improvements

- redefine the page around dimensions/weight/handling, not an arbitrary litre ceiling;
- use profiles such as `smallest/easiest to store`, `cordless compact`, `compact professional dust extractor`;
- include hose/accessory storage and carry workflow when documented;
- hand off to `/aspirateur-chantier-sans-fil/` when battery mobility becomes the primary requirement.

## Missing data

- no normalized dimensions/footprint dataset has been persisted for current candidates;
- no GSC data available to determine whether users interpret `petit` as tank volume, weight or physical footprint.

## Next step

Keep the URL, replace the `<15 L` definition at hub level, build a compactness evidence table and rewrite by profile rather than a single score.
