# E3-18: BJT Wilson current mirror
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    q1 = elm.BjtNpn().right().reverse().anchor('emitter').at((0, 0))
    q2 = elm.BjtNpn().right().anchor('emitter').at((3.4, 0))
    for q in (q1, q2): elm.Line().down().at(q.emitter).length(0.3); elm.Ground()
    elm.Line().at(q1.base).to(q2.base)
    Y = elm.Line().up().at(q2.collector).length(0.8).end; elm.Dot().at(Y)
    k = (q2.base[0] - 0.5, q2.base[1]); elm.Dot().at(k)
    elm.Line().at(k).to((k[0], Y[1])); elm.Line().to(Y)
    q3 = elm.BjtNpn().right().anchor('emitter').at(Y)
    X = elm.Line().up().at(q1.collector).toy(q3.base[1]).end; elm.Dot().at(X)
    elm.Line().at(q3.base).to(X)
    elm.SourceI().up().at(X).label('$I_{REF}$', loc='bottom', ofst=(-0.3, 0)) if False else None
    elm.SourceI().up().at(X).reverse().label('$I_{REF}$'); elm.Vdd().label('$V_{CC}$')
    elm.Line().up().at(q3.collector).length(0.8); elm.Dot(open=True).label('$I_O$', loc='top')
    elm.Label().at((q1.base[0] - 1.3, q1.base[1])).label('$Q_1$')
    elm.Label().at((q2.base[0] + 1.4, q2.base[1])).label('$Q_2$')
    elm.Label().at((q3.base[0] + 1.4, q3.base[1])).label('$Q_3$')
    save(d, 'E3-18-wilson-mirror')
