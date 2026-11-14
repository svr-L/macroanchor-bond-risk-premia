# Research status and roadmap — 14 November 2026

## Parent paper: finalized, full executed source recovered

[The Macro Anchor as a Short-Rate Central Tendency: Bond Risk Premia and an Empirical-Design Decomposition](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104) is the frozen October 2026 working paper. Its final source coverage now includes publication-era US 08, panel 09, **executed 09b/09c and 10**, matching frozen US/G10 derived inputs, final control tables, scripts and vector figures.

**Remaining external input gap:** the exact raw GSW `feds200628.csv` and ALFRED `CPIAUCSL_all_vintages.csv` original upload were not in the recovered final master ZIP. Do not claim full raw-data replay of those branches; see [replication guide](replication_guide.md).

## Maintenance only (not new science)

1. If the original ALFRED matrix and raw GSW file are recovered, verify their provenance / source hashes and integrate them under an explicit data-redistribution decision. Do not replace them with unverified revised versions.
2. If the original code needs portable execution, add **wrappers or environment instructions** without silently altering the frozen executed notebooks.
3. Keep SSRN as the sole distribution source of the full paper; keep descendant research independent.

## Independent descendants

- [Sparse Curve Allocation](https://github.com/svr-L/macroanchor-sparse-curve-allocation) — sparse non-neutral tenor allocation based on the parent signal.
- [Intra-Curve Relative Value](https://github.com/svr-L/macroanchor-intra-curve-relative-value) — same-country cross-tenor DV01-neutral research.
- [Inter-Curve Relative Value](https://github.com/svr-L/macroanchor-inter-curve-relative-value) — cross-country sovereign residual RV with credit-risk diagnostics.

These are not alternative versions of the 2026 parent empirical forecasting paper. They should not rewrite its validated historical conclusions.
