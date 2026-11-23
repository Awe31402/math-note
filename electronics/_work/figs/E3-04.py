# E3-04 figure: CE stage driving a Darlington emitter follower into a speaker
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
with drawing() as d:
    elm.Dot(open=True).label('$v_s$', loc='left'); elm.Line().right().length(0.8)
    q1 = elm.BjtNpn(circle=True).anchor('base').label('CE', loc='right')
    elm.Resistor().down().at(q1.emitter).label('0.2 kΩ', loc='bottom'); elm.Ground()
    c1 = elm.Dot().at(q1.collector)
    elm.Resistor().up().at(c1.center).label('$R_C$ 5 kΩ', loc='bottom'); elm.Vdd().label('$V_{CC}$')
    elm.Line().right().at(c1.center).length(1.5)
    q2 = elm.BjtNpn(circle=True).anchor('base').label('$\\beta_1$', loc='right')
    elm.Line().up().at(q2.collector).length(0.6); elm.Vdd().label('$V_{CC}$')
    elm.Line().right().at(q2.emitter).length(0.8)
    q3 = elm.BjtNpn(circle=True).anchor('base').label('$\\beta_2$', loc='right')
    elm.Line().up().at(q3.collector).length(1.4); elm.Vdd().label('$V_{CC}$')
    e = elm.Dot().at(q3.emitter)
    elm.SourceI().down().at(e.center).label('$I$', loc='top'); elm.Vss().label('$-V$')
    elm.Line().right().at(e.center).length(1.8); o = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().label('$R_L$ 4 Ω', loc='bottom'); elm.Ground()
    save(d, 'E3-04-ce-darlington')
