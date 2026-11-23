# E4-07: Widlar current source
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    q1 = elm.BjtNpn().right().reverse().anchor('emitter').at((0, 0))
    q2 = elm.BjtNpn().right().anchor('emitter').at((3.4, 0.0))
    elm.Line().down().at(q1.emitter).length(1.6); elm.Ground()
    elm.Resistor().down().at(q2.emitter).length(1.6).label('$R_E$', loc='bottom'); elm.Ground()
    elm.Line().at(q1.base).to(q2.base)
    X = elm.Line().up().at(q1.collector).length(0.8).end; elm.Dot().at(X)
    k = (q1.base[0] + 0.5, q1.base[1]); elm.Dot().at(k)
    elm.Line().at(k).to((k[0], X[1])); elm.Line().to(X)
    elm.SourceI().up().at(X).reverse().label('$I_{REF}$'); elm.Vdd().label('$V_{CC}$')
    elm.Line().up().at(q2.collector).length(1.0); elm.Dot(open=True).label('$I_O$', loc='top')
    elm.Label().at((q1.base[0] - 1.3, q1.base[1])).label('$Q_1$')
    elm.Label().at((q2.base[0] + 1.4, q2.base[1])).label('$Q_2$')
    elm.Label().at((1.7, -2.6)).label('$V_T$ ln($I_{REF}$/$I_O$) = $I_O R_E$')
    save(d, 'E4-07-widlar')
