# E3-13: diff pair with PMOS current-source (active) loads and finite tail resistance
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
from diffpair import diff_pair
import schemdraw.elements as elm
with drawing() as d:
    q1, q2, tail = diff_pair(d)
    p3 = elm.PFet().right().reverse().anchor('drain').at(q1.drain)
    p4 = elm.PFet().left().reverse().flip().anchor('drain').at(q2.drain)
    for p in (p3, p4):
        elm.Line().up().at(p.source).length(0.4); elm.Vdd().label('$V_{DD}$')
    elm.Line().left().at(p3.gate).length(0.6); elm.Dot(open=True).label('$V_B$', loc='left')
    elm.Line().right().at(p4.gate).length(0.6); elm.Dot(open=True).label('$V_B$', loc='right')
    elm.Label().at((p3.gate[0] - 0.2, p3.gate[1] + 0.5)).label('$Q_3$')
    elm.Label().at((p4.gate[0] + 0.2, p4.gate[1] + 0.5)).label('$Q_4$')
    elm.Dot().at(q1.drain).label('$v_{o1}$', loc='left'); elm.Dot().at(q2.drain).label('$v_{o2}$', loc='right')
    elm.Dot().at(tail)
    t = elm.SourceI().down().at(tail).label('$I$', loc='bottom'); elm.Vss()
    elm.Line().right().at(tail).length(1.6); elm.Resistor().down().label('$R_{SS}$', loc='bottom')
    elm.Line().left().length(1.6)
    save(d, 'E3-13-active-load')
