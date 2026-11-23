# E3-16: non-inverting amplifier with input offset voltage source
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    op = elm.Opamp(leads=True).flip().right()          # in2 (+) on top, in1 (-) at bottom
    elm.Line().left().at(op.in2).length(0.6)
    elm.BatteryCell().left().label('$V_{OS}$', loc='top')
    elm.Line().left().length(0.6); elm.Dot(open=True).label('$v_i$', loc='left')
    n = elm.Line().left().at(op.in1).length(0.8).end; elm.Dot().at(n)
    m = elm.Line().down().at(n).length(1.2).end; elm.Dot().at(m)
    elm.Resistor().down().at(m).label('$R_1$', loc='bottom'); elm.Ground()
    elm.Resistor().right().at(m).tox(op.out[0] + 0.6).label('$R_2$', loc='bottom')
    elm.Line().up().toy(op.out[1]); elm.Line().left().tox(op.out[0])
    elm.Dot().at((op.out[0] + 0.6, op.out[1]))
    elm.Line().right().at((op.out[0] + 0.6, op.out[1])).length(0.8); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.Label().at((op.out[0] - 1.2, op.out[1] + 1.3)).label('$A_d$, $R_o$')
    save(d, 'E3-16-noninv-offset')
