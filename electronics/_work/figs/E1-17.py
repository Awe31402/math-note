# E1-17 figures: V->I converter (laser driver), I->I amplifier
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:   # V->I: vi at +, R from - to ground, laser between output and -
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(2.5); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().left().at(op.in1).length(1.0); n = elm.Dot()
    elm.Line().up().at(n.center).length(0.01)
    elm.Resistor().left().at(n.center).length(1.5).label('$R$', loc='top'); elm.Ground()
    elm.Line().right().at(op.out).length(0.6); o = elm.Dot()
    elm.Line().up().at(o.center).length(2.0); elm.LED().left().tox(n.center[0]).label('$R_L$', loc='top'); elm.Line().down().toy(n.center[1])
    save(d, 'E1-17-v-to-i')

with drawing() as d:   # I->I
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().left().at(op.in1).length(1.0); n = elm.Dot()
    elm.SourceI().left().at(n.center).reverse().label('$i_i$'); elm.Ground()
    elm.Line().right().at(op.out).length(0.8); o = elm.Dot()
    elm.LED().up().at(o.center).length(2.6).label('$R_L$', loc='bottom'); x = elm.Dot().label('X', loc='top')
    elm.Resistor().left().at(x.center).tox(n.center[0]).label('$R_2$')
    elm.Line().down().toy(n.center[1])
    elm.Line().right().at(x.center).length(1.2); elm.Resistor().down().label('$R_1$', loc='bottom'); elm.Ground()
    save(d, 'E1-17-i-to-i')
