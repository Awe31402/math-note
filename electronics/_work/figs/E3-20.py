# E3-20: op amp + NMOS laser driver (series-series feedback, laser in drain)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    op = elm.Opamp(leads=True).flip().right()
    elm.Line().left().at(op.in2).length(1.0); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().right().at(op.out).length(0.8)
    q = elm.NFet().anchor('gate').reverse()
    elm.Label().at((q.gate[0] + 0.1, q.gate[1] - 0.5)).label('$Q$')
    elm.LED().up().at(q.drain).reverse().label('laser', loc='bottom'); elm.Vdd().label('$V_{DD}$')
    s = elm.Dot().at(q.source)
    t = elm.Line().down().at(q.source).length(1.2).end; elm.Dot().at(t)
    elm.Resistor().down().at(t).label('$R$', loc='bottom'); elm.Ground()
    n = elm.Line().left().at(op.in1).length(0.6).end
    elm.Line().at(n).to((n[0], t[1])); elm.Line().to(t)
    elm.Label().at((q.source[0] + 1.8, q.source[1] - 0.6)).label('$i_o$ ≈ $v_i$/R')
    save(d, 'E3-20-laser-driver')
