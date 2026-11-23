# E2-08 figures: carrier extraction waveforms, spectra of synchronous detection, integrator follower
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

t = np.linspace(0, 1, 6000); fc = 12; m = 0.5
env = 1 + m*np.sin(2*np.pi*t); am = env*np.sin(2*np.pi*fc*t)
sq = 5.7*np.sign(am)
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.4))
axs[0].plot(t, am, color='#2a6fdb', lw=0.8); axs[0].set_title('AM 信號（振幅在變）', fontsize=9)
axs[1].plot(t, sq, color='#d9480f', lw=0.8); axs[1].set_title('比較器（和 0 比）：±($V_{Z0}$+0.7) 方波', fontsize=9)
axs[1].set_yticks([-5.7, 0, 5.7])
axs[2].plot(t, 4/np.pi*5.7*np.sin(2*np.pi*fc*t), color='#2f9e44', lw=0.8); axs[2].set_title('低通取第一根：$\\frac{4}{\\pi}(V_{Z0}+0.7)\\sin\\omega_ct$', fontsize=9)
for a in axs: a.set_xticks([]); a.axhline(0, color='k', lw=0.4); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-08-carrier-extract.svg')); plt.close(fig)

fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.3))
def lines(a, xs, hs, c):
    for x, h in zip(xs, hs): a.vlines(x, 0, h, color=c, lw=2.5)
def sb(a, x, h, c):
    a.fill_between([x-0.18, x-0.03], 0, h, color=c, alpha=0.6); a.fill_between([x+0.03, x+0.18], 0, h, color=c, alpha=0.6)
lines(axs[0], [1], [1], '#2a6fdb'); sb(axs[0], 1, 0.35, '#d9480f'); axs[0].set_title('AM：載波 + 兩邊聲音', fontsize=9)
axs[0].set_xticks([0, 1]); axs[0].set_xticklabels(['0', '$f_c$'])
lines(axs[1], [1, 3, 5, 7], [1, 1/3, 1/5, 1/7], '#d9480f'); axs[1].set_title('比較器輸出：只有 $f_c$ 的奇數倍', fontsize=9)
axs[1].set_xticks([1, 3, 5, 7]); axs[1].set_xticklabels(['$f_c$', '$3f_c$', '$5f_c$', '$7f_c$'])
lines(axs[2], [0, 2], [1, 0.5], '#2a6fdb'); sb(axs[2], 2, 0.18, '#d9480f')
axs[2].fill_between([0.03, 0.18], 0, 0.35, color='#d9480f', alpha=0.6); axs[2].text(0.22, 0.38, '聲音', color='#d9480f', fontsize=8)
axs[2].plot([0, 0.6, 0.9], [0.9, 0.9, 0], color='#2f9e44', lw=1.2); axs[2].text(0.62, 0.92, '低通', color='#2f9e44', fontsize=8)
axs[2].set_title('AM × 載波：聲音回到低頻、另一份在 $2f_c$', fontsize=9)
axs[2].set_xticks([0, 2]); axs[2].set_xticklabels(['0', '$2f_c$'])
for a in axs: a.set_yticks([]); a.set_ylim(0, 1.15); a.set_xlim(-0.3, a.get_xlim()[1]+0.3); a.spines[['top','right','left']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-08-sync-spectra.svg')); plt.close(fig)

tt = np.linspace(0, 5, 500); VR = 2
fig, ax = plt.subplots(figsize=(5.2, 2.5))
ax.plot(tt, VR + (4-VR)*np.exp(-tt), color='#2a6fdb', lw=2, label='$v_O(0) > V_R$：往下掉')
ax.plot(tt, VR + (0-VR)*np.exp(-tt), color='#d9480f', lw=2, label='$v_O(0) < V_R$：往上升')
ax.axhline(VR, color='k', lw=0.8, ls=':'); ax.text(4.2, 2.1, '$V_R$', fontsize=9)
ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_xticklabels(['0', '$\\tau$', '$2\\tau$', '$3\\tau$', '$4\\tau$', '$5\\tau$'])
ax.set_ylabel('$v_O$'); ax.legend(fontsize=7.5, frameon=False, loc='upper right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-08-integrator-follow.svg')); plt.close(fig)
