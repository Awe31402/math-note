# E1-09 figures: one-stage MOS amplifier (full), its AC equivalent, two-stage cascade
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm

def stage(d, x0, cin_from=None, label_in='$v_s$'):
    """bias divider + coupling cap + NMOS + 5k load at x offset x0; returns (gate node, drain node)"""
    vdd = elm.Vdd().at((x0, 6)).label('10 V')
    elm.Resistor().down().at((x0, 6)).length(3).label('80 kΩ', loc='bottom')
    g = elm.Dot()
    elm.Resistor().down().length(3).label('20 kΩ', loc='bottom'); elm.Ground()
    elm.Line().right().at(g.center).length(1)
    q = elm.NFet(bulk=False).anchor('gate').reverse()
    elm.Ground().at(q.source)
    elm.Resistor().up().at(q.drain).length(2.2).label('5 kΩ', loc='top'); elm.Vdd().label('10 V')
    dn = elm.Dot().at(q.drain)
    return g, dn

with drawing() as d:
    g, dn = stage(d, 0)
    c = elm.Capacitor().left().at(g.center).length(2.5).label('$C$')
    elm.SourceSin().down().label('$v_s$', loc='top'); elm.Ground()
    elm.Line().right().at(dn.center).length(1.5); elm.Dot(open=True).label('$v_o$', loc='right')
    save(d, 'E1-09-one-stage')

with drawing() as d:   # AC equivalent
    s = elm.SourceSin().up().label('$v_s$', loc='top'); elm.Ground().at(s.start)
    elm.Capacitor().right().at(s.end).label('$C$'); n = elm.Dot().label('$v_i$', loc='top')
    elm.Resistor().down().at(n.center).label('16 kΩ', loc='bottom').label('80∥20', loc='top'); elm.Ground()
    elm.Line().right().at(n.center).length(2.5).linestyle(':')
    elm.Dot(open=True)
    src = elm.SourceControlledI().down().at((7.5, 0)).label('$2v_i$', loc='bottom')
    o = elm.Dot().at((7.5, 0)).label('$v_o$', loc='top')
    elm.Ground().at(src.end)
    elm.Line().right().at(o.center).length(2.5)
    elm.Resistor().down().label('5 kΩ', loc='bottom'); elm.Ground()
    save(d, 'E1-09-ac-equivalent')

with drawing() as d:
    g1, d1 = stage(d, 0)
    elm.Capacitor().left().at(g1.center).length(2.5).label('$C$')
    elm.SourceSin().down().label('$v_s$', loc='top'); elm.Ground()
    g2, d2 = stage(d, 8)
    elm.Wire('-|').at(d1.center).to((g2.center[0]-2.5, g2.center[1])); elm.Dot()
    elm.Capacitor().right().at((g2.center[0]-2.5, g2.center[1])).to(g2.center).label('$C$')
    elm.Line().right().at(d2.center).length(1.5); elm.Dot(open=True).label('$v_o$', loc='right')
    save(d, 'E1-09-two-stage')
