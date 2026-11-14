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

The values below are **from the final October 2026 manuscript** linked above. The original **executed final-paper notebooks 09b, 09c, and 10**, hash-matched frozen US and G10 CSV inputs, controls scripts and final output tables are included here. **The original ALFRED CPI vintage matrix and frozen GSW source file are not**; see the [evidence-coverage audit](docs/replication_guide.md).

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

**Publication-era scientific source is now included, not only described.** The notebook numbering retains the research lineage. The original final-paper 09b/09c/10 notebooks are included **byte-for-byte** from the author-identifiable final research master of 18 October 2026, with their archived execution outputs. The earlier 08/09 public notebooks retain their own recorded outputs; their analytical code matches the corresponding final-master sources (08 also contains a Colab upload helper cell).

| Path | Scope |
|---|---|
| [`notebooks/00`–`05`](notebooks/README.md) | Historical US short-rate/target reconciliation and G10 development; not replacements for the final executed analyses. |
| [`notebooks/08_macroanchor_bond_risk_premia.ipynb`](notebooks/08_macroanchor_bond_risk_premia.ipynb) | Paper-era US model/GSW zero-coupon/benchmark/nested forecast tests. **Exact GSW raw input is still needed** for its GSW branch. |
| [`notebooks/09_g10_panel_dependence_and_global_factors.ipynb`](notebooks/09_g10_panel_dependence_and_global_factors.ipynb) | Paper-era G10 panel, dependence and global-factor regressions. |
| [`notebooks/09b_panel_carry_value_controls_executed.ipynb`](notebooks/09b_panel_carry_value_controls_executed.ipynb) | **Final executed** G10 local carry/value controls; archived outputs present. |
| [`notebooks/09c_us_regime_intercepts_correction.ipynb`](notebooks/09c_us_regime_intercepts_correction.ipynb) | **Final executed** US regime/intercept correction; archived outputs present. |
| [`notebooks/10_vintage_costs_crosssection_executed.ipynb`](notebooks/10_vintage_costs_crosssection_executed.ipynb) | **Final executed** ALFRED real-time, US economic-value and cross-country sort analyses; archived outputs present. Full vintage **re-execution** additionally needs the original ALFRED CPI file. |
| [`data/frozen/`](data/frozen/) | Hash-matched **final frozen US and G10 derived inputs**. |
| [`results/final_paper/`](results/final_paper/) | Final control tables and exported vector figures; no manuscript PDF or TeX. |
| [`scripts/`](scripts/) | Original panel-control and figure-production scripts, plus input staging and validation. |
| [`extensions/`](extensions/README.md) | Legacy exploratory TAA / curve-RV notebooks; not the mature descendant projects. |

**Provenance:** `09b` SHA-256 `90aa6e5c…`, `09c` `4f98a9fd…`, `10` `5dd9475b…` (full digests in [release audit](docs/repo_audit_2026-11-14.md)). The two frozen CSV input SHA-256 values match the final manuscript. Neither raw `feds200628.csv` nor the **unhashed original** `CPIAUCSL_all_vintages.csv` is part of this delivery; results requiring those files are preserved **as executed notebook outputs**, not newly re-executed or claimed fully independently reproducible. See the [replication guide](docs/replication_guide.md).

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
