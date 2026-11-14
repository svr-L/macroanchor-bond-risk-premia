# Macro-Anchored Bond Risk Premia

**Research code and empirical audit for:**  
*The Macro Anchor as a Short-Rate Central Tendency: Bond Risk Premia and an Empirical-Design Decomposition* (2026).

**[Read or download the working paper on SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104)** · [Research methodology](docs/methodology.md) · [Replication and evidence coverage](docs/replication_guide.md) · [Research lineage](#related-repositories)

**Paper-hosting policy:** The manuscript is distributed **on SSRN**, not in this repository. This repository contains research notebooks and documentation; the PDF and LaTeX manuscript are deliberately not mirrored here.

## Research question and economic mechanism

Can a slow-moving nominal macro anchor — a proxy for the neutral real short rate plus trend inflation — help forecast sovereign-bond excess returns? The distinction is **how the macro state is used**, not simply whether it is correlated with long yields.

1. **The direct gap fails.** A raw ten-year yield–anchor gap exhibits strong in-sample fit but fails a recursive out-of-sample forecasting test (`R²_OOS = −0.445` in the canonical common-window comparison).
2. **The state is embedded in short-rate dynamics.** A Hull–White-type Gaussian short-rate process, estimated under the physical measure, reverts toward the slow macro anchor rather than assuming that the ten-year yield itself should quickly revert to the anchor.
3. **The predictor is a model-implied wedge.** The difference between the observed sovereign yield and the model's zero-market-price-of-risk, pure-expectations yield is used to forecast bond excess returns. It is a **model-implied term-premium signal**, **not** a structurally identified term premium: model error, liquidity and measurement effects can also contribute.

For the construction used in the paper:

```text
trend_inflation_t  = EWMA_36(12-month CPI inflation)
r_star_proxy_t     = EWMA_120(three-month bill rate − trend_inflation_t)
theta_t            = r_star_proxy_t + trend_inflation_t

dr_t               = kappa × (theta_t − r_t) dt + sigma dW_t^P
signal(t, tau)     = observed_yield(t, tau) − pure_expectations_yield(t, tau)
```

The two EWMAs have half-lives of 36 and 120 months. This is a transparent statistical proxy, **not** an estimate of the Holston–Laubach–Williams neutral rate. See [methodology](docs/methodology.md) for target and evaluation details.

## Main findings from the working paper

The values below are **from the final October 2026 manuscript** linked above. The notebook subset distributed in this repository does **not** independently reproduce every final paper table; see the [evidence-coverage audit](docs/replication_guide.md).

| Research test | Paper result and interpretation |
|---|---|
| Direct 10Y anchor gap | Strong in-sample fit, **`R²_OOS = −0.445`** on the canonical common window: an economic narrative alone does not ensure a reliable forecast. |
| Macro-anchored short-rate wedge, CMT 2Y–10Y basket | **`R²_OOS = +0.0163`**, positive but marginal (conditional block-bootstrap p ≈ 0.086). |
| Macro-anchored wedge, 10Y GSW zero-coupon | **`R²_OOS = +0.1553`**, Clark–West **`t = 3.12`** on final data. Evidence is concentrated at the long end. |
| 10Y CMT, reconstructed ALFRED CPI vintages | Standalone **`R²_OOS = 0.0985 → 0.0986`**; the nested yield-level Clark–West statistic **falls from 3.15 to 0.84**. Standalone predictability survives this as-of reconstruction; **incremental predictability does not pass the declared real-time test**. |
| International developed-market panel | Nine usable countries; positive country-level slopes in 9/9 and positive pseudo-OOS `R²` in 6/9. Two-way fixed-effects coefficient **`β = 0.0185`** (Driscoll–Kraay `t = 4.84`); with local yield-level and slope controls **`β = 0.0134`** (`t = 3.08`). Panel inputs are revised, not fully vintage-real-time. |
| US duration-timing economics | At 2 bp, the primary linear rule has net Sharpe 0.50 vs 0.42 for static duration, but its certainty-equivalent gain is **negative**; the preregistered economic success criterion is **not met**. |
| Model sensitivity | Target construction, tenor and sample history materially influence results; the short-rate mean-reversion estimate is sensitive to the early sample. The study reports these choices rather than selecting a best-looking specification. |

**Reading the evidence:** this is research into **conditional predictive information** and empirical-design sensitivity, not a guarantee of investable alpha or a claim that all tenors, vintage definitions or implementation rules work equally well. In particular, the GSW 10Y final-data result and the ALFRED CMT 10Y test are **different target constructions**; they are not interchangeable.

## Repository contents and evidence status

This repository has **two layers**. The archived exploratory notebooks document how the project evolved; the later 08–09 notebooks add a subset of publication-era diagnostics. A number of final-manuscript analyses were executed separately and **are not present in this uploaded repository snapshot**. The numbers in the table above are sourced to the [paper on SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104), not attributed to absent code.

| Path | Scope |
|---|---|
| [`notebooks/00_capstone_overview.ipynb`](notebooks/00_capstone_overview.ipynb) | Historical research map: original rates/TAA exploration and model lineage, not the final paper's replication entrypoint. |
| [`notebooks/01_affine_short_rate_us.ipynb`](notebooks/01_affine_short_rate_us.ipynb) | US short-rate model, affine yields and early diagnostics; includes a **release-lag proxy**, not the final ALFRED full-vintage study. |
| [`notebooks/02_us_reconciliation_ladder.ipynb`](notebooks/02_us_reconciliation_ladder.ipynb) | Reconciliation of different US return-target constructions and common-window choices. |
| [`notebooks/03_us_row_by_row_audit.ipynb`](notebooks/03_us_row_by_row_audit.ipynb) | Month-by-month checks of the US versus G10 panel input/target definitions. |
| [`notebooks/04_g10_panel_replication.ipynb`](notebooks/04_g10_panel_replication.ipynb) | Early international replication, using revised data and approximate 10Y returns. |
| [`notebooks/05_g10_panel_us_diagnostics.ipynb`](notebooks/05_g10_panel_us_diagnostics.ipynb) | US panel row diagnostics and sample-construction differences. |
| [`notebooks/08_macroanchor_bond_risk_premia.ipynb`](notebooks/08_macroanchor_bond_risk_premia.ipynb) | Publication-era US robustness, curve/return construction, forecasting and benchmark comparisons; requires archived external inputs. |
| [`notebooks/09_g10_panel_dependence_and_global_factors.ipynb`](notebooks/09_g10_panel_dependence_and_global_factors.ipynb) | Publication-era G10 dependence, fixed effects, factor and cross-sectional tests; requires archived external inputs. |
| [`extensions/06_taa_overlay_diagnostics.ipynb`](extensions/06_taa_overlay_diagnostics.ipynb) | Earlier tactical-allocation/synthetic diagnostics, not the latest separate allocation study. |
| [`extensions/07_curve_rv_extension_v1.ipynb`](extensions/07_curve_rv_extension_v1.ipynb) | Early within-curve RV exploration; **not** the current stand-alone intra-curve project. |

**Not in this snapshot:** the final executed `09b` carry/value controls, `09c` regime/intercept correction, `10` full-ALFRED-vintage/economic-value/cross-country-sort notebook, and their complete hash-pinned input bundle. They are referenced in the manuscript but have **not been fabricated or reconstructed** here. See [replication guide](docs/replication_guide.md).

## Related repositories

These are **independent research descendants**, not components that must be installed for the parent forecasting model. They share the MacroAnchor economic signal but answer **different portfolio-construction questions**:

| Repository | How it develops the parent research |
|---|---|
| **[MacroAnchor Sparse Curve Allocation](https://github.com/svr-L/macroanchor-sparse-curve-allocation)** | Translates the parent cross-tenor excess-return forecasts into sparse, cost-aware tenor allocations. Uses conditional volatility / DV01 / tail-risk constraints and spanning tests; **not** a duration-neutral relative-value strategy. |
| **[MacroAnchor Intra-Curve Relative Value](https://github.com/svr-L/macroanchor-intra-curve-relative-value)** | Searches for residual mispricing **between maturities on the same sovereign curve**, with DV01 neutrality, curve-factor exposure checks and transaction-cost stress tests. It supersedes the exploratory `extensions/07` notebook as a separate line of research. |
| **[MacroAnchor Inter-Curve Relative Value](https://github.com/svr-L/macroanchor-inter-curve-relative-value)** | Compares MacroAnchor residuals **across sovereign-country curves** at similar maturity, constructing cross-market DV01-neutral long/short portfolios and examining credit/country-risk diagnostics. It is distinct from within-curve butterflies and from the paper's forecasting panel. |

The parent repository asks **whether the signal forecasts bond returns**. Sparse allocation asks **how to use the forecast across tenors**; intra-curve RV asks **whether relative dislocations persist after neutralizing duration/curve exposures**; inter-curve RV asks **whether country-relative dislocations support a neutralized sovereign trade**. Positive findings in one branch do not automatically validate another.

## Getting started

```bash
conda env create -f environment.yml
conda activate macroanchor-bond-risk-premia
jupyter lab
```

Alternative installation via pip:

```bash
python -m venv .venv
# activate the environment (Windows: .venv\\Scripts\\activate)
python -m pip install -r requirements.txt
jupyter lab
```

For notebook-specific prerequisites and an honest description of **which results the committed materials can reproduce**, read [`docs/replication_guide.md`](docs/replication_guide.md) before executing a notebook. Earlier notebooks can download public inputs where supported; 08–09 expect separate source files and are **not one-click offline replications** in this archive.

## Data, reproducibility and status

- Public primary sources include FRED, ALFRED, Federal Reserve Gürkaynak–Sack–Wright Treasury curves and OECD Main Economic Indicators; market curves and published revised series are not equivalent to real-time macro vintages.
- The working paper documents frozen snapshots, code and hashes. Only a **partial historical/public notebook collection** is present here; do not interpret that as a complete independent replication package for the final manuscript.
- The original scientific result is **frozen**. Future upgrades to portfolio construction, term-premium models or multiverse methods belong in separate research lines, with explicit versioning; they do not silently replace the October 2026 results.
- No manuscript PDF or LaTeX source is distributed in this repository. **[The latest paper is hosted on SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104).**

## Disclaimer

Independent research carried out in a personal capacity. Not investment advice. The analyses and views are the author's and are not those of any employer.
