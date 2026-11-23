# E4-02: CS high-frequency small-signal model (Cgs, Cgd bridging, CL)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
Y = -3
with drawing() as d:
    elm.SourceSin().up().at((0, Y)).toy(0).label('$v_s$', loc='top')
    elm.Resistor().right().label('$R_s$'); g = elm.Dot().label('G', loc='top')
    gx = g.center[0]
    elm.Capacitor().down().at(g.center).toy(Y).label('$C_{gs}$', loc='top')
    up = elm.Line().up().at(g.center).length(1.4).end
    elm.Capacitor().right().at(up).length(5.0).label('$C_{gd}$')
    dx = gx + 5.0
    elm.Line().down().toy(0); elm.Dot().at((dx, 0)).label('D', loc='top', ofst=(0.3, 0))
    elm.Line().left().at((dx, 0)).length(2.0)
    elm.SourceControlledI().down().toy(Y).label('$g_m v_{gs}$', loc='top')
    elm.Resistor().down().at((dx, 0)).toy(Y).label('$R_L$', loc='bottom')
    elm.Line().right().at((dx, 0)).length(1.8); c = elm.Dot()
    elm.Capacitor().down().at(c.center).toy(Y).label('$C_L$', loc='bottom')
    elm.Line().right().at(c.center).length(0.6); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.Line().at((0, Y)).to((dx + 1.8, Y)); elm.Ground().at((gx + 2.5, Y))
    save(d, 'E4-02-cs-hf-model')
