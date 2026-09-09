# AUDIT — `/comparatifs/aspirateur-chantier-puissant/`

Date: 2026-09-09
Mode: `AUDIT`
Decision: `DEEP_REWRITE`
Confidence: 99%
Indexing: `KEEP_NOINDEX`

## Intent

The query can remain distinct if the page genuinely helps users understand and compare suction performance. The current execution does not yet prove that distinction.

## Preserve

- the explanation that watts, airflow and vacuum/depression are different quantities;
- the warning that filter loading and automatic cleaning matter for sustained performance;
- the safety boundary: raw suction does not replace dust-class requirements.

## Blockers

1. **100% product-universe duplication with the general comparison.** Both pages use Kärcher WD 7 Control, Kärcher NT 30/1 Tact Te M ACD and Bosch GAS 35 M AFC.
2. **The strongest score weight is built on cross-brand airflow/depression figures.** Measurement points/protocols are not demonstrated equivalent, so the page creates an unjustified podium from manufacturer maxima.
3. **The hub currently summarizes the page as `Dépression > 25 kPa`, which is not a sufficient definition of “powerful” and does not match the page's own emphasis on airflow and sustained performance.
4. **The same candidate can win raw numbers but lose the actual chantier decision**, meaning the current single ranking combines two incompatible questions.
5. **Legacy cloned architecture** with the same method/model/limits prose as the general page.

## Why this is the highest-confidence rewrite

The new professional pilot explicitly refuses to use cross-brand airflow/depression as a podium when equivalent measurement points are not documented. The powerful page currently does the opposite by making `Débit et dépression annoncés` a 35% hard gate.

## Secondary improvements

- decide whether the page answers `highest published suction figures` or `best sustained extraction performance for a task`;
- if using numeric comparisons, create equivalence groups by measurement context instead of one cross-brand table;
- separate coarse-debris lifting, airflow transport and fine-dust endurance;
- make the page hand off to class M and usage pages when safety or dust loading becomes primary.

## Missing data

- no standardized manufacturer measurement protocol table;
- no independent same-protocol test data is currently persisted.

## Next step

Rebuild from the measurement problem upward. Do not reuse the general page's exact candidate universe. If comparable evidence cannot support a true ranking, use scenario-based shortlists plus an explicit measurement caveat rather than a score.
