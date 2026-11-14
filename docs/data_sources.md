# Data sources and provenance

The parent paper is on [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7684104). This release now includes the *final derived frozen US and G10 input snapshots*, unlike the earlier public repository, but it is not a complete archive of all **raw** inputs.

## Included hash-verified derived data

| File | Location | SHA-256 |
|---|---|---|
| US canonical monthly panel | `data/frozen/paper_config_monthly_panel.csv` | `67ed3093d17cf5ed849a8cfa3fa95ac5fb2c1f47d58a69110f96a366a1fbd7f5` |
| G10 model-ready panel | `data/frozen/g10_panel_model_objects.csv` | `1628c4eaff487f6d87cc93fe62c7af909850d9ceedf448d9d8321f8b8477bbf6` |

The hashes match the **original final personal master** of 18 October 2026, not a fresh download. Snapshot availability facilitates checks of 09b, 09c and parts of 10.

## Raw sources and remaining limitations

- US yields: FRED Treasury constant maturity and 3-month bill, Gürkaynak–Sack–Wright Fed zero-coupon curve. Historical CPI: CPIAUCSL (FRED/ALFRED). The canonical raw GSW `feds200628.csv` expected SHA-256 is `c3541ab54e054c0bcc3c17bbe038a3129da2c26486ef3c255e2378d7d63aa9c4`; **not supplied** in recovered archive.
- Full-vintage CPI: final executed 10 uses ALFRED `CPIAUCSL_all_vintages.csv` with 669 vintage releases through September 11, 2026. Its upload was **not hashed by that notebook** and is **not included** here. Early notebook 01 instead uses a lag proxy — it does not reproduce full as-of CPI history.
- International panel: OECD Main Economic Indicators via FRED; nine usable countries (Japan excluded due to insufficient usable forecast history). Australia and New Zealand rely on quarterly CPI with release timing; country-level returns are duration approximations. The panel is based on **revised historical macro data**, hence pseudo-OOS.

Live public-series downloads can lead to different values. No current download should silently replace a frozen source, and no hash for the original ALFRED upload has been fabricated.
