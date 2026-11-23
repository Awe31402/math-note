# E2-01 figures: band diagrams (intrinsic/n/p), pn concentration profile, barrier with forward bias
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axs = plt.subplots(1, 3, figsize=(8.4, 2.6), sharey=True)
for a, title in zip(axs, ['本質矽', 'n 型（摻磷）', 'p 型（摻硼）']):
    a.fill_between([0, 1], 1.6, 2.2, color='#dbe4ff'); a.fill_between([0, 1], -0.6, 0, color='#ffe3e3')
    a.text(0.03, 1.85, '導帶 $E_c$', fontsize=8); a.text(0.03, -0.35, '價帶 $E_v$（價電子填滿）', fontsize=8)
    a.annotate('', (0.9, 1.6), (0.9, 0), arrowprops=dict(arrowstyle='<->')); a.text(0.72, 0.75, '$E_g$', fontsize=8)
    a.set_title(title, fontsize=10); a.set_xticks([]); a.set_yticks([]); a.set_xlim(0, 1)
axs[1].plot([0.1, 0.7], [1.45, 1.45], ls='--', color='#d9480f'); axs[1].text(0.1, 1.2, '施體 $N_D$（⊕）', fontsize=8, color='#d9480f')
for x in [0.2, 0.35, 0.5, 0.65]: axs[1].plot(x, 1.75, 'o', color='#1c7ed6', ms=5)
axs[2].plot([0.1, 0.7], [0.15, 0.15], ls='--', color='#2f9e44'); axs[2].text(0.1, 0.3, '受體 $N_A$（⊖）', fontsize=8, color='#2f9e44')
for x in [0.2, 0.35, 0.5, 0.65]: axs[2].plot(x, -0.15, 'o', mfc='white', mec='#c92a2a', ms=5)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-01-bands-doping.svg')); plt.close(fig)

x = np.linspace(-1, 1, 400); W = 0.2
fig, ax = plt.subplots(figsize=(5.4, 2.8))
p = np.where(x < -W, 1e16, np.where(x > W, 1e4, np.nan)); n = np.where(x > W, 1e16, np.where(x < -W, 1e4, np.nan))
ax.semilogy(x, p, color='#c92a2a', lw=2, label='電洞 $p$'); ax.semilogy(x, n, color='#1c7ed6', lw=2, label='電子 $n$')
ax.axvspan(-W, W, color='#eee'); ax.text(-0.17, 1e9, '空乏區 $W$', fontsize=8)
ax.text(-0.95, 3e16, 'p 側：$p = N_A = 10^{16}$', fontsize=8); ax.text(0.3, 3e16, 'n 側：$n = N_D = 10^{16}$', fontsize=8)
ax.text(-0.95, 2e3, '$n = n_i^2/N_A = 10^4$', fontsize=8); ax.text(0.3, 2e3, '$p = n_i^2/N_D = 10^4$', fontsize=8)
ax.set_ylim(1e2, 1e18); ax.set_ylabel('濃度 (cm$^{-3}$)'); ax.set_xticks([]); ax.legend(fontsize=8, frameon=False, loc='center left', bbox_to_anchor=(0, 0.55)); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-01-concentration.svg')); plt.close(fig)

x = np.linspace(-1, 1, 400)
fig, ax = plt.subplots(figsize=(5.0, 2.6))
ax.plot(x, 0.7/(1+np.exp(-x/0.08)), color='#2a6fdb', lw=2, label='平衡：位能障 $V_0$')
ax.plot(x, 0.4/(1+np.exp(-x/0.08)), color='#d9480f', lw=2, ls='--', label='正向偏壓：$V_0 - V_A$')
ax.annotate('', (0.8, 0.7), (0.8, 0), arrowprops=dict(arrowstyle='<->')); ax.text(0.83, 0.33, '$V_0$≈0.7 V', fontsize=8)
ax.text(-0.95, 0.6, '（電洞看到的山：p 側低、n 側高）', fontsize=8)
ax.set_xticks([]); ax.set_ylabel('電洞的位能（V）'); ax.legend(fontsize=8, frameon=False, loc='center left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-01-barrier-bias.svg')); plt.close(fig)
