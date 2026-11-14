# Notebook lineage and publication-era execution

The first six notebooks document the historical build-up. **The October 2026 final manuscript is represented by notebooks 08, 09, 09b, 09c and 10.** This repository includes the final **executed** 09b/09c/10 originals and their retained output cells; they were not fabricated from manuscript tables.

| File | Content | Provenance |
|---|---|---|
| `00_capstone_overview.ipynb` | Project origins and research map | Historical |
| `01_affine_short_rate_us.ipynb` | Initial affine model, CPI release-lag proxy | Historical; **not** the ALFRED full-vintage test |
| `02_us_reconciliation_ladder.ipynb` | US target/tenor reconciliation | Historical |
| `03_us_row_by_row_audit.ipynb` | Row-by-row source audit | Historical |
| `04_g10_panel_replication.ipynb` | Early G10 pseudo-OOS panel | Historical |
| `05_g10_panel_us_diagnostics.ipynb` | Panel-US comparison | Historical |
| `08_macroanchor_bond_risk_premia.ipynb` | US zero-coupon, nested tests, benchmark controls | Same research source as final master, retaining public Colab upload helper/output cells |
| `09_g10_panel_dependence_and_global_factors.ipynb` | G10 dependence, factors and cross-sectional controls | Same source code as final master; retains historical execution outputs |
| `09b_panel_carry_value_controls_executed.ipynb` | G10 carry/value controls | **Byte-identical to 18 Oct final master, executed** |
| `09c_us_regime_intercepts_correction.ipynb` | Regime/intercept correction | **Byte-identical to 18 Oct final master, executed** |
| `10_vintage_costs_crosssection_executed.ipynb` | Full CPI as-of vintage, net-of-cost duration timing, cross-country long/short | **Byte-identical to 18 Oct final master, executed** |

Hash-pinned `paper_config_monthly_panel.csv` and `g10_panel_model_objects.csv` are included in `../data/frozen/`. For notebooks that expect a file in their working directory, run `python scripts/stage_frozen_inputs.py --dest notebooks` **from the repository root** (no notebook code is changed). Start Jupyter in `notebooks/`; a script can also be run from repository root after staging the inputs there.

The **raw GSW/FEDS file** and the **original ALFRED CPI vintage matrix** remain external. They are documented in [the data sources](../docs/data_sources.md) and [replication guide](../docs/replication_guide.md). The retained output cells are an execution record, **not** proof that every analysis can be replayed with this ZIP alone.

Portfolio/TAA exploration in `../extensions/` is historical. Updated investing and RV engines live in the three separately linked descendant repos in [the root README](../README.md#related-repositories).
