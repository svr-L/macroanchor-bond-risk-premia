# Final-paper replication and evidence coverage (14 November 2026)

**Manuscript:** [MacroAnchor on SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104). The paper PDF and TeX are deliberately excluded from this repository.

## 1. Actual source coverage

This release **includes** the final executed notebook sources for the previously missing tests:

| Manuscript evidence | Code/data included | Re-execution caveat |
|---|---|---|
| Baseline short-rate model, in-sample/raw gap, US CMT | 01–03 and publication-era 08, frozen US CSV | Earlier 01–03 are historical; rely on final 08 for publication-era definitions |
| GSW zero-coupon 10Y, canonical benchmark/nested US tests | 08 source and frozen US CSV | Original hash-pinned `feds200628.csv` **not included** |
| G10 dependence / two-way FE / global-factor tests | 09 source and frozen G10 CSV | Source code and panel snapshot supplied |
| Final G10 carry/value controls | **09b executed**, frozen G10 CSV, control script, exported final table | All included; archived output verified by source checksum |
| US regime/intercept correction | **09c executed**, frozen G10 CSV, exported final table | All included; archived output verified by source checksum |
| Full CPI ALFRED as-of-vintage test | **10 executed**, frozen US CSV | Exact original ALFRED vintage matrix **not included**; vintage section cannot be faithfully re-executed from ZIP alone |
| US net-of-cost timing and international sort | **10 executed**, frozen US and G10 CSVs | Source and recorded outputs present; independent replay not claimed in this release |
| Vector figure exports | `results/final_paper/figures/`, source script `scripts/rebuild_vector_figs.py` | Figure production may need input paths adjusted; files are archived originals |

**Input SHA-256 recorded in the final master:**

- `data/frozen/paper_config_monthly_panel.csv`: `67ed3093d17cf5ed849a8cfa3fa95ac5fb2c1f47d58a69110f96a366a1fbd7f5`
- `data/frozen/g10_panel_model_objects.csv`: `1628c4eaff487f6d87cc93fe62c7af909850d9ceedf448d9d8321f8b8477bbf6`
- Original `feds200628.csv` (not bundled): `c3541ab54e054c0bcc3c17bbe038a3129da2c26486ef3c255e2378d7d63aa9c4`
- Original `CPIAUCSL_all_vintages.csv`: used in the final 10 execution **but not byte-hashed at that time**; no digest is invented.

Original final-master checksums are preserved in `final_master_CHECKSUMS_SHA256.txt`; `09b`, `09c`, `10` match exactly. Final manuscript-specific results are not reassigned to early notebooks.

## 2. Reproducing checks with the available inputs

From repository root:

```bash
python scripts/verify_release.py
python scripts/stage_frozen_inputs.py --dest notebooks
cd notebooks
jupyter lab
```

- `stage_frozen_inputs.py` copies the two frozen datasets into the working notebook folder, verifies their SHA-256 hashes, and does not modify the originals or any `.ipynb`.
- In the classic Jupyter environment, execute 09b and 09c from `notebooks/` to reproduce the controls on the supplied G10 panel.
- Notebook 10 uses an interactive file-discovery/upload setup and can run the US/panel stages using the supplied snapshots; its ALFRED section needs the exact vintage upload used in the archived execution. Do **not** silently substitute a later ALFRED download when claiming numerical identity.
- Notebook 08's **GSW zero-coupon branch** needs the exact hash-matched raw FEDS file and is not complete from the frozen CMT snapshot alone.
- Many earlier notebooks also make independent live public-data calls, so their output may change after public-data revisions.

**Local validation completed on 14 November 2026:** 09b and 09c re-executed successfully on the supplied frozen panel, including 09c hard asserts. Notebook 10 re-executed successfully for synthetic self-tests, the US snapshot baseline, US net-of-cost timing and G10 long/short portfolio sorts; the as-of CPI vintage section skipped because the original ALFRED file is absent. No full GSW/ALFRED raw-source replay or complete nested-bootstrap replay was performed. The original executed notebooks are preserved unmodified.

## 3. Scientific interpretation

US vintage-real-time robustness applies only to the CPI reconstruction **actually tested**; the international panel remains pseudo-OOS because its macro inputs are revised. The 10Y standalone CMT performance remains positive under the as-of reconstruction, but the nested yield-level Clark–West significance degrades. Net US duration-timing value does **not** satisfy the preregistered CE criterion. Preserve these limits when citing the SSRN study.
