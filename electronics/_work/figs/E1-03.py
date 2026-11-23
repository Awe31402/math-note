# E1-03 figures: parallel-plate capacitor microphone, microphone model + amplifier input
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(4.6, 2.6))
ax.plot([0, 4], [2, 2], color='#d9480f', lw=4); ax.plot([0, 4], [0, 0], color='#2a6fdb', lw=4)
for x in [0.5, 1.5, 2.5, 3.5]:
    ax.annotate('', (x, 0.1), (x, 1.9), arrowprops=dict(arrowstyle='->', color='gray'))
ax.text(4.15, 2, '$+Q$（可動薄膜）', va='center'); ax.text(4.15, 0, '$-Q$（固定）', va='center')
ax.text(1.0, 1.0, '$E$', color='gray'); ax.annotate('', (-0.3, 0), (-0.3, 2), arrowprops=dict(arrowstyle='<->'))
ax.text(-0.6, 1, '$d$', va='center'); ax.text(1.4, 2.25, '面積 $A$')
ax.annotate('聲音 $f(t)$', (2, 2.05), (2.6, 2.8), arrowprops=dict(arrowstyle='->'))
ax.set_xlim(-0.8, 6.6); ax.set_ylim(-0.4, 3.1); ax.axis('off')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-03-plates.svg')); plt.close(fig)

with drawing() as d:
    c = elm.Capacitor().up().label('$C$', loc='top').label('$V_{DC}=Q/C$', loc='bottom')
    elm.Ground().at(c.start)
    s = elm.SourceSin().up().at(c.end).label('$v_s = Af(t)$', loc='top')
    elm.Line().right().at(s.end).length(3).label('$i_i$ →'); n = elm.Dot()
    elm.Resistor().down().length(6).label('$R_i$', loc='top')
    elm.Ground()
    save(d, 'E1-03-mic-model')
