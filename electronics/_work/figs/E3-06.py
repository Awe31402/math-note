# E3-06 figures: RC-loop phases & magnitude; square wave -> sine via narrow band-pass
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, axs = plt.subplots(1, 3, figsize=(10.5, 2.9))
w = np.logspace(-2, 2, 400); x = w
lp = 1/(1+1j*x); hp = 1j*x/(1+1j*x); L = lp*hp
axs[0].semilogx(w, np.degrees(np.angle(lp)), color='#2a6fdb', label='低通 $-\\tan^{-1}(\\omega/\\omega_0)$')
axs[0].semilogx(w, np.degrees(np.angle(hp)), color='#d9480f', label='高通 $90° - \\tan^{-1}(\\omega/\\omega_0)$')
axs[0].semilogx(w, np.degrees(np.angle(L)), color='k', lw=2, label='相加')
axs[0].axhline(0, color='#888', lw=0.6); axs[0].axvline(1, color='#888', lw=0.6, ls=':')
axs[0].set_xlabel('$\\omega/\\omega_0$'); axs[0].set_ylabel('相位 (°)'); axs[0].legend(fontsize=6.5, frameon=False, loc='lower left'); axs[0].set_title('只有 $\\omega_0$ 相位相加為 0', fontsize=9)
axs[1].semilogx(w, np.abs(L), color='k', lw=2); axs[1].axhline(0.5, color='#d9480f', ls=':', lw=1)
axs[1].text(0.012, 0.52, '在 $\\omega_0$ 是 1/2 → 放大器要 ≥ 2', fontsize=8, color='#d9480f')
axs[1].set_xlabel('$\\omega/\\omega_0$'); axs[1].set_title('低通 × 高通的大小', fontsize=9)
for k, h in [(1, 1), (3, 1/3), (5, 1/5), (7, 1/7)]: axs[2].vlines(k, 0, h, color='#2a6fdb', lw=3)
xx = np.linspace(0.3, 8, 800); Q = 20; H = 1/np.sqrt(1 + (Q*(xx - 1/xx))**2)
axs[2].plot(xx, H, color='#2f9e44', lw=1.5); axs[2].text(1.3, 0.9, '窄帶通（$RC$ 大）只留 $\\omega$', fontsize=8, color='#2f9e44')
axs[2].set_xticks([1, 3, 5, 7]); axs[2].set_xticklabels(['$\\omega$', '$3\\omega$', '$5\\omega$', '$7\\omega$']); axs[2].set_yticks([])
axs[2].set_title('方波頻譜 → 只剩正弦', fontsize=9)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-06-osc-bpf.svg')); plt.close(fig)
