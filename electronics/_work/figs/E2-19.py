# E2-19 figures: CS + CD driving speaker; CS-CG sharing one 2 mA source
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:   # CS + CD
    elm.Dot(open=True).label('$v_s$', loc='left')
    elm.Line().right().length(0.8)
    q1 = elm.NFet().anchor('gate').reverse().label('$Q_1$', loc='right', ofst=(0.5, 0.2))
    elm.Line().down().at(q1.source).length(0.3); elm.Ground()
    dn = elm.Dot().at(q1.drain)
    elm.Resistor().up().at(dn.center).label('$R_D$ 5 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(dn.center).length(1.6)
    q2 = elm.NFet().anchor('gate').reverse().label('$Q_2$', loc='right', ofst=(0.5, 0.2))
    elm.Line().up().at(q2.drain).length(0.8); elm.Vdd().label('10 V')
    s = elm.Dot().at(q2.source)
    elm.SourceI().down().at(s.center).label('100 mA', loc='top'); elm.Vss().label('−10 V')
    elm.Capacitor().right().at(s.center).length(2.2).label('$C$')
    o = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().label('$R_L$ 0.1 kΩ', loc='bottom'); elm.Ground()
    save(d, 'E2-19-cs-cd')

