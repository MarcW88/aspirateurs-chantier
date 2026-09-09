# Next step after comparison workflow migration

Do not rewrite comparison pages immediately.

Required next operation:

`comparison-analysis-workflow / CLUSTER_AUDIT`

Scope: all nine current `/comparatifs/` URLs.

Only after the cluster audit should each page receive a decision (`KEEP`, `LIGHT_UPDATE`, `DEEP_REWRITE`, `MERGE`, `NOINDEX`) and be processed accordingly.
