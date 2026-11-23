# E2-17 figures: drain-feedback bias with RG, current mirror, CS amp biased by current source
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:   # drain feedback bias
    g0 = elm.Ground()
    elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Resistor().right().label('$R_s$'); elm.Capacitor().right().label('$C$')
    n = elm.Dot()
    elm.Line().right().length(0.8)
    q = elm.NFet().anchor('gate').reverse()
    elm.Line().down().at(q.source).length(0.3); elm.Ground()
    dd = elm.Dot().at(q.drain)
    elm.Resistor().up().at(dd.center).label('$R_D$ 8 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(dd.center).length(1.5); o = elm.Dot().label('$v_O$', loc='right')
    elm.Line().down().at(n.center).length(2.8)
    elm.Resistor().right().tox(o.center[0]+0.0).label('$R_G$ 10 MΩ', loc='bottom'); elm.Line().up().toy(o.center[1])
    save(d, 'E2-17-drain-feedback')

with drawing() as d:   # current mirror
    m = elm.Dot()
    elm.Line().left().length(1.0)
    q1 = elm.NFet().anchor('gate').reverse().flip().label('$Q_{ref}$', loc='bottom')
    elm.Line().down().at(q1.source).length(0.3); elm.Ground()
    a = elm.Dot().at(q1.drain)
    elm.Resistor().up().at(a.center).label('$R$ 8 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(a.center).tox(m.center[0]); elm.Line().down().toy(m.center[1])
    elm.Line().right().at(m.center).length(1.0)
    q2 = elm.NFet().anchor('gate').reverse().label('$Q_2$', loc='bottom')
    elm.Line().down().at(q2.source).length(0.3); elm.Ground()
    elm.Line().up().at(q2.drain).length(1.2); elm.Dot(open=True).label('$I_O$ = 1 mA', loc='top')
    save(d, 'E2-17-current-mirror')

with drawing() as d:   # CS amp with current-source bias and bypass capacitor
    elm.Dot(open=True).label('$V_{DC} + v_s$', loc='left')
    elm.Line().right().length(1.0)
    q = elm.NFet().anchor('gate').reverse().label('$Q_1$', loc='right', ofst=(0.5, 0.2))
    elm.Resistor().up().at(q.drain).label('$R_D$ 5 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(q.drain).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    s = elm.Dot().at(q.source)
    elm.SourceI().down().at(s.center).label('1 mA', loc='top').label('$Q_2$', loc='bottom'); elm.Vss().label('−10 V')
    elm.Line().right().at(s.center).length(2.0); elm.Capacitor().down().label('$C$', loc='bottom'); elm.Ground()
    save(d, 'E2-17-cs-current-bias')
