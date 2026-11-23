# shared helpers for schemdraw figures
import os, schemdraw
schemdraw.use('svg')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'figures')
def save(d, name):
    from whitebg import add_bg
    f = os.path.join(OUT, f'{name}.svg'); d.save(f); add_bg(f)
def drawing(): 
    d = schemdraw.Drawing(show=False); d.config(unit=3, fontsize=14); return d
def mpl():
    """matplotlib with CJK text usable inside mathtext strings"""
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    plt.rcParams.update({'font.sans-serif': ['Noto Sans CJK JP', 'DejaVu Sans'], 'axes.unicode_minus': False,
                         'mathtext.fontset': 'custom', 'mathtext.rm': 'Noto Sans CJK JP',
                         'mathtext.it': 'DejaVu Sans:italic', 'mathtext.bf': 'DejaVu Sans:bold',
                         'mathtext.sf': 'DejaVu Sans', 'mathtext.cal': 'DejaVu Sans'})
    return plt
def clean(*axs):
    for a in axs: a.spines[['top', 'right']].set_visible(False)
