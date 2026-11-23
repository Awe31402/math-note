# E2-22 figure: CMOS amplifier (PMOS on top, NMOS bottom, gates & drains tied)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:
    elm.Dot(open=True).label('$v_s$', loc='left')
    elm.Line().right().length(1.0); g = elm.Dot()
    elm.Line().up().length(0.75); elm.Line().right().length(0.6)
    qp = elm.PFet().anchor('gate').reverse().label('PMOS', loc='right', ofst=(0.6, 0))
    elm.Line().up().at(qp.source).length(0.4); elm.Vdd().label('+5 V')
    elm.Line().down().at(g.center).length(0.75); elm.Line().right().length(0.6)
    qn = elm.NFet().anchor('gate').reverse().label('NMOS', loc='right', ofst=(0.6, 0))
    elm.Line().down().at(qn.source).length(0.4); elm.Vss().label('−5 V')
    elm.Line().at(qp.drain).to(qn.drain)
    o = elm.Dot().at(((qp.drain[0]+qn.drain[0])/2, (qp.drain[1]+qn.drain[1])/2))
    elm.Line().right().at(o.center).length(2.0); oo = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().label('$R_L$', loc='bottom'); elm.Ground()
    save(d, 'E2-22-cmos-amp')
