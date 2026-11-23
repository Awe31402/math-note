# E1-01 figures: basic circuit, parallel, series, worked example
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing
import schemdraw.elements as elm

# 1. battery + resistor loop
with drawing() as d:
    b = elm.BatteryCell().up().reverse().label('1.5 V', loc='top')   # long plate (+) on top
    elm.Line().right().at(b.end).length(3).label('$I$ →')
    r = elm.Resistor().down().label('$R$', loc='bottom')
    elm.Line().left().to(b.start)
    save(d, 'E1-01-basic')

# 2. parallel
with drawing() as d:
    b = elm.BatteryCell().up().reverse().label('$V$', loc='top')
    elm.Ground().at(b.start)
    w = elm.Line().right().at(b.end).length(2.5).label('$I$ →')
    elm.Resistor().down().at(w.end).label('$R_1$', loc='top').label('$V/R_1$', loc='bottom')
    elm.Ground()
    elm.Line().right().at(w.end).length(3)
    elm.Resistor().down().label('$R_2$', loc='top').label('$V/R_2$', loc='bottom')
    elm.Ground()
    save(d, 'E1-01-parallel')

# 3. series (voltage divider)
with drawing() as d:
    b = elm.BatteryCell().up().reverse().label('$V$', loc='top')
    elm.Ground().at(b.start)
    elm.Resistor().right().at(b.end).label('$R_1$').label('$I$ →', loc='bottom')
    n = elm.Dot().label('$v_O$', loc='right')
    elm.Resistor().down().at(n.center).label('$R_2$', loc='top')
    elm.Ground()
    save(d, 'E1-01-series')

# 4. worked example
with drawing() as d:
    b = elm.BatteryCell().up().reverse().label('10 V', loc='top')
    elm.Ground().at(b.start)
    elm.Resistor().right().at(b.end).label('5 Ω').label('1 A →', loc='bottom')
    n = elm.Dot().label('5 V', loc='top')
    elm.Resistor().down().at(n.center).label('10 Ω', loc='top').label('0.5 A', loc='bottom')
    elm.Ground()
    elm.Line().right().at(n.center).length(3)
    elm.Resistor().down().label('10 Ω', loc='top').label('0.5 A', loc='bottom')
    elm.Ground()
    save(d, 'E1-01-example')
