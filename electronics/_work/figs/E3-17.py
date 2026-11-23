# E3-17: BJT diff pair with PNP mirror load and base-current compensation (Q5)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    q3 = elm.BjtPnp().right().reverse().anchor('emitter').at((0, 0))
    q4 = elm.BjtPnp().right().anchor('emitter').at((5, 0))
    for q in (q3, q4):
        elm.Line().up().at(q.emitter).length(0.4); elm.Vdd().label('$V_{CC}$')
    elm.Line().at(q3.base).to(q4.base)
    B = ((q3.base[0] + q4.base[0]) / 2, q3.base[1]); elm.Dot().at(B)
    elm.Resistor().up().at(B).toy(q3.emitter[1] + 0.4).label('$R$', loc='bottom'); elm.Vdd()
    e5 = elm.Line().down().at(B).length(0.8).end
    q5 = elm.BjtPnp().right().anchor('emitter').at(e5)
    elm.Line().down().at(q5.collector).length(0.4); elm.Ground()
    A = elm.Line().down().at(q3.collector).length(2.6).end
    elm.Line().at(q5.base).to((q3.collector[0], q5.base[1])); elm.Dot().at((q3.collector[0], q5.base[1]))
    C = elm.Line().down().at(q4.collector).length(2.6).end
    q1 = elm.BjtNpn().right().anchor('collector').at(A)
    q2 = elm.BjtNpn().right().reverse().anchor('collector').at(C)
    elm.Line().left().at(q1.base).length(0.6); elm.Dot(open=True).label('$v_{i1}$', loc='left')
    elm.Line().right().at(q2.base).length(0.6); elm.Dot(open=True).label('$v_{i2}$', loc='right')
    elm.Dot().at((C[0], C[1] + 0.8)); elm.Line().right().at((C[0], C[1] + 0.8)).length(1.6); elm.Dot(open=True).label('$v_o$', loc='right')
    a = elm.Line().down().at(q1.emitter).length(0.4).end; b = elm.Line().down().at(q2.emitter).length(0.4).end
    elm.Line().at(a).to(b); t = ((a[0] + b[0]) / 2, a[1]); elm.Dot().at(t)
    elm.SourceI().down().at(t).label('$I$', loc='bottom'); elm.Vss()
    for q, lab, dx in ((q1, '$Q_1$', 0.6), (q2, '$Q_2$', -0.6), (q3, '$Q_3$', -0.7), (q4, '$Q_4$', 0.7), (q5, '$Q_5$', 0.7)):
        elm.Label().at((q.base[0] + (1.3 if dx > 0 else -1.3) * (1 if q not in (q1, q4, q5) else 1), q.base[1])).label(lab) if False else None
    elm.Label().at((q1.base[0] + 1.3, q1.base[1] + 0.2)).label('$Q_1$')
    elm.Label().at((q2.base[0] - 1.3, q2.base[1] + 0.2)).label('$Q_2$')
    elm.Label().at((q3.base[0] - 1.4, q3.base[1])).label('$Q_3$')
    elm.Label().at((q4.base[0] + 1.4, q4.base[1])).label('$Q_4$')
    elm.Label().at((q5.base[0] + 1.4, q5.base[1])).label('$Q_5$')
    save(d, 'E3-17-base-comp-mirror')
