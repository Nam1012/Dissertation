import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
def e0(f): return np.where(f<=50,2.0,2.0+0.085*np.clip(f-50,0,None)**0.53)
def eu(f): return np.where(f<=50,3.5,2.6+35*((90-f)/100)**4)
f=np.linspace(12,90,400)
sp={"SCB1/SCB3":22.16,"POS1":30.5,"POS2":52.5,"SCCB2":55.84}
fig,ax=plt.subplots(1,2,figsize=(10,4))
ax[0].plot(f,e0(f),"k-",label=r"$\varepsilon_{c0}$ ($\varepsilon_{c2}$)")
ax[0].plot(f,eu(f),"k--",label=r"$\varepsilon_{cu}$ ($\varepsilon_{cu2}$)")
ax[0].axvline(50,color="gray",lw=0.8,ls=":")
for n,v in sp.items():
    c="C3" if v>50 else "C0"
    ax[0].plot([v,v],[e0(v),eu(v)],"o",color=c)
    off={"SCB1/SCB3":(-20,-14),"POS1":(-4,-14),"POS2":(6,4),"SCCB2":(6,4)}[n]
    ax[0].annotate(n,(v,eu(v)),textcoords="offset points",xytext=off,fontsize=8,color=c)
ax[0].set_xlabel(r"$f'_c$ (MPa)"); ax[0].set_ylabel(r"Strain (‰)")
ax[0].set_title("(a) EC2 Table 3.1 strain limits"); ax[0].legend(fontsize=8)
for n,v in sp.items():
    a,u=float(e0(v)),float(eu(v)); e=np.linspace(0,a,100)
    s=e/a*(2-e/a); c="C3" if v>50 else "C0"
    ax[1].plot(e,s,color=c,ls="-" if v>50 else "--")
    ax[1].lines[-1].set_label(f"{n} ({v} MPa): "+r"$\varepsilon_{c0}$="+f"{a:.2f}‰, "+r"$\varepsilon_{cu}$="+f"{u:.2f}‰")
    ax[1].plot(a,1,"o",color=c,ms=4)
ax[1].set_xlabel(r"$\varepsilon_c$ (‰)"); ax[1].set_ylabel(r"$\sigma_c/f'_c$")
ax[1].set_title(r"(b) Ascending branch (parabola, n = 2 as in [D])"); ax[1].legend(fontsize=7,loc="lower right")
for x in ax: x.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("EC2_concrete_strength_effect.png",dpi=300)
