# E2-12 figures: NMOS cross-section (VDS=0 and VDS>0), source barrier lowering
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def mos(a, taper, title):
    a.add_patch(Rectangle((0, 0), 10, 4, fc='#fff4e6', ec='k'))            # p body
    a.add_patch(Rectangle((0.3, 2.9), 2.2, 1.1, fc='#d0ebff', ec='k'))     # n+ source
    a.add_patch(Rectangle((7.5, 2.9), 2.2, 1.1, fc='#d0ebff', ec='k'))     # n+ drain
    a.add_patch(Rectangle((2.5, 4.0), 5.0, 0.35, fc='#e9ecef', ec='k'))    # oxide
    a.add_patch(Rectangle((2.5, 4.35), 5.0, 0.35, fc='#868e96', ec='k'))   # gate metal
    a.add_patch(Polygon([(2.5, 4.0), (7.5, 4.0), (7.5, 2.6), (2.5, 2.6)], fc='#eee', ec='none', alpha=0.9))  # depletion
    t0, t1 = 0.45, (0.08 if taper else 0.45)
    a.add_patch(Polygon([(2.5, 4.0), (7.5, 4.0), (7.5, 4.0-t1), (2.5, 4.0-t0)], fc='#4dabf7', ec='none'))  # channel
    a.text(1.4, 3.35, 'n+', ha='center', fontsize=9); a.text(8.6, 3.35, 'n+', ha='center', fontsize=9)
    a.text(1.4, 4.25, 'S', ha='center', fontsize=10); a.text(8.6, 4.25, 'D', ha='center', fontsize=10); a.text(5, 4.85, 'G', ha='center', fontsize=10)
    a.text(5, 1.2, 'p 型基板（body）', ha='center', fontsize=9)
    a.text(5, 3.0, '空乏區（離子）', ha='center', fontsize=7.5, color='#555')
    a.text(5, 3.75 if not taper else 3.8, 'n 通道（電子）', ha='center', fontsize=7.5, color='#1864ab')
    a.text(2.4, 4.45, 'SiO₂', ha='right', fontsize=7)
    a.set_xlim(-0.2, 10.2); a.set_ylim(0, 5.2); a.axis('off'); a.set_title(title, fontsize=9)
fig, axs = plt.subplots(1, 2, figsize=(9.6, 2.9))
mos(axs[0], False, '$V_{GS} > V_t$、$V_{DS} = 0$：通道均勻')
mos(axs[1], True, '$V_{DS} > 0$：$V(x)$ 從 0 升到 $V_{DS}$，汲極端電子少')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-12-nmos-channel.svg')); plt.close(fig)

x = np.linspace(-2, 2, 400)
def barrier(h): return h/(1+np.exp(-x*4))
fig, ax = plt.subplots(figsize=(5.0, 2.5))
ax.plot(x, barrier(1.0), color='#888', lw=2, ls='--', label='$V_{GS}=0$：高山 $V_0$')
ax.plot(x, barrier(0.35), color='#2a6fdb', lw=2, label='$V_{GS} > V_t$：$V_0 - Q_{P2}/C_j$')
ax.plot([-1.6, -1.2, -0.8], [0.03, 0.03, 0.03], 'o', color='#1864ab'); ax.text(-1.9, 0.12, '源極的電子', fontsize=8, color='#1864ab')
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('源極 n+ → 閘極下方的 p 區'); ax.set_ylabel('電子看到的位能')
ax.legend(fontsize=7.5, frameon=False, loc='lower right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-12-barrier.svg')); plt.close(fig)
