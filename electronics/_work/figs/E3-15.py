# E3-15: two-stage CMOS op amp (current-mirror-loaded diff pair + PMOS CS stage)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
from diffpair import diff_pair
import schemdraw.elements as elm
with drawing() as d:
    q1, q2, tail = diff_pair(d, inL='$v_{-}$', inR='$v_{+}$')
    p3 = elm.PFet().left().reverse().flip().anchor('drain').at(q1.drain)
    p4 = elm.PFet().right().reverse().anchor('drain').at(q2.drain)
    for p in (p3, p4):
        elm.Line().up().at(p.source).length(0.4); elm.Vdd().label('$V_{DD}$')
    elm.Line().at(p3.gate).to(p4.gate)
    k = (p3.gate[0] + 0.4, p3.gate[1]); elm.Dot().at(k)
    elm.Line().at(k).to((k[0], q1.drain[1])); elm.Line().to(q1.drain)
    elm.Label().at((p3.drain[0] - 0.7, p3.gate[1])).label('$Q_3$')
    elm.Label().at((p4.drain[0] + 0.7, p4.gate[1] + 0.3)).label('$Q_4$')
    n = elm.Dot().at(q2.drain).label('$v_{o1}$', loc='bottom', ofst=(0.5, 0))
    elm.Dot().at(tail); elm.SourceI().down().at(tail).label('$2I$', loc='bottom'); elm.Vss()
    # second stage
    elm.Line().right().at(q2.drain).length(2.6)
    p6 = elm.PFet().anchor('gate').reverse()
    elm.Label().at((p6.gate[0] - 0.1, p6.gate[1] + 0.5)).label('$Q_6$')
    elm.Line().up().at(p6.source).length(0.4); elm.Vdd().label('$V_{DD}$')
    o = elm.Dot().at(p6.drain)
    elm.Line().right().at(p6.drain).length(1.2); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.SourceI().down().at(p6.drain).label('$I_6$', loc='bottom'); elm.Vss()
    save(d, 'E3-15-two-stage-opamp')
