# E2-15 figures: small-signal on transfer curve, biased CS amp with coupling cap, AC equivalent
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
k, Vt, VGS = 2, 1, 2
fig, ax = plt.subplots(figsize=(5.4, 3.2))
v = np.linspace(1, 3, 200); ax.plot(v, k/2*(v-Vt)**2, color='#2a6fdb', lw=2)
ID = k/2*(VGS-Vt)**2; gm = k*(VGS-Vt)
xx = np.array([1.5, 2.5]); ax.plot(xx, ID + gm*(xx-VGS), color='#d9480f', lw=1.2, ls='--'); ax.text(2.45, 2.3, '斜率 $g_m$', color='#d9480f', fontsize=8)
t = np.linspace(0, 1, 200); a = 0.15
ax.plot(VGS + a*np.sin(2*np.pi*2*t), -0.6*t - 0.1, color='#2f9e44', lw=1.2)   # input below axis
ax.plot(3.05 + 0.5*t, ID + gm*a*np.sin(2*np.pi*2*t), color='#2f9e44', lw=1.2)  # output to right
ax.plot(VGS, ID, 'o', color='k'); ax.text(VGS-0.35, ID+0.25, 'Q (2 V, 1 mA)', fontsize=8)
ax.axhline(ID, color='#aaa', lw=0.6, ls=':'); ax.axvline(VGS, color='#aaa', lw=0.6, ls=':')
ax.text(2.2, -0.55, '$v_{gs}$', color='#2f9e44', fontsize=9); ax.text(3.3, 1.45, '$i_d = g_mv_{gs}$', color='#2f9e44', fontsize=9)
ax.set_xlim(0.9, 3.7); ax.set_ylim(-0.8, 4.2); ax.set_xlabel('$v_{GS}$ (V)'); ax.set_ylabel('$i_D$ (mA)')
ax.set_title('小信號：在 Q 點附近把拋物線當直線', fontsize=9); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-15-small-signal.svg')); plt.close(fig)

with drawing() as d:
    g0 = elm.Ground()
    s = elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Resistor().right().label('$R_s$')
    elm.Capacitor().right().label('$C$')
    n = elm.Dot()
    elm.Line().right().length(1.0)
    q = elm.NFet().anchor('gate').reverse()
    elm.Line().down().at(q.source).length(0.3); elm.Ground()
    elm.Resistor().up().at(q.drain).label('$R_D$ 5 kΩ', loc='bottom'); t = elm.Vdd().label('10 V')
    elm.Line().right().at(q.drain).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    elm.Resistor().up().at(n.center).label('$R_1$ 8 MΩ', loc='top'); elm.Vdd().label('10 V')
    elm.Resistor().down().at(n.center).label('$R_2$ 2 MΩ', loc='top'); elm.Ground()
    save(d, 'E2-15-biased-amp')

with drawing() as d:
    g = elm.Dot(open=True).label('G: $v_{gs}$', loc='left')
    elm.Line().right().length(1.0).linestyle(':')
    D = (g.center[0]+3.0, g.center[1]+1.5)
    elm.Dot().at(D).label('D: $v_o$', loc='top')
    src = elm.SourceI().down().at(D).length(3).label('$g_mv_{gs}$', loc='top')
    elm.Ground().at(src.end); 
    elm.Line().right().at(D).length(2.2); elm.Resistor().down().length(3).label('$R_D$', loc='bottom'); elm.Ground()
    save(d, 'E2-15-ac-model')
