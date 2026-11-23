# E1-08 figures: simple MOS amplifier model, square-law transfer with Q point, bias divider + coupling capacitor
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:   # MOS model: open input, dependent current source, RL to 10 V
    i = elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().down().length(3).linestyle(':')
    elm.Ground()
    src = elm.SourceControlledI().up().at((4, -3)).reverse().label('$i_o$', loc='bottom')
    elm.Ground().at(src.start)
    n = elm.Dot().at(src.end).label('$v_o$', loc='right')
    elm.Resistor().up().at(n.center).label('$R_L$ = 5 kΩ', loc='bottom')
    elm.Vdd().label('10 V')
    save(d, 'E1-08-mos-model')

v = np.linspace(0, 3.2, 400); io = np.where(v > 1, (v-1)**2, 0)
fig, ax = plt.subplots(figsize=(4.8, 3.2))
ax.plot(v, io, color='#2a6fdb', lw=2)
ax.plot([2], [1], 'o', color='#d9480f'); ax.text(2.05, 0.75, '$Q$ (2 V, 1 mA)')
ax.plot(v, 1+2*(v-2), color='#d9480f', ls='--', lw=1); ax.text(2.45, 2.15, '斜率 = 2 mA/V', color='#d9480f', fontsize=9)
ax.plot([0], [0], 'o', color='gray'); ax.text(0.05, 0.25, '沒有直流：\n工作點在 0，斜率 0', fontsize=8, color='gray')
ax.set_xlabel('$v_i$ (V)'); ax.set_ylabel('$i_o$ (mA)'); ax.set_xlim(0, 3.2); ax.set_ylim(-0.2, 4.5); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-08-square-law.svg')); plt.close(fig)

t = np.linspace(0, 2, 400); vs = 0.05*np.sin(2*np.pi*t)
fig, axs = plt.subplots(1, 2, figsize=(7.4, 2.4))
axs[0].plot(t, 2+vs, color='#2a6fdb', lw=2); axs[0].axhline(2, color='gray', ls=':'); axs[0].set_title('輸入 $v_i = 2 + v_s$（V）', fontsize=10); axs[0].set_ylim(1.8, 2.2)
axs[1].plot(t, 5-10*vs, color='#d9480f', lw=2); axs[1].axhline(5, color='gray', ls=':'); axs[1].set_title('輸出 $v_o = 5 - 10\\,v_s$（V）', fontsize=10); axs[1].set_ylim(4, 6)
for a in axs: a.set_xticks([]); a.set_xlabel('$t$'); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-08-waveforms.svg')); plt.close(fig)

with drawing() as d:   # bias divider + coupling capacitor from microphone
    top = elm.Vdd().label('10 V')
    r1 = elm.Resistor().down().label('80 kΩ', loc='bottom')
    g = elm.Dot().label('$v_i$', loc='right')
    elm.Resistor().down().label('20 kΩ', loc='bottom'); elm.Ground()
    c = elm.Capacitor().left().at(g.center).length(3).label('$C$')
    s = elm.SourceSin().down().label('$v_s$', loc='top')
    elm.SourceV().down().reverse().label('$V_{mic}$', loc='top'); elm.Ground()
    save(d, 'E1-08-bias-coupling')
