import numpy as np, pandas as pd, math, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
P = ROOT / 'g10_panel_model_objects.csv'
df=pd.read_csv(P, parse_dates=['date']).sort_values(['country','date']).reset_index(drop=True)
MINW=120; NW_LAG=12

def past_only_z(x,minobs=120):
    x=np.asarray(x,float); z=np.full(len(x),np.nan)
    for t in range(minobs,len(x)):
        hist=x[:t]; hist=hist[np.isfinite(hist)]
        if len(hist)<minobs or not np.isfinite(x[t]): continue
        sd=hist.std(ddof=1)
        if sd>1e-12: z[t]=(x[t]-hist.mean())/sd
    return z
for col in ['y10','slope']:
    df[col+'_z_past']=df.groupby('country', group_keys=False)[col].transform(lambda s: pd.Series(past_only_z(s.to_numpy(), MINW), index=s.index))
analysis=df.dropna(subset=['rx','tp','tp_z_past']).copy()

def alternating_absorb(d, cols, groups, tol=1e-11,max_iter=500):
    z=d[cols].astype(float).copy()
    for _ in range(max_iter):
        old=z.to_numpy(copy=True)
        for g in groups:
            z=z-z.groupby(d[g]).transform('mean')
        diff=np.nanmax(np.abs(z.to_numpy()-old))
        if diff<tol: break
    return z

def driscoll_kraay(y,X,dates,lag=12):
    y=np.asarray(y,float); X=np.asarray(X,float); dates=pd.to_datetime(np.asarray(dates))
    if X.ndim==1:X=X[:,None]
    m=np.isfinite(y)&np.isfinite(X).all(axis=1)&pd.notna(dates)
    y,X,dates=y[m],X[m],dates[m]
    beta=np.linalg.lstsq(X,y,rcond=None)[0]; e=y-X@beta; bread=np.linalg.pinv(X.T@X)
    score_df=pd.DataFrame(X*e[:,None]); score_df['date']=dates
    G=score_df.groupby('date').sum().sort_index().to_numpy(float)
    S=G.T@G
    for ell in range(1,min(lag,len(G)-1)+1):
        w=1.0-ell/(lag+1.0); Gamma=G[ell:].T@G[:-ell]; S+=w*(Gamma+Gamma.T)
    V=bread@S@bread; T=len(np.unique(dates)); k=X.shape[1]
    if T>k: V*=T/(T-k)
    se=np.sqrt(np.maximum(np.diag(V),0))
    return beta,se,V,int(len(y)),int(T)

def panel_fit(data,x_cols):
    d=data[['date','country','rx']+x_cols].dropna().copy(); cols=['rx']+x_cols
    z=alternating_absorb(d,cols,['country','date'])
    b,se,V,n,T=driscoll_kraay(z['rx'].to_numpy(),z[x_cols].to_numpy(),d['date'],12)
    return pd.DataFrame({'beta':b,'se_DK':se,'t_DK':b/se}, index=x_cols),n,T
models={
    'TP only':['tp_z_past'],
    'TP + local yield level':['tp_z_past','y10_z_past'],
    'TP + local slope (carry)':['tp_z_past','slope_z_past'],
    'TP + level + slope':['tp_z_past','y10_z_past','slope_z_past'],
}
rows=[]
for name,xs in models.items():
    r,n,T=panel_fit(analysis,xs)
    for x,row in r.iterrows(): rows.append({'model':name,'variable':x,**row.to_dict(),'n':n,'T':T})
out=pd.DataFrame(rows)
print('full model hash',hashlib.sha256(P.read_bytes()).hexdigest())
print('analysis obs',len(analysis), 'months',analysis.date.nunique(), 'countries',analysis.country.nunique())
print(out.to_string(index=False,float_format=lambda x:f'{x:.6f}'))
out.to_csv(ROOT/'table_panel_carry_value_controls.csv',index=False)
# check common sample across all 3 controls and original on same sample
common=analysis.dropna(subset=['tp_z_past','y10_z_past','slope_z_past','rx'])
print('\ncommon sample:',len(common),common.date.nunique())
for xs in [['tp_z_past'],['tp_z_past','y10_z_past'],['tp_z_past','slope_z_past'],['tp_z_past','y10_z_past','slope_z_past']]:
    r,n,T=panel_fit(common,xs); print(xs, '\n',r, 'n',n,'T',T)
