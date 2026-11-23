# E3-09 figures: PLL block diagram; multiplier phase-detector characteristic
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, axs = plt.subplots(1, 2, figsize=(10.0, 2.9), gridspec_kw={'width_ratios': [1.3, 1]})
a = axs[0]; a.axis('off'); a.set_xlim(0, 10); a.set_ylim(0, 4)
for txt, x, y in [('相位偵測器\n$K_1(\\theta_1-\\theta_2)$', 1.5, 2.3), ('積分（RC）\n／放大 A', 4.5, 2.3), ('VCO\n$\\omega_2 = \\omega_0 + K_2v$', 7.5, 2.3)]:
    a.add_patch(FancyBboxPatch((x-1.0, y-0.55), 2.0, 1.1, boxstyle='round,pad=0.05', fc='#e7f0ff', ec='#2a6fdb'))
    a.text(x, y, txt, ha='center', va='center', fontsize=8)
a.annotate('', (0.5, 2.3), (-0.2, 2.3), arrowprops=dict(arrowstyle='->')); a.text(-0.2, 2.6, '輸入 $\\omega_1$', fontsize=8)
a.annotate('', (3.5, 2.3), (2.5, 2.3), arrowprops=dict(arrowstyle='->'))
a.annotate('', (6.5, 2.3), (5.5, 2.3), arrowprops=dict(arrowstyle='->')); a.text(5.6, 2.55, '$v$', fontsize=9)
a.plot([8.5, 9.5, 9.5, 1.5, 1.5], [2.3, 2.3, 0.6, 0.6, 1.75], color='k', lw=1); a.annotate('', (1.5, 1.75), (1.5, 1.2), arrowprops=dict(arrowstyle='->'))
a.text(5.0, 0.25, '回授 $\\omega_2$；穩態 $\\omega_2 = \\omega_1$，$v$ 就是 FM 解調輸出', ha='center', fontsize=8)
a.text(4.5, 3.4, '$\\dfrac{d\\omega_2}{dt} = K_1K_2(\\omega_1 - \\omega_2)$', ha='center', fontsize=9, color='#d9480f')
d = np.linspace(-2*np.pi, 2*np.pi, 500)
axs[1].plot(d, np.cos(d), color='#2a6fdb', lw=2); axs[1].axhline(0, color='k', lw=0.5)
for x0, c, t in [(-np.pi/2, '#2f9e44', '鎖得住'), (np.pi/2, '#d9480f', '離開'), (3*np.pi/2, '#2f9e44', '鎖得住')]:
    axs[1].plot(x0, 0, 'o', color=c); axs[1].text(x0-0.6, 0.15 if c != '#d9480f' else -0.3, t, fontsize=8, color=c)
axs[1].set_xlabel('$\\theta_1 - \\theta_2$'); axs[1].set_yticks([]); axs[1].set_xticks([])
axs[1].set_title('乘法器 + 低通：$\\frac{1}{2}v_1v_2\\cos(\\theta_1-\\theta_2)$，週期性', fontsize=9)
axs[1].spines[['top','right','left']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-09-pll.svg')); plt.close(fig)
