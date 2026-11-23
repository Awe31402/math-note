# E2-18 figures: common-gate and common-drain amplifiers with current-source bias
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:   # common gate
    g = elm.Ground()
    elm.Line().up().length(0.8); elm.Line().right().length(1.0)
    q = elm.NFet().anchor('gate').reverse()
    elm.Resistor().up().at(q.drain).label('$R_D$ 5 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(q.drain).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    s = elm.Dot().at(q.source)
    elm.SourceI().down().at(s.center).label('1 mA', loc='top'); elm.Vss().label('−10 V')
    elm.Capacitor().right().at(s.center).length(2.0).label('$C$', loc='bottom')
    elm.Resistor().right().label('$R_S$', loc='bottom')
    elm.SourceSin().down().label('$v_s$', loc='bottom'); elm.Ground()
    save(d, 'E2-18-common-gate')

with drawing() as d:   # common drain (source follower)
    g0 = elm.Ground()
    elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Resistor().right().label('$R_S$')
    elm.Line().right().length(0.6)
    q = elm.NFet().anchor('gate').reverse()
    elm.Line().up().at(q.drain).length(0.8); elm.Vdd().label('10 V')
    s = elm.Dot().at(q.source)
    elm.SourceI().down().at(s.center).label('1 mA', loc='bottom'); elm.Vss().label('−10 V')
    elm.Capacitor().right().at(s.center).length(2.5).label('$C$')
    o = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().label('$R_L$', loc='bottom'); elm.Ground()
    save(d, 'E2-18-common-drain')
