# E4-08: 741 op amp block diagram with the numbers from the lecture
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl, clean
import numpy as np; plt = mpl()
from matplotlib.patches import FancyBboxPatch
fig, ax = plt.subplots(figsize=(8.6, 2.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 2.4); ax.axis('off')
blocks = [(0.3, '輸入級（差動）\nNPN 隨耦 + 橫向 PNP\n10 μA', '$A_{d1}=150$\n' + r'$A_{cm1}\approx3\times10^{-6}$'),
          (2.75, '增益級（共射）\n0.5 mA', r'$A_2\approx2000$'),
          (5.2, 'AB 類輸出級\n達靈頓 + 短路保護', '增益 ≈ 1'),
          (7.65, '偏壓網路\n28.6 k → 1 mA\nWidlar → 10 μA', '')]
for x, t, g in blocks:
    ax.add_patch(FancyBboxPatch((x, 0.9), 2.0, 1.2, boxstyle='round,pad=0.05', fc='#eef3fb' if g else '#f3f3f3', ec='#2a6fdb' if g else '#888'))
    ax.text(x + 1.0, 1.5, t, ha='center', va='center', fontsize=8.5)
    if g: ax.text(x + 1.0, 0.5, g, ha='center', va='center', fontsize=8, color='#d9480f')
for x in (2.35, 4.8): ax.annotate('', xy=(x + 0.35, 1.5), xytext=(x, 1.5), arrowprops=dict(arrowstyle='->', lw=1.4))
ax.text(0.0, 2.3, r'$R_{id}\approx1$ MΩ', fontsize=8); ax.text(6.4, 2.3, r'總增益 $\approx3\times10^5$，$R_o$ 數十 Ω', fontsize=8.5)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E4-08-741-blocks.svg')); plt.close(fig)
