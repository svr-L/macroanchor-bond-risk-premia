#!/usr/bin/env python3
"""Offline integrity audit; does not execute empirical notebooks or fetch data."""
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
    'notebooks/09b_panel_carry_value_controls_executed.ipynb':'90aa6e5ce88ea823739b',
    'notebooks/09c_us_regime_intercepts_correction.ipynb':'4f98a9fde88e04b454bc',
    'notebooks/10_vintage_costs_crosssection_executed.ipynb':'5dd9475b14afe68f99b14ce4e11a5241',
    'data/frozen/paper_config_monthly_panel.csv':'67ed3093d17cf5ed849a8cfa3fa95ac5fb2c1f47d58a69110f96a366a1fbd7f5',
    'data/frozen/g10_panel_model_objects.csv':'1628c4eaff487f6d87cc93fe62c7af909850d9ceedf448d9d8321f8b8477bbf6',
}
# Precise full hashes are verified from the final master by the release audit.
for p,prefix in EXPECTED.items():
    b=(ROOT/p).read_bytes();sha=hashlib.sha256(b).hexdigest()
    if not sha.startswith(prefix):raise SystemExit(f'FAIL {p}: {sha} != prefix {prefix}')
    if p.endswith('.ipynb'):
        nb=json.loads(b)
        if nb.get('nbformat')!=4:raise SystemExit(f'FAIL notebook format {p}')
    print(f'OK {p}: {sha}')
assert not any('manuscript' in x.name.lower() for x in ROOT.rglob('*.pdf'))
assert not any('manuscript' in x.name.lower() for x in ROOT.rglob('*.tex'))
print('Offline integrity checks passed. Does not assert raw-source or full numerical replay.')
