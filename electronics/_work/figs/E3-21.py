# E3-21: transimpedance amplifier (photodetector current -> voltage)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    op = elm.Opamp(leads=True).right()
    elm.Line().left().at(op.in2).length(0.3); elm.Ground()
    n = elm.Line().left().at(op.in1).length(1.4).end; elm.Dot().at(n)
    elm.Resistor().down().at(n).length(2.4).label('$R_s$', loc='bottom'); elm.Ground()
    n2 = elm.Line().left().at(n).length(1.8).end
    elm.SourceI().down().at(n2).length(2.4).reverse().label('$i_s$', loc='top'); elm.Ground()
    elm.Line().up().at(n).length(1.6)
    elm.Resistor().right().tox(op.out[0] + 0.6).label('$R$')
    elm.Line().down().toy(op.out[1]); elm.Line().left().tox(op.out[0])
    elm.Dot().at((op.out[0] + 0.6, op.out[1]))
    elm.Line().right().at((op.out[0] + 0.6, op.out[1])).length(0.8); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.Label().at((op.out[0] + 1.6, op.out[1] - 0.7)).label('≈ −R $i_s$')
    elm.Label().at((n2[0] - 0.2, n2[1] + 0.6)).label('photodetector')
    save(d, 'E3-21-tia')
