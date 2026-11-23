# E3-19: series-shunt feedback: A-circuit with beta network loading (beta = 0)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    op = elm.Opamp(leads=True).flip().right()
    elm.Line().left().at(op.in2).length(1.4); elm.Dot(open=True).label('$v_i$', loc='left')
    n = elm.Line().left().at(op.in1).length(0.8).end; elm.Dot().at(n)
    elm.Resistor().down().at(n).label('$R_{11}$ = $R_1$∥$R_2$', loc='bottom'); elm.Ground()
    o = elm.Line().right().at(op.out).length(0.8).end; elm.Dot().at(o)
    elm.Resistor().down().at(o).label('$R_{22}$ = $R_1$+$R_2$', loc='bottom'); elm.Ground()
    elm.Line().right().at(o).length(3.8); p = elm.Dot()
    elm.Resistor().down().at(p.center).label('$R_L$', loc='bottom'); elm.Ground()
    elm.Line().right().at(p.center).length(0.8); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.Label().at((op.out[0] - 1.3, op.out[1] + 1.5)).label('basic amplifier with loading ($\\beta=0$)')
    save(d, 'E3-19-a-circuit')
