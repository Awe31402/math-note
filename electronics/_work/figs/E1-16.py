# E1-16 figures: flyback transient, I-V amplifier model, LED band diagram with well
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

t = np.linspace(-0.5, 5, 500)
fig, axs = plt.subplots(1, 2, figsize=(7.6, 2.6))
i = np.where(t < 0, 20, 20*np.exp(-t)); v = np.where(t < 0, 0.05, -0.7*np.exp(-t))
axs[0].plot(t, i, color='#2a6fdb', lw=2); axs[0].set_title('線圈電流：20 mA 指數衰減', fontsize=9); axs[0].set_ylabel('mA')
axs[1].plot(t, v, color='#d9480f', lw=2, label='有飛輪二極體'); axs[1].axhline(-0.7, ls=':', color='gray'); axs[1].text(2.5, -0.62, '−0.7 V', fontsize=8)
axs[1].set_title('繼電器上端電壓：最低只到 −0.7 V', fontsize=9); axs[1].set_ylabel('V'); axs[1].text(0.1, -0.2, '（沒有二極體會是 −100 V）', fontsize=8)
for a in axs: a.set_xlabel('$t/\\tau$，$\\tau = L/r_d$ ≈ 1 ms'); a.spines[['top','right']].set_visible(False); a.axvline(0, color='k', lw=0.5)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-16-flyback-transient.svg')); plt.close(fig)

with drawing() as d:
    s = elm.SourceI().up().label('$i_s$', loc='top'); elm.Ground().at(s.start)
    elm.Line().right().at(s.end).length(2); a = elm.Dot()
    elm.Resistor().down().at(a.center).label('$R_s$', loc='bottom'); elm.Ground()
    elm.Line().right().at(a.center).length(2).label('$i_i$ →'); b = elm.Dot()
    elm.Resistor().down().at(b.center).label('$R_i$≈0', loc='bottom'); elm.Ground()
    src = elm.SourceControlledV().up().at((b.center[0]+3, b.center[1]-3)).label('$A i_i$', loc='top')
    elm.Ground().at(src.start)
    elm.Resistor().right().at(src.end).label('$R_o$=0'); o = elm.Dot().label('$v_o$', loc='top')
    elm.Resistor().down().at(o.center).label('$R_L$', loc='bottom'); elm.Ground()
    save(d, 'E1-16-iv-model')

x = np.linspace(0, 10, 500)
well = (x > 4.3) & (x < 5.7)
Ec = np.where(well, 1.7, 2.2)
Ev = np.where(well, 0.6, 0.2)
fig, ax = plt.subplots(figsize=(5.2, 2.6))
ax.plot(x, Ec, color='#2a6fdb', lw=2, label='導帶'); ax.plot(x, Ev, color='#d9480f', lw=2, label='價帶')
ax.annotate('電子 →', (4.6, 1.75), (1.0, 2.35), arrowprops=dict(arrowstyle='->'), fontsize=8)
ax.annotate('← 電洞', (5.4, 0.55), (7.4, 0.0), arrowprops=dict(arrowstyle='->'), fontsize=8)
ax.annotate('', (5, 0.65), (5, 1.65), arrowprops=dict(arrowstyle='->', color='#2f9e44')); ax.text(5.15, 1.1, '結合發光', color='#2f9e44', fontsize=8)
ax.set_xticks([]); ax.set_yticks([]); ax.legend(fontsize=8, frameon=False, loc='lower left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-16-led-well.svg')); plt.close(fig)
