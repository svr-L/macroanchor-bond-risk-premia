# Data layout

- `frozen/` — **included**, hash-verified derived canonical US and model-ready G10 panels used in the final October 2026 manuscript. Public-source derived inputs are frozen; do not modify them when claiming a replication.
- `raw/` — user-supplied external raw sources (not bundled): especially the exact GSW `feds200628.csv` and ALFRED `CPIAUCSL_all_vintages.csv` used for full-source replay.
- `cache/` — optional exploratory public-data downloads; do not substitute these for the fixed input lineage.

From root, `python scripts/stage_frozen_inputs.py --dest notebooks` copies and validates the two supplied snapshots into the working notebook folder. Staged files are ignored by Git; source files in `frozen/` remain unchanged. See [data provenance](../docs/data_sources.md).
