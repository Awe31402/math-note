# shared helpers for schemdraw figures
import os, schemdraw
schemdraw.use('svg')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'figures')
def save(d, name): d.save(os.path.join(OUT, f'{name}.svg'))
def drawing(): 
    d = schemdraw.Drawing(show=False); d.config(unit=3, fontsize=14); return d
