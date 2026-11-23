# E3-11: resistively loaded MOS differential pair
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
from diffpair import diff_pair
import schemdraw.elements as elm
with drawing() as d:
    q1, q2, tail = diff_pair(d)
    for q, lab, side in ((q1, '$v_{D1}$', 'left'), (q2, '$v_{D2}$', 'right')):
        dd = elm.Dot().at(q.drain).label(lab, loc=side)
        elm.Resistor().up().at(q.drain).label('$R_D$', loc='top' if side=='left' else 'bottom'); elm.Vdd().label('$V_{DD}$')
    elm.Dot().at(tail)
    elm.SourceI().down().at(tail).label('$I$', loc='bottom'); elm.Vss().label('$-V_{SS}$')
    save(d, 'E3-11-diff-pair')
