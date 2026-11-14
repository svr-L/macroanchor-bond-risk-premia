#!/usr/bin/env python3
"""Copy hash-verified frozen derived inputs into the notebooks' working folder.

The original executed notebooks are not modified. No downloads are performed.
Usage from repository root: python scripts/stage_frozen_inputs.py --dest notebooks
"""
import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "paper_config_monthly_panel.csv": "67ed3093d17cf5ed849a8cfa3fa95ac5fb2c1f47d58a69110f96a366a1fbd7f5",
    "g10_panel_model_objects.csv": "1628c4eaff487f6d87cc93fe62c7af909850d9ceedf448d9d8321f8b8477bbf6",
}

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--dest',default='notebooks',help='relative path under repo root (default notebooks)')
    args=ap.parse_args()
    dest=(ROOT/args.dest).resolve()
    if ROOT not in dest.parents and dest != ROOT:raise ValueError('Destination must remain within repository')
    dest.mkdir(parents=True,exist_ok=True)
    for name,sha in EXPECTED.items():
        src=ROOT/'data'/'frozen'/name
        if digest(src)!=sha:raise ValueError(f'Frozen input digest mismatch: {name}')
        tgt=dest/name
        if tgt.exists() and digest(tgt)!=sha:
            raise ValueError(f'Existing {tgt} differs from frozen input; refusing to overwrite')
        if not tgt.exists():tgt.write_bytes(src.read_bytes())
        print(f'OK {name}: {sha[:16]}... staged in {dest.relative_to(ROOT)}')

if __name__=='__main__':main()
