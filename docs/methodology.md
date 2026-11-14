# Methodology and interpretation

This document summarizes the research objects in [the paper hosted on SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104). The linked paper takes precedence over earlier notebook prose.

## 1. Slowly moving macroeconomic central tendency

The nominal anchor is a sum of two statistical states:

```text
pi_e(t)   = EWMA_36[ CPI(t)/CPI(t−12) − 1 ]
r_star(t) = EWMA_120[ r_3m(t) − pi_e(t) ]
theta(t)  = r_star(t) + pi_e(t)
```

Half-lives are months. `r_star` is a neutral-rate **proxy**, not a structural estimate of the equilibrium real rate. The nominal anchor contains **no long-yield term premium** by construction.

## 2. From a failed direct gap to short-rate dynamics

A direct gap between observed 10Y yields and the anchor has strong in-sample explanatory power but `R²_OOS = −0.445` in the canonical common-window forecast comparison. The hypothesis does **not** require ten-year yields to mechanically converge to the anchor in one year.

Instead the state enters a Gaussian short-rate process under the physical measure:

```text
dr_t = kappa × (theta_t − r_t) dt + sigma dW^P_t
```

The model estimates `kappa` and `sigma` from short-rate time-series data. It does not recalibrate to match the current yield curve. At a forecast origin, the macro state is held locally fixed over the bond-pricing horizon.

The physical parameters are reused for a **zero-market-price-of-risk counterfactual** to obtain a model-implied pure-expectations yield `y_PE(t, tau)`; then:

```text
TP_model(t, tau) = y_observed(t, tau) − y_PE(t, tau)
```

This difference is **not structurally identified term premium**; it can contain model misspecification, liquidity and measurement effects. The point is to test its predictive content, not to claim complete P/Q identification.

## 3. Bond-return targets, forecasting and inference

- Primary US inputs: 1Y–10Y constant-maturity Treasury yields, a three-month Treasury bill rate, CPI, and an external Kim–Wright 10Y term-premium series. Gürkaynak–Sack–Wright zero-coupon Treasury curves supply the exact zero-coupon return branch.
- Distinct target definitions: CMT holding-period approximations, exact GSW zero-coupon holding-period returns and duration-approximated 10Y returns. The latter is necessary for the international panel and is **not** an exact zero-coupon return.
- Prediction: expanding-window regressions (120-month initial estimation window); historical expanding mean as forecast benchmark; overlapping 12-month targets.
- Evaluation: realized `R²_OOS`, Clark–West statistics with HAC/Newey–West handling of overlap, and conditional moving-block bootstrap for the main nested US comparisons.
- The 2Y–10Y CMT basket provides modest/marginal evidence. The strongest US results are concentrated at the 10Y zero-coupon target; claims are target-specific.

## 4. Timing, real-time data and international validity

The final-paper vintage check uses **ALFRED CPI histories rebuilt as-of each forecast origin**, not merely a one-month release-lag shift. The latter exists in older notebook 01 but is not the final test. The 10Y CMT standalone `R²_OOS` is stable (`0.0985 → 0.0986`), **whereas nested yield-level incremental significance falls** (Clark–West `3.15 → 0.84`). Do not combine revised-data strong incremental claims with vintage-real-time language.

The G10 international result uses nine **usable** developed-market countries after sample restrictions; OECD MEI inputs are revised historical observations and results are pseudo-OOS. It includes month and country fixed effects, Driscoll–Kraay uncertainty, local yield/slope controls and portfolio-sort diagnostics. Countries share global shocks and must not be counted as independent experiments.

Primary US duration timing at 2bp produces a higher net Sharpe than static duration, but the preregistered combined economic-value criterion is **not met** because the certainty-equivalent gain is negative.

## 5. Design sensitivity, model uncertainty and scope

The study reports how tenor choice, target mechanics, funding, initial sample and anchor initialization affect apparent predictability. The estimated mean-reversion speed is especially dependent on the earliest interest-rate history; 10-year rolling estimates are near zero in part of the middle sample.

The public repository contains the historical notebooks and the 08/09 paper-era subset, **not** the final executed 09b/09c/10 code and pinned input bundle. See [replication guide](replication_guide.md) for an exact audit. The research in the separate [sparse allocation](https://github.com/svr-L/macroanchor-sparse-curve-allocation), [intra-curve RV](https://github.com/svr-L/macroanchor-intra-curve-relative-value), and [inter-curve RV](https://github.com/svr-L/macroanchor-inter-curve-relative-value) repositories belongs to independent downstream questions; none changes the frozen claims of this paper.
