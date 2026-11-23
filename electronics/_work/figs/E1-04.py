# E1-04 figures: RC charging circuits and waveforms
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def src(d, lab):
    b = elm.BatteryCell().up().reverse().label(lab, loc='top'); elm.Ground().at(b.start); return b

with drawing() as d:            # (a) R then C, vo across C
    b = src(d, '$V$'); elm.Resistor().right().at(b.end).label('$R$').label('$i$ →', loc='bottom')
    n = elm.Dot().label('$v_O$', loc='right'); elm.Capacitor().down().at(n.center).label('$C$', loc='top'); elm.Ground()
    save(d, 'E1-04-rc')
with drawing() as d:            # (b) R1, then R2 || C, vo across C
    b = src(d, '$V$'); elm.Resistor().right().at(b.end).label('$R_1$'); n = elm.Dot()
    elm.Resistor().down().at(n.center).label('$R_2$', loc='top'); elm.Ground()
    elm.Line().right().at(n.center).length(2.5); m = elm.Dot().label('$v_O$', loc='right')
    elm.Capacitor().down().at(m.center).label('$C$', loc='top'); elm.Ground()
    save(d, 'E1-04-r1r2c')
with drawing() as d:            # (c) C then R, vo across R
    b = src(d, '$V$'); elm.Capacitor().right().at(b.end).label('$C$')
    n = elm.Dot().label('$v_O$', loc='right'); elm.Resistor().down().at(n.center).label('$R$', loc='top'); elm.Ground()
    save(d, 'E1-04-cr')
with drawing() as d:            # (d) R1, C, R2 in series, vo across R2
    b = src(d, '$V$'); elm.Resistor().right().at(b.end).label('$R_1$'); elm.Capacitor().right().label('$C$')
    n = elm.Dot().label('$v_O$', loc='right'); elm.Resistor().down().at(n.center).label('$R_2$', loc='top'); elm.Ground()
    save(d, 'E1-04-r1cr2')
with drawing() as d:            # (e) microphone -> blocking C -> amplifier
    c = elm.SourceV().up().label('$V_{DC}$', loc='top'); elm.Ground().at(c.start)
    s = elm.SourceSin().up().at(c.end).label('$v_s$', loc='top')
    elm.Capacitor().right().at(s.end).label('$C$'); n = elm.Dot()
    elm.Resistor().down().length(6).at(n.center).label('$R$', loc='top'); elm.Ground()
    elm.Line().right().at(n.center).length(2); elm.Dot(open=True).label('$v_i$', loc='right')
    save(d, 'E1-04-block-dc')

t = np.linspace(0, 5, 400)
fig, axs = plt.subplots(1, 2, figsize=(7.6, 2.6))
axs[0].plot(t, np.exp(-t), color='#d9480f', lw=2); axs[0].set_title('$i(t)$：從 $V/R$ 指數下降', fontsize=10)
axs[1].plot(t, 1-np.exp(-t), color='#2a6fdb', lw=2); axs[1].axhline(0.632, ls=':', color='gray'); axs[1].axvline(1, ls=':', color='gray')
axs[1].text(1.1, 0.5, '$t=\\tau$, 63%'); axs[1].axhline(1, ls='--', color='gray', lw=1); axs[1].text(3.3, 0.88, '$V$')
axs[1].set_title('$v_O(t)$：指數上升到 $V$', fontsize=10)
for a in axs: a.set_xlabel('$t/\\tau$'); a.set_yticks([]); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-04-charge-curves.svg')); plt.close(fig)

fig, ax = plt.subplots(figsize=(4.2, 2.4))
ax.plot(t, np.exp(-t), color='#2a6fdb', lw=2); ax.axhline(0, color='k', lw=0.8)
ax.text(0.15, 0.9, '$V$'); ax.text(1.1, 0.42, '$t=\\tau$, 剩 37%'); ax.axvline(1, ls=':', color='gray')
ax.set_xlabel('$t/\\tau$'); ax.set_ylabel('$v_O$'); ax.set_yticks([]); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-04-decay.svg')); plt.close(fig)

tt = np.linspace(0, 6, 600)
fig, ax = plt.subplots(figsize=(5.4, 2.5))
ax.plot(tt, np.sin(2*np.pi*tt/2), color='#888', lw=1.5, label='$v_s$')
ax.plot(tt, 0.1*np.sin(2*np.pi*tt/2 - np.pi/2), color='#2a6fdb', lw=2, label='$v_O$（約 1/10）')
ax.axhline(0, color='k', lw=0.6); ax.set_xlabel('$t$（單位 μs）'); ax.set_yticks([])
ax.annotate('', (0, -1.25), (1, -1.25), arrowprops=dict(arrowstyle='<->')); ax.text(0.25, -1.55, '$T/2=1$ μs')
ax.set_ylim(-1.7, 1.3); ax.legend(loc='upper right', fontsize=8, frameon=False); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-04-ac.svg')); plt.close(fig)
