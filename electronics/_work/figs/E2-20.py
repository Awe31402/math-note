# E2-20 figure: two CS transistors sharing a 2 mA tail source (complementary outputs)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:
    elm.Dot(open=True).label('$v_s$', loc='left')
    elm.Line().right().length(1.0)
    q1 = elm.NFet().anchor('gate').reverse().label('$Q_1$', loc='left', ofst=(-0.1, -1.0))
    xs, ys = q1.source
    elm.Line().right().at(q1.source).length(2.4)
    gx = xs + 2.4 + 1.37
    elm.Ground().at((gx+1.0, ys+0.75))
    elm.Line().left().at((gx+1.0, ys+0.75)).length(1.0)
    q2 = elm.NFet().anchor('gate').reverse().flip().label('$Q_2$', loc='left', ofst=(0.1, -1.0))
    t = elm.Dot().at((xs+1.2, ys))
    elm.SourceI().down().at(t.center).label('2 mA', loc='top'); elm.Vss().label('−10 V')
    for q, nm, side in [(q1, '$v_{o1} = 5 - 5v_s$', 'left'), (q2, '$v_{o2} = 5 + 5v_s$', 'right')]:
        dd = elm.Dot().at(q.drain)
        elm.Resistor().up().at(dd.center).label('5 kΩ', loc='top' if side == 'left' else 'bottom'); elm.Vdd().label('10 V')
        elm.Line().at(dd.center).length(1.0).left() if side == 'left' else elm.Line().at(dd.center).length(1.0).right()
        elm.Dot(open=True).label(nm, loc=side)
    save(d, 'E2-20-shared-tail')
