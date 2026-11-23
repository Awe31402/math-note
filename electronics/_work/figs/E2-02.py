# E2-02 figures: minority-carrier profiles under forward bias
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
W = 0.4; xn = np.linspace(W/2, 4, 300); xp = np.linspace(-4, -W/2, 300)
fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.plot(xn, 0.15 + 0.85*np.exp(-(xn-W/2)/0.9), color='#c92a2a', lw=2, label='n 側的電洞 $p_n(x)$')
ax.plot(xp, 0.15 + 0.6*np.exp((xp+W/2)/0.9), color='#1c7ed6', lw=2, label='p 側的電子 $n_p(x)$')
ax.axhline(0.15, xmin=0, xmax=1, color='gray', ls=':', lw=1); ax.text(2.6, 0.18, '$p_{n0}$（平衡值）', fontsize=8)
ax.axvspan(-W/2, W/2, color='#eee'); ax.text(-0.2, 0.9, '空乏區', fontsize=8)
ax.text(0.3, 1.02, '$p_{n0}e^{V/V_T}$', fontsize=9, color='#c92a2a')
ax.annotate('', (W/2+0.9, 0.12), (W/2, 0.12), arrowprops=dict(arrowstyle='<->')); ax.text(W/2+0.25, 0.04, '$L_p$', fontsize=9)
ax.set_xlabel('$x$'); ax.set_ylabel('少數載子濃度'); ax.set_yticks([]); ax.set_xticks([]); ax.set_ylim(0, 1.15)
ax.legend(fontsize=8, frameon=False, loc='upper left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-02-minority-profile.svg')); plt.close(fig)
