# E1-06 figures: high-pass response, laser pointer with bypass capacitor, water-level picture
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

w = np.logspace(-1, 6, 400); w0 = 10
fig, ax = plt.subplots(figsize=(5.2, 2.7))
ax.semilogx(w, (w/w0)/np.sqrt(1+(w/w0)**2), color='#2a6fdb', lw=2)
ax.axvspan(1e2, 1e5, color='#2f9e44', alpha=0.15); ax.text(1.3e2, 0.5, '聲音 $10^2$–$10^5$ rad/s', fontsize=8)
for x, s in [(1, '$0.1\\omega_0$'), (10, '$\\omega_0=10$'), (100, '$10\\omega_0$')]:
    ax.axvline(x, color='gray', ls=':'); ax.text(x*1.1, 1.03, s, fontsize=8)
ax.set_xlabel('$\\omega$ (rad/s)'); ax.set_ylabel('$|v_O/v_s|$'); ax.set_ylim(0, 1.12); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-06-highpass-voice.svg')); plt.close(fig)

with drawing() as d:
    s = elm.SourceI().up().label('$I_{DC}+i_s$', loc='top')
    elm.Ground().at(s.start)
    elm.Line().right().at(s.end).length(3).label('→'); n = elm.Dot()
    elm.Capacitor().down().at(n.center).label('$C$', loc='top').label('$i_s$ ↓', loc='bottom'); elm.Ground()
    elm.Line().right().at(n.center).length(3)
    elm.LED().down().label('$R_L$', loc='top').label('$I_{DC}$ ↓', loc='bottom'); elm.Ground()
    save(d, 'E1-06-laser-bypass')

t = np.linspace(0, 6, 600)
fig, axs = plt.subplots(1, 2, figsize=(7.6, 2.5), sharey=True)
axs[0].plot(t, 2+0.3*np.sin(2*np.pi*3*t), color='#888', lw=1.2, label='輸入 $V_{DC}+v_s$')
axs[0].plot(t, 2*(1-np.exp(-t/0.4)), color='#2a6fdb', lw=2, label='電容 $v_C$')
axs[0].set_title('$\\omega \\gg \\omega_0$：電容只跟到直流', fontsize=10)
axs[1].plot(t, 2+0.3*np.sin(2*np.pi*0.3*t), color='#888', lw=1.2, label='輸入')
axs[1].plot(t, 2*(1-np.exp(-t/0.4))+0.3*np.sin(2*np.pi*0.3*t-0.2)*(1-np.exp(-t/0.4)), color='#2a6fdb', lw=2, label='電容 $v_C$')
axs[1].set_title('$\\omega \\ll \\omega_0$：電容直流交流都跟上', fontsize=10)
for a in axs: a.set_xticks([]); a.set_yticks([]); a.set_xlabel('$t$'); a.legend(fontsize=7.5, frameon=False, loc='lower right'); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-06-water-level.svg')); plt.close(fig)
