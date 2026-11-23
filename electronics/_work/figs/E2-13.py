# E2-13 figures: NMOS output characteristics, example circuit
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
k, Vt = 2, 1
v = np.linspace(0, 4, 400)
fig, ax = plt.subplots(figsize=(5.6, 3.0))
for vgs, c in [(3, '#2a6fdb'), (2.5, '#4dabf7'), (2, '#f08c00'), (1.5, '#d9480f'), (1, '#888')]:
    vov = vgs - Vt
    i = np.where(v < vov, k*(vov*v - v**2/2), k*vov**2/2)
    ax.plot(v, i, color=c, lw=2, label=f'$V_{{GS}}$ = {vgs} V' + ('（= $V_t$）' if vgs == 1 else ''))
vb = np.linspace(0, 2, 50); ax.plot(vb, k*vb**2/2, color='#555', ls='--', lw=1)
ax.text(0.15, 3.6, '三極管區\n$V_{DS} \\leq V_{GS}-V_t$', fontsize=8); ax.text(2.4, 4.3, '飽和區  $I_D = \\frac{1}{2}k(V_{GS}-V_t)^2$', fontsize=8)
ax.annotate('夾止點', (2, 4), (1.2, 4.6), fontsize=8, arrowprops=dict(arrowstyle='->', color='#555'))
ax.set_xlabel('$V_{DS}$ (V)'); ax.set_ylabel('$I_D$ (mA)'); ax.set_ylim(0, 5.2)
ax.legend(fontsize=7, frameon=False, loc='center right'); ax.spines[['top','right']].set_visible(False)
ax.set_title('$k$ = 2 mA/V²，$V_t$ = 1 V', fontsize=9)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-13-output-char.svg')); plt.close(fig)

with drawing() as d:
    elm.Dot(open=True).label('$V_{GS}$ = 5 V', loc='left')
    elm.Line().right().length(1.2)
    q = elm.NFet().anchor('gate').reverse()
    elm.Line().down().at(q.source).length(0.3); elm.Ground()
    elm.Resistor().up().at(q.drain).label('$R_D$ = 5 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(q.drain).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    save(d, 'E2-13-example')
