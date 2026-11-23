# E4-03: MOS cascode amplifier (CS Q1 + CG Q2) with current-source load
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    elm.Ground().at((0, -1.2)); elm.SourceSin().up().at((0, -1.2)).label('$v_s$', loc='top'); elm.Resistor().right().label('$R_s$')
    elm.Line().right().length(0.6)
    q1 = elm.NFet().anchor('gate').reverse()
    elm.Line().down().at(q1.source).length(0.3); elm.Ground()
    m = elm.Line().up().at(q1.drain).length(0.6).end; elm.Dot().at(m)
    q2 = elm.NFet().right().reverse().anchor('source').at(m)
    elm.Line().left().at(q2.gate).length(0.8); elm.Dot(open=True).label('$V_{G2}$', loc='left')
    o = elm.Dot().at(q2.drain)
    elm.SourceI().up().at(q2.drain).reverse().label('$I$', loc='bottom'); elm.Vdd().label('$V_{DD}$')
    elm.Line().right().at(q2.drain).length(1.2); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.Label().at((q1.gate[0] - 0.7, q1.gate[1] - 0.6)).label('$Q_1$ CS')
    elm.Label().at((q2.gate[0] + 0.1, q2.gate[1] + 0.55)).label('$Q_2$ CG')
    elm.Label().at((m[0] + 1.3, m[1])).label('1/$g_{m2}$')
    save(d, 'E4-03-cascode')
