# Corrected source and code audit — 14 November 2026

**Supersedes the incomplete documentation-only update made earlier on 14 November.** The source archive supplied as the 'old repository' was correctly a prior version, **not** a statement that its subset represented the latest scientific work. This corrected package integrates existing final research materials, preserving original bytes.

## Integrated originals, recovered from `MacroAnchor_FINAL_PERSONAL_2026-10-18.zip`

| File | SHA-256 (complete) |
|---|---|
| `notebooks/09b_panel_carry_value_controls_executed.ipynb` | `90aa6e5ce88ea823739b45ac89d3a03c3c191f76edfeb1cd7325328af35e3316` |
| `notebooks/09c_us_regime_intercepts_correction.ipynb` | `4f98a9fde88e04b454bc46ce5dd86ff795a2eb81b8164531bedc6c2f067301b8` |
| `notebooks/10_vintage_costs_crosssection_executed.ipynb` | `5dd9475b14afe68f99b14ce4e11a524108335c09116250cf7bd8d80cd1d87fc0` |

Also added: SHA-256-verified `paper_config_monthly_panel.csv` and `g10_panel_model_objects.csv`; executed-control exported tables; original `run_panel_controls.py`, `rebuild_vector_figs.py` and seven vector figure PDFs. No manuscript PDF or TeX is present. Original 00–05/08/09/06/07 notebook bytes have **not** been changed from the supplied repository ZIP; 09's code matches the final-master 09 v7; 08's code matches after excluding its additional public Colab upload-helper cell.

## Actual remaining gaps

- The original raw GSW/FEDS source (`feds200628.csv`), SHA-256 `c3541ab54e054c0bcc3c17bbe038a3129da2c26486ef3c255e2378d7d63aa9c4`, was not in the final master archive.
- The exact ALFRED CPI vintage upload (`CPIAUCSL_all_vintages.csv`) was not present and was not originally hashed in notebook 10. We preserve its archived executed outcomes, **without claiming an exact independent replay of those vintage results**.
- **Independent local replay performed:** 09b and 09c both executed successfully with `nbclient` against the included G10 snapshot; 09b reproduced the main panel coefficient β = 0.018547 and the local-controls outputs, and 09c passed its hard manuscript-value assertions. Notebook 10 executed successfully against the included US and G10 snapshots: its synthetic self-tests passed, the canonical basket result reproduced (`R²_OOS = +0.0163`, CW `t = 1.366`, `n = 336`), the economic-value section matched the manuscript (linear net SR at 2bp = 0.50; CE gain −0.0140) and the country long–short section matched (top-3/bottom-3 mean = 0.96%, NW `t = 2.80`). Its CPI-as-of/ALFRED section **explicitly skipped** because the original vintage matrix is missing. The replays were run on temporary in-memory notebook copies; the submitted executed original notebooks remain byte-identical to the final master. No full 08/09 end-to-end bootstrap or missing raw-source replay was attempted.

## Release verification

Run `python scripts/verify_release.py` and optionally `python scripts/stage_frozen_inputs.py --dest notebooks`. The first checks byte provenance and notebook format; the second copies verified data for notebook-local loading. Both are offline, and neither mutates executed research sources.

The repository's original `.pdf` and `.tex` manuscript files are excluded. SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104.
