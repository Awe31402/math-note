# E3-01 figures: 1/C^2 vs V_R, forward-biased minority profile, pnp BJT hole profile
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, axs = plt.subplots(1, 3, figsize=(10.5, 2.9))
V0 = 0.7; vr = np.linspace(-V0, 5, 100)
axs[0].plot(vr, (vr + V0), color='#2a6fdb', lw=2); axs[0].axhline(0, color='k', lw=0.5); axs[0].axvline(0, color='k', lw=0.5)
axs[0].plot(-V0, 0, 'o', color='#d9480f'); axs[0].text(-0.6, 0.4, '$-V_0$', color='#d9480f')
axs[0].set_xlabel('反向偏壓 $V_R$ (V)'); axs[0].set_ylabel('$1/C^2$'); axs[0].set_yticks([]); axs[0].set_title('C–V 量測：直線，斜率→濃度、截距→$V_0$', fontsize=8.5)
x = np.linspace(0, 4, 200)
axs[1].plot(x, np.exp(-x), color='#2a6fdb', lw=2); axs[1].axhline(0.0, color='k', lw=0.5)
axs[1].axvline(1, color='#888', ls=':', lw=1); axs[1].text(1.05, 0.5, '$L_p$', fontsize=9)
axs[1].text(0.1, 0.9, '$p_{n0}(e^{V/V_T} - 1)$', fontsize=8)
axs[1].set_xlabel('進入 N 區的距離 $x$'); axs[1].set_ylabel('多出來的電洞 $p - p_{n0}$'); axs[1].set_yticks([]); axs[1].set_xticks([])
axs[1].set_title('正向偏壓：少數載子注入後指數衰減', fontsize=8.5)
axs[2].axvspan(0, 1, color='#ffe3e3'); axs[2].axvspan(1, 1.4, color='#e7f5ff'); axs[2].axvspan(1.4, 2.6, color='#ffe3e3')
xb = np.linspace(1, 1.4, 50); axs[2].plot(xb, 1 - (xb-1)/0.4, color='#2a6fdb', lw=2.5)
axs[2].text(0.3, 1.1, 'P$^+$ 射極', fontsize=8); axs[2].text(1.02, 1.1, 'N 基極', fontsize=8); axs[2].text(1.7, 1.1, 'P 集極', fontsize=8)
axs[2].annotate('', (1.4, 0.55), (0.6, 0.55), arrowprops=dict(arrowstyle='->', color='#d9480f')); axs[2].text(0.45, 0.62, '100 電洞/s', fontsize=7.5, color='#d9480f')
axs[2].annotate('', (2.3, 0.35), (1.4, 0.35), arrowprops=dict(arrowstyle='->', color='#d9480f')); axs[2].text(1.6, 0.42, '99 → 集極', fontsize=7.5, color='#d9480f')
axs[2].annotate('', (1.2, -0.05), (1.2, 0.25), arrowprops=dict(arrowstyle='->', color='#2f9e44')); axs[2].text(1.25, 0.05, '1 個復合\n（基極補電子）', fontsize=7, color='#2f9e44')
axs[2].set_xlim(0, 2.6); axs[2].set_ylim(-0.1, 1.3); axs[2].set_xticks([]); axs[2].set_yticks([])
axs[2].set_title('PNP：基極窄（$W \\ll L_p$），電洞分布近直線', fontsize=8.5)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-01-pn-bjt.svg')); plt.close(fig)
