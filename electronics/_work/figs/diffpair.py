# helper: MOS differential pair (Q1 gate left, Q2 gate right, sources tied)
import schemdraw.elements as elm
def diff_pair(d, x0=0, y0=0, gap=6, inL='$v_{G1}$', inR='$v_{G2}$', n1='$Q_1$', n2='$Q_2$'):
    elm.Dot(open=True).at((x0, y0)).label(inL, loc='left')
    elm.Line().right().length(0.8)
    q1 = elm.NFet().anchor('gate').reverse()
    elm.Dot(open=True).at((x0 + gap + 1.6, y0)).label(inR, loc='right')
    elm.Line().left().length(0.8)
    q2 = elm.NFet().anchor('gate').reverse().flip()
    elm.Label().at((q1.gate[0] - 0.35, q1.gate[1] - 0.45)).label(n1)
    elm.Label().at((q2.gate[0] + 0.35, q2.gate[1] - 0.45)).label(n2)
    a = elm.Line().down().at(q1.source).length(0.5).end
    b = elm.Line().down().at(q2.source).length(0.5).end
    elm.Line().at(a).to(b)
    tail = ((a[0] + b[0]) / 2, a[1])
    return q1, q2, tail
