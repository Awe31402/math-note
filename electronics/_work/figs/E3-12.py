# E3-12: differential-mode and common-mode half circuits
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    for x, vin, src, title in ((0, '$v_{id}/2$', None, 'DM half circuit'), (6.5, '$v_{icm}$', '$2R_{SS}$', 'CM half circuit')):
        elm.Dot(open=True).at((x, 0)).label(vin, loc='left')
        elm.Line().right().length(0.8)
        q = elm.NFet().anchor('gate').reverse()
        elm.Resistor().up().at(q.drain).label('$R_D$', loc='bottom'); elm.Vdd().label('$V_{DD}$')
        elm.Dot().at(q.drain); elm.Line().right().at(q.drain).length(1.0); elm.Dot(open=True).label('$v_o$', loc='right')
        if src:
            elm.Resistor().down().at(q.source).label(src, loc='bottom'); elm.Ground()
        else:
            elm.Line().down().at(q.source).length(0.4); elm.Ground()
        elm.Label().at((x + 1.6, -5.2)).label(title)
    save(d, 'E3-12-half-circuits')
