# E2-26 figure: cascode amplifier with cascode PMOS current-source load
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm

with drawing() as d:
    gap = 0.8
    def nmos(gx, gy, lab):
        elm.Line().right().at((gx-1.0, gy)).length(1.0)
        return elm.NFet().anchor('gate').reverse().label(lab, loc='right', ofst=(0.4, 0))
    def pmos(gx, gy, lab):
        elm.Line().right().at((gx-1.0, gy)).length(1.0)
        return elm.PFet().anchor('gate').reverse().label(lab, loc='right', ofst=(0.4, 0))
    q1 = nmos(0, 0, '$Q_1$'); elm.Dot(open=True).at((-1.0, 0)).label('$v_s$ (+2 V)', loc='left')
    elm.Line().down().at(q1.source).length(0.3); elm.Ground()
    y2 = q1.drain[1] + gap + 0.75
    q2 = nmos(0, y2, '$Q_2$'); elm.Dot(open=True).at((-1.0, y2)).label('$V_{G2}$', loc='left')
    elm.Line().at(q1.drain).to(q2.source)
    o = elm.Dot().at((q2.drain[0], q2.drain[1] + gap/2))
    elm.Line().at(q2.drain).to(o.center)
    y3 = o.center[1] + gap/2 + 0.75
    q3 = pmos(0, y3, '$Q_3$'); elm.Dot(open=True).at((-1.0, y3)).label('$V_{G3}$', loc='left')
    elm.Line().at(q3.drain).to(o.center)
    y4 = q3.source[1] + gap + 0.75
    q4 = pmos(0, y4, '$Q_4$'); elm.Dot(open=True).at((-1.0, y4)).label('8 V', loc='left')
    elm.Line().at(q4.drain).to(q3.source)
    elm.Line().up().at(q4.source).length(0.3); elm.Vdd().label('10 V')
    elm.Line().right().at(o.center).length(1.5); elm.Dot(open=True).label('$v_O$', loc='right')
    save(d, 'E2-26-cascode')
