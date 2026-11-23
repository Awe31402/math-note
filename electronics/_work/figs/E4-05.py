# E4-05: common-emitter stage followed by an emitter follower driving R_L
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm
with drawing() as d:
    elm.Dot(open=True).at((0, 0)).label('$v_s$', loc='left'); elm.Line().right().length(0.8)
    q1 = elm.BjtNpn().anchor('base')
    elm.Line().down().at(q1.emitter).length(0.3); elm.Ground()
    c = elm.Dot().at(q1.collector)
    elm.Resistor().up().at(q1.collector).label('$R_C$', loc='bottom'); elm.Vdd().label('$V_{CC}$')
    elm.Line().right().at(q1.collector).length(1.6)
    q2 = elm.BjtNpn().anchor('base')
    elm.Line().up().at(q2.collector).length(0.6); elm.Vdd().label('$V_{CC}$')
    o = elm.Dot().at(q2.emitter)
    elm.SourceI().down().at(q2.emitter).label('$I$ (10 mA)', loc='bottom'); elm.Vss().label('$-V_{EE}$')
    elm.Line().right().at(q2.emitter).length(3.4); p = elm.Dot()
    elm.Resistor().down().at(p.center).label('$R_L$', loc='bottom'); elm.Ground()
    elm.Line().right().at(p.center).length(0.6); elm.Dot(open=True).label('$v_o$', loc='right')
    elm.Label().at((q1.base[0] + 1.3, q1.base[1] - 0.2)).label('$Q_1$')
    elm.Label().at((q2.base[0] + 1.3, q2.base[1] + 0.2)).label('$Q_2$')
    elm.Label().at((q2.emitter[0] + 3.2, q2.emitter[1] + 1.4)).label('$R_{out}$ = $R_C$/(1+β) + $r_e$')
    save(d, 'E4-05-ce-follower')
