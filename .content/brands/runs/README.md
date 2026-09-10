# Brand workflow run evidence — contract v2

This directory stores **editorial execution evidence**, not generated marketing copy.

A file `<slug>.json` is created only after a real `brand-content-workflow` run. Python generators must never fabricate one.

A valid run records:

- `contract_version: 2`
- `slug`
- `status: PASS`
- `reader_decision`
- `value_without_affiliate_links`
- an evidence-derived `outline`
- `shared_steps` for the imported/shared skill stack
- `custom_steps` limited to `vacuum-domain-review` and `brand-analysis-publish-review`
- final `publish_review`

Every `PASS` step needs a concrete `output` summary. `N/A` is allowed only with a reason.

The expected shared execution steps are:

`search-intent`, `content-audit`, `content-refresh`, `fact-check-pre`, `evidence-based-reviews`, `affiliate-value`, `content-brief-authoring`, `content-and-copy`, `fact-check-post`, `humanizer`, `general-writing`, `anti-ai-slop`, `internal-linking-audit`, `seo-technical`, `seo-best-practices`, `editorial-qa`.

The custom layer is intentionally narrow. It may adapt the vacuum-cleaner domain and perform the cross-brand publish decision, but it may not reimplement the shared skills.

Validate one completed run with:

```bash
python3 validate_brand_run_evidence.py --slug karcher --require-run
```

Current legacy pages can remain as `noindex, follow` drafts without a run file. They must be marked `REQUIRES_WORKFLOW_RERUN`, never `READY_FOR_HUMAN_VALIDATION`.
