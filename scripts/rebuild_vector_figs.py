from pathlib import Path
import hashlib
import numpy as np, pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from statistics import NormalDist
from scipy.stats import ncx2

ROOT = Path(__file__).resolve().parent
src = ROOT / 'paper_config_monthly_panel.csv'
outdir = ROOT / 'figures'
EXPECTED_INPUT_SHA256 = '67ed3093d17cf5ed849a8cfa3fa95ac5fb2c1f47d58a69110f96a366a1fbd7f5'
actual_sha = hashlib.sha256(src.read_bytes()).hexdigest()
assert actual_sha == EXPECTED_INPUT_SHA256, (actual_sha, EXPECTED_INPUT_SHA256)
outdir.mkdir(exist_ok=True)
df=pd.read_csv(src,parse_dates=['date'])
dates=pd.DatetimeIndex(df['date'])
MATS=[1,2,3,5,7,10]
Y=df[[f'y{x}' for x in MATS]].to_numpy(float)
r=df['TB3MS'].to_numpy(float)
cpi=df['CPIAUCSL'].to_numpy(float)
kw=df['THREEFYTP10'].to_numpy(float)
Tn=len(df); MINW=120; DTm=1/12
PI_HL=36; RSTAR_HL=120
cpi_yoy=pd.Series(cpi,index=dates).pct_change(12,fill_method=None)
pi_raw=cpi_yoy.ewm(halflife=PI_HL).mean()
short_s=pd.Series(r,index=dates)
rstar=(short_s-pi_raw).ewm(halflife=RSTAR_HL).mean().bfill()
pi_trend=pi_raw.bfill()
anchor=(rstar+pi_trend).to_numpy(float)

def fit_ou(rw):
    x=rw[:-1]; y=rw[1:]; X=np.column_stack([np.ones(len(x)),x])
    c,b=np.linalg.lstsq(X,y,rcond=None)[0]; b=float(np.clip(b,1e-6,.999999))
    k=-12*np.log(b); th=float(c/(1-b)); e=y-(c+b*x)
    s2=float(np.var(e))*2*k/max(1-b*b,1e-10)
    return k,th,np.sqrt(max(s2,1e-10))
def fit_cir(rw):
    x=np.maximum(rw[:-1],1e-4); d=rw[1:]-rw[:-1]; w=1/np.sqrt(x)
    X=np.column_stack([np.ones(len(x))*w,x*w]); y=d*w
    b0,b1=np.linalg.lstsq(X,y,rcond=None)[0]
    k=float(np.clip(-b1*12,1e-4,20)); th=float(np.clip(b0*12/k,1e-4,.5))
    e=d-(b0+b1*x); s2=float(np.mean(e*e/(x*DTm)))
    return k,th,np.sqrt(max(s2,1e-10))
def fit_hw(rw,anc):
    g=anc[:len(rw)-1]-rw[:-1]; d=rw[1:]-rw[:-1]
    X=np.column_stack([np.ones(len(g)),g]); a0,sl=np.linalg.lstsq(X,d,rcond=None)[0]
    e=d-(a0+sl*g); k=float(np.clip(sl*12,1e-4,20)); s=float(np.std(e))*np.sqrt(12)
    return k,s
kOU_t=np.full(Tn,np.nan); thOU_t=np.full(Tn,np.nan); sOU_t=np.full(Tn,np.nan)
kC_t=np.full(Tn,np.nan); thC_t=np.full(Tn,np.nan); sC_t=np.full(Tn,np.nan)
kHW_t=np.full(Tn,np.nan); sHW_t=np.full(Tn,np.nan)
for t in range(MINW,Tn):
    kOU_t[t],thOU_t[t],sOU_t[t]=fit_ou(r[:t+1])
    kC_t[t],thC_t[t],sC_t[t]=fit_cir(r[:t+1])
    kHW_t[t],sHW_t[t]=fit_hw(r[:t+1],anchor[:t+1])

def Bv(tau,k): k=max(k,1e-4); return (1-np.exp(-k*tau))/k
def vas_yield(tau,rr,k,th,s):
    k=max(k,1e-4); B=Bv(tau,k)
    lnA=(th-s*s/(2*k*k))*(B-tau)-s*s*B*B/(4*k)
    return (-lnA+B*rr)/tau
def cir_yield(tau,rr,k,th,s):
    k=max(k,1e-4); s=max(s,1e-4); g=np.sqrt(k*k+2*s*s)
    eg=np.exp(g*tau); den=(g+k)*(eg-1)+2*g
    B=2*(eg-1)/den; lnA=(2*k*th/(s*s))*np.log(2*g*np.exp((k+g)*tau/2)/den)
    return (-lnA+B*rr)/tau
TAUS=np.array(MATS,float); nta=len(TAUS)
TPHW=np.full((Tn,nta),np.nan); TPOU=np.full_like(TPHW,np.nan); TPCIR=np.full_like(TPHW,np.nan)
for t in range(MINW,Tn):
    for j,tau in enumerate(TAUS):
        TPOU[t,j]=Y[t,j]-vas_yield(tau,r[t],kOU_t[t],thOU_t[t],sOU_t[t])
        TPHW[t,j]=Y[t,j]-vas_yield(tau,r[t],kHW_t[t],anchor[t],sHW_t[t])
        TPCIR[t,j]=Y[t,j]-cir_yield(tau,r[t],kC_t[t],thC_t[t],sC_t[t])

# Canonical-provenance guards for Figure 2
slope = Y[:, -1] - Y[:, 0]
mask_s = np.isfinite(TPHW[:, -1]) & np.isfinite(slope)
mask_kw = np.isfinite(TPHW[:, -1]) & np.isfinite(kw)
corr_slope = float(np.corrcoef(TPHW[mask_s, -1], slope[mask_s])[0, 1])
corr_kw = float(np.corrcoef(TPHW[mask_kw, -1], kw[mask_kw])[0, 1])
kappa_final = float(kHW_t[-1])
assert abs(kappa_final - 0.196821) < 5e-6, kappa_final
assert abs(corr_slope - 0.281472) < 5e-6, corr_slope
assert abs(corr_kw - 0.688190) < 5e-6, corr_kw
print(f'canonical guards: kappa={kappa_final:.6f}, corr_slope={corr_slope:.6f}, corr_KW={corr_kw:.6f}')

# Vector Figure 2
plt.rcParams.update({'font.size':7.5,'axes.grid':True,'grid.alpha':0.25})
fig,ax=plt.subplots(1,2,figsize=(6.5,2.3))
for nm,tp in [('HW (macro anchor)',TPHW),('OU',TPOU),('CIR',TPCIR)]:
    ax[0].plot(dates,tp[:,-1]*100,lw=1.1,label=nm)
ax[0].plot(dates,kw*100,'k--',lw=1.0,label='Kim-Wright')
ax[0].axhline(0,lw=.6,color='k'); ax[0].set_ylabel('Percent'); ax[0].legend(fontsize=6.3,ncol=2)
ax[0].set_title('Ten-year model-implied wedge')
ax[1].plot(TAUS,TPHW[-1]*100,marker='o',label='HW (macro anchor)')
ax[1].plot(TAUS,TPOU[-1]*100,marker='s',label='OU')
ax[1].plot(TAUS,TPCIR[-1]*100,marker='^',label='CIR')
ax[1].axhline(0,lw=.6,color='k'); ax[1].set_xlabel('Maturity (years)'); ax[1].set_ylabel('Percent')
ax[1].legend(fontsize=6.3); ax[1].set_title('Model-implied wedge by maturity, May 2026')
fig.tight_layout(); fig.savefig(outdir/'fig_model_tp.pdf',bbox_inches='tight'); plt.close(fig)

# Vector Figure 7 (PIT)
uOU=[]; uC=[]
for t in range(MINW,Tn-12):
    k,th,s=kOU_t[t],thOU_t[t],sOU_t[t]
    m=th+(r[t]-th)*np.exp(-k); v=s*s*(1-np.exp(-2*k))/(2*k)
    uOU.append(NormalDist(m,np.sqrt(max(v,1e-12))).cdf(r[t+12]))
    k,th,s=kC_t[t],thC_t[t],sC_t[t]
    c=2*k/(s*s*(1-np.exp(-k))); dof=4*k*th/(s*s); nc=2*c*max(r[t],1e-6)*np.exp(-k)
    uC.append(float(ncx2.cdf(2*c*max(r[t+12],1e-6),dof,nc)))
uOU=np.array(uOU); uC=np.array(uC)
fig,ax=plt.subplots(1,2,figsize=(6.5,2.0))
ax[0].hist(uOU,bins=10,range=(0,1),edgecolor='black'); ax[0].axhline(len(uOU)/10,ls='--',lw=1.0)
ax[0].set_title('PIT: Gaussian OU'); ax[0].set_xlabel('Probability integral transform'); ax[0].set_ylabel('Count')
ax[1].hist(uC,bins=10,range=(0,1),edgecolor='black'); ax[1].axhline(len(uC)/10,ls='--',lw=1.0)
ax[1].set_title('PIT: CIR'); ax[1].set_xlabel('Probability integral transform')
fig.tight_layout(); fig.savefig(outdir/'fig_pit.pdf',bbox_inches='tight'); plt.close(fig)
print('saved vector figures')
print(outdir/'fig_model_tp.pdf', (outdir/'fig_model_tp.pdf').stat().st_size)
print(outdir/'fig_pit.pdf', (outdir/'fig_pit.pdf').stat().st_size)
