# E4-01: discrete CS amplifier with coupling capacitors C1, C3 and source bypass C2
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    elm.Ground().at((0, -1.5)); elm.SourceSin().up().at((0, -1.5)).label('$v_s$', loc='top')
    elm.Resistor().right().label('$R_s$')
    elm.Capacitor().right().label('$C_1$')
    g = elm.Dot()
    elm.Resistor().down().at(g.center).label('$R_G$', loc='bottom'); elm.Ground()
    elm.Line().right().at(g.center).length(0.8)
    q = elm.NFet().anchor('gate').reverse()
    elm.Resistor().up().at(q.drain).label('$R_D$', loc='bottom'); elm.Vdd().label('$V_{DD}$')
    s = elm.Line().down().at(q.source).length(0.4).end; elm.Dot().at(s)
    elm.Resistor().down().at(s).label('$R_S$', loc='top'); elm.Vss().label('$-V_{SS}$')
    elm.Line().right().at(s).length(1.4); elm.Capacitor().down().label('$C_2$', loc='bottom'); elm.Ground()
    elm.Dot().at(q.drain); elm.Line().right().at(q.drain).length(0.8)
    elm.Capacitor().right().label('$C_3$'); o = elm.Dot()
    elm.Resistor().down().at(o.center).label('$R_L$', loc='bottom'); elm.Ground()
    elm.Line().right().at(o.center).length(0.6); elm.Dot(open=True).label('$v_o$', loc='right')
    save(d, 'E4-01-cs-coupling-caps')
