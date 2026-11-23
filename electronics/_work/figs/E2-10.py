# E2-10 figures: drain-end channel width vs VDS, ID-VDS family with pinch-off locus
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
V0 = 0.7; Voff = 4.0
# choose H/2 so that h=0 at reverse bias 4 V: W0*sqrt(1+4/V0) = Hhalf
Hh = 1.0; W0 = Hh/np.sqrt(1+Voff/V0)
fig, axs = plt.subplots(1, 2, figsize=(8.8, 2.9))
vds = np.linspace(0, 4, 300)
h = 2*(Hh - W0*np.sqrt(1+vds/V0)); h = np.maximum(h, 0)
axs[0].plot(vds, h/h[0], color='#2a6fdb', lw=2)
axs[0].axvline(4, color='#d9480f', ls=':', lw=1); axs[0].text(3.05, 0.55, '夾止\n$|V_{GS,\\mathrm{off}}|$ = 4 V', color='#d9480f', fontsize=8)
axs[0].set_xlabel('$V_{DS}$ (V)，$V_{GS}=0$'); axs[0].set_ylabel('汲極端通道寬 $h$（相對）'); axs[0].set_title('汲極端通道隨 $V_{DS}$ 變窄，4 V 時夾止', fontsize=9)
v = np.linspace(0, 10, 600)
for vgs, c in [(0, '#2a6fdb'), (-1, '#4dabf7'), (-2, '#f08c00'), (-3, '#d9480f')]:
    vov = vgs + Voff
    idv = np.where(v < vov, 2*vov*v - v**2, vov**2)
    axs[1].plot(v, idv, color=c, lw=2, label=f'$V_{{GS}}$ = {vgs} V')
loc = np.linspace(0, 4, 50); axs[1].plot(loc, loc**2, color='#888', ls='--', lw=1)
axs[1].text(0.2, 15, '歐姆區', fontsize=9); axs[1].text(6, 17.2, '放大區（平）', fontsize=9)
axs[1].text(2.6, 4.2, '夾止點\n$V_{DS} = V_{GS} - V_{GS,\\mathrm{off}}$', fontsize=7.5, color='#555')
axs[1].set_xlabel('$V_{DS}$ (V)'); axs[1].set_ylabel('$I_D$'); axs[1].set_yticks([]); axs[1].legend(fontsize=7, frameon=False, loc='center right')
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-10-pinchoff.svg')); plt.close(fig)
