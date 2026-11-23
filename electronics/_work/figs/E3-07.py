# E3-07 figure: large-signal transconductance ratio 2 I1(x)/(x I0(x)) vs x = V/V_T
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.special import iv
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(0.01, 10, 400)
fig, axs = plt.subplots(1, 2, figsize=(8.4, 2.8))
axs[0].plot(x, 2*iv(1, x)/iv(0, x), color='#2a6fdb', lw=2); axs[0].axhline(2, color='#888', ls=':', lw=1)
axs[0].set_xlabel('$x = V/V_T$'); axs[0].set_title('基頻電流振幅 / 直流 $= 2I_1(x)/I_0(x)$：飽和', fontsize=9)
axs[1].plot(x, 2*iv(1, x)/(x*iv(0, x)), color='#d9480f', lw=2); axs[1].axhline(1, color='#888', ls=':', lw=1)
axs[1].set_xlabel('$x = V/V_T$'); axs[1].set_title('等效 $G_m/g_m$：振幅越大越小，迴路增益降到 1', fontsize=9)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-07-large-signal-gm.svg')); plt.close(fig)
