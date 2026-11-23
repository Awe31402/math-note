"""Small helper library for the block / protocol / tree diagrams in the notes.

The diagrams_lectureXX.py scripts import this.  Every figure is drawn in
"grid units" (1 unit = UNIT inches) so coordinates can be read off the old
ASCII sketches.  Output goes to ../images/<name>.png.

Rebuild every diagram (from the cryptography-notes folder):
    for f in scripts/diagrams_lecture*.py; do python3 "$f"; done

Needs matplotlib >= 3.6 (font fallback: Latin/math glyphs from DejaVu Sans,
Chinese from Noto Sans CJK TC).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "images"
UNIT = 0.55  # inches per grid unit
FS = 11  # base font size

def _cjk_font():
    """matplotlib only reads the first face of a .ttc (the JP one), so pull
    the Traditional-Chinese face out into a cached .otf once."""
    from matplotlib import font_manager as fm
    cache = Path.home() / ".cache" / "crypto-notes-fonts" / "NotoSansCJKtc-Regular.otf"
    if not cache.exists():
        try:
            from fontTools.ttLib import TTCollection
            ttc = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
            for face in TTCollection(ttc).fonts:
                if face["name"].getDebugName(1) == "Noto Sans CJK TC":
                    cache.parent.mkdir(parents=True, exist_ok=True)
                    face.save(cache)
                    break
        except Exception:  # fall back to whatever CJK font is installed
            return "Noto Sans CJK JP"
    if cache.exists():
        fm.fontManager.addfont(str(cache))
        return "Noto Sans CJK TC"
    return "Noto Sans CJK JP"


plt.rcParams.update({
    "font.family": ["DejaVu Sans", _cjk_font()],
    "mathtext.fontset": "dejavusans",
    "font.size": FS,
    "savefig.dpi": 160,
})

INK = "#222222"
GRAY = "#888888"
BOX = "#e8f0fb"
BOX_EDGE = "#3b6fb6"
ALT = "#fdf1e2"
ALT_EDGE = "#c77c1e"
GREEN = "#e6f4ea"
GREEN_EDGE = "#2e8b57"
RED = "#c0392b"
PARTY = {"Alice": "#2a62b8", "Bob": "#2e8b57", "Oscar": "#c0392b",
         "KDC": "#7b4bb0", "CA": "#7b4bb0", "CA2": "#7b4bb0"}


class Fig:
    """A canvas measured in grid units; y grows upwards."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.fig = plt.figure(figsize=(w * UNIT, h * UNIT))
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, w)
        self.ax.set_ylim(0, h)
        self.ax.axis("off")

    # ---- primitives -------------------------------------------------
    def text(self, x, y, s, ha="center", va="center", size=None, color=INK,
             weight="normal", style="normal", **kw):
        size = size or FS
        if "$" in s and any(ord(ch) >= 0x2E80 for ch in s.replace("$", "")):
            return self._mixed(x, y, s, ha, va, size, color, weight, **kw)
        return self.ax.text(x, y, s, ha=ha, va=va, fontsize=size,
                            color=color, fontweight=weight, fontstyle=style,
                            linespacing=1.35, **kw)

    def _mixed(self, x, y, s, ha, va, size, color, weight, **kw):
        """Mathtext cannot fall back to the CJK font, so a line that mixes
        Chinese and $math$ is drawn as separate pieces placed side by side."""
        r = self.fig.canvas.get_renderer()
        inv = self.ax.transData.inverted()
        lh = size * 1.35 / 72 / UNIT  # line height in grid units
        lines = s.split("\n")
        n = len(lines)
        # baseline of first line
        asc = size * 0.36 / 72 / UNIT
        if va == "center":
            b0 = y + (n - 1) * lh / 2 - asc
        elif va == "top":
            b0 = y - size * 0.95 / 72 / UNIT
        elif va == "bottom":
            b0 = y + (n - 1) * lh + size * 0.25 / 72 / UNIT
        else:
            b0 = y
        for i, line in enumerate(lines):
            parts = line.split("$")
            pieces = []
            for j, p in enumerate(parts):
                if not p:
                    continue
                pieces.append(f"${p}$" if j % 2 else p)
            arts, widths = [], []
            for p in pieces:
                t = self.ax.text(0, b0 - i * lh, p, ha="left", va="baseline",
                                 fontsize=size, color=color, fontweight=weight,
                                 **kw)
                bb = t.get_window_extent(r)
                (x0, _), (x1, _) = inv.transform([(bb.x0, 0), (bb.x1, 0)])
                arts.append(t)
                widths.append(x1 - x0)
            tot = sum(widths)
            cx = {"left": x, "right": x - tot}.get(ha, x - tot / 2)
            for t, wd in zip(arts, widths):
                t.set_x(cx)
                cx += wd
        return None

    def box(self, x, y, s="", w=2.0, h=0.8, fc=BOX, ec=BOX_EDGE, size=None,
            weight="normal", round_=True, lw=1.3, ls="-", z=2):
        """Box centred at (x, y)."""
        style = "round,pad=0,rounding_size=0.15" if round_ else "square,pad=0"
        p = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=style,
                           fc=fc, ec=ec, lw=lw, ls=ls, zorder=z)
        self.ax.add_patch(p)
        if s:
            self.text(x, y, s, size=size, weight=weight, zorder=z + 1)
        return (x, y, w, h)

    def frame(self, x0, y0, x1, y1, label=None, ec=GRAY, ls="--", fc="none",
              label_pos="top", size=None, z=0):
        """Rectangle given by corners, optional title on its edge."""
        p = FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                           boxstyle="round,pad=0,rounding_size=0.15",
                           fc=fc, ec=ec, lw=1.2, ls=ls, zorder=z)
        self.ax.add_patch(p)
        if label:
            ly = y1 if label_pos == "top" else y0
            self.text((x0 + x1) / 2, ly, label, size=size or FS - 1,
                      color=ec if ec != "none" else INK, zorder=z + 3,
                      bbox=dict(fc="white", ec="none", pad=1.5))

    def arrow(self, *pts, label=None, lpos=0.5, loff=0.22, color=INK,
              lw=1.3, head=True, both=False, ls="-", size=None, lcolor=None,
              lside="above", z=1):
        """Polyline arrow through pts; arrow head at the last point."""
        pts = list(pts)
        for a, b in zip(pts[:-2], pts[1:-1]):
            self.ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw,
                         ls=ls, zorder=z, solid_capstyle="butt")
        a, b = pts[-2], pts[-1]
        style = "<|-|>" if both else ("-|>" if head else "-")
        self.ax.add_patch(FancyArrowPatch(
            a, b, arrowstyle=style, mutation_scale=12, color=color, lw=lw,
            ls=ls, shrinkA=0, shrinkB=0, zorder=z))
        if both and len(pts) > 2:
            pass
        if label is not None:
            # label on the longest segment
            segs = list(zip(pts[:-1], pts[1:]))
            p, q = max(segs, key=lambda s: abs(s[0][0] - s[1][0]) + abs(s[0][1] - s[1][1]))
            mx = p[0] + (q[0] - p[0]) * lpos
            my = p[1] + (q[1] - p[1]) * lpos
            if abs(q[1] - p[1]) < 1e-9:  # horizontal
                dy = loff if lside == "above" else -loff
                self.text(mx, my + dy, label, va="bottom" if dy > 0 else "top",
                          size=size or FS - 1, color=lcolor or color)
            else:
                dx = loff if lside != "left" else -loff
                self.text(mx + dx, my, label, ha="left" if dx > 0 else "right",
                          size=size or FS - 1, color=lcolor or color)

    def line(self, *pts, color=INK, lw=1.3, ls="-", z=1):
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        self.ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=z)

    def op(self, x, y, sym="+", r=0.22, z=3):
        """Circled operator: '+' = XOR (⊕), 'x' = multiply (⊗), 'box+' = ⊞."""
        if sym == "box+":
            self.box(x, y, "", w=2 * r, h=2 * r, fc="white", ec=INK,
                     round_=False, lw=1.3, z=z)
        else:
            self.ax.add_patch(Circle((x, y), r, fc="white", ec=INK, lw=1.3, zorder=z))
        if sym in ("+", "box+"):
            self.line((x - r, y), (x + r, y), z=z + 1)
            self.line((x, y - r), (x, y + r), z=z + 1)
        else:
            d = r * 0.7071
            self.line((x - d, y - d), (x + d, y + d), z=z + 1)
            self.line((x - d, y + d), (x + d, y - d), z=z + 1)
        return (x, y)

    def dot(self, x, y, r=0.06, color=INK, z=3):
        self.ax.add_patch(Circle((x, y), r, fc=color, ec=color, zorder=z))

    def save(self, name):
        OUT.mkdir(exist_ok=True)
        path = OUT / f"{name}.png"
        # crop to the drawn artists only (the invisible axes would otherwise
        # keep all the empty canvas)
        from matplotlib.transforms import Bbox
        r = self.fig.canvas.get_renderer()
        arts = self.ax.texts + self.ax.patches + self.ax.lines
        bbs = [a.get_window_extent(r) for a in arts if a.get_visible()]
        bb = Bbox.union(bbs).transformed(self.fig.dpi_scale_trans.inverted())
        self.fig.savefig(path, facecolor="white", bbox_inches=bb.padded(0.12))
        plt.close(self.fig)
        print("wrote", path.relative_to(OUT.parent))
        return path


# ---------------------------------------------------------------------------
# High-level builders
# ---------------------------------------------------------------------------

def _nlines(s):
    return s.count("\n") + 1


def protocol(name, parties, rows, col_w=5.0, line_h=0.42, margin=0.6,
             widths=None):
    """Message-sequence diagram.

    parties: list of names, e.g. ["Alice", "Bob"].
    rows: list of
        (party, text)               – a note under that party's column
        ("msg", src, dst, label)    – an arrow between two columns
        ("msg", src, dst, label, note) – arrow plus a note on the arrow's row
        ("span", text)              – a note centred across the whole width
        ("gap",)                    – a little vertical space
    Several notes for different parties can be put on one row by passing a
    tuple of rows: (("Alice", "..."), ("Bob", "...")).
    """
    n = len(parties)
    if widths is None:
        widths = [col_w] * n
    xs, acc = [], margin
    for wdt in widths:
        xs.append(acc + wdt / 2)
        acc += wdt
    W = acc + margin

    # measure heights
    def row_height(r):
        if isinstance(r[0], tuple):
            return max(row_height(x) for x in r)
        if r[0] == "gap":
            return 0.35
        if r[0] == "msg":
            extra = _nlines(r[4]) if len(r) > 4 and r[4] else 1
            return max(1.0, line_h * (_nlines(r[3]) + 1.2), line_h * extra + 0.3)
        return line_h * _nlines(r[-1]) + 0.22

    hs = [row_height(r) for r in rows]
    H = sum(hs) + 1.4 + margin
    f = Fig(W, H)
    top = H - margin
    col = {p: x for p, x in zip(parties, xs)}
    for p, x in zip(parties, xs):
        c = PARTY.get(p, INK)
        f.box(x, top - 0.3, p, w=min(widths[parties.index(p)] - 0.6, 2.6),
              h=0.65, fc="white", ec=c, weight="bold")
        f.line((x, top - 0.65), (x, 0.3), color="#d0d0d0", lw=1.0, ls=(0, (4, 3)), z=0)
    y = top - 1.15

    def draw(r, y, h):
        if r[0] == "gap":
            return
        if r[0] == "msg":
            _, s, d, lab = r[:4]
            note = r[4] if len(r) > 4 else None
            yy = y - h / 2 - 0.12
            x0, x1 = col[s], col[d]
            sgn = 1 if x1 > x0 else -1
            f.arrow((x0 + sgn * 0.15, yy), (x1 - sgn * 0.15, yy), label=lab,
                    color=INK, loff=0.1)
            if note:
                f.text((x0 + x1) / 2, yy - 0.12, note, va="top", size=FS - 2,
                       color=GRAY)
            return
        if r[0] == "span":
            f.text(W / 2, y - h / 2, r[1], color=GRAY, size=FS - 1)
            return
        p, s = r
        f.text(col[p], y - h / 2, s, color=INK)

    for r, h in zip(rows, hs):
        if isinstance(r[0], tuple):
            for x in r:
                draw(x, y, h)
        else:
            draw(r, y, h)
        y -= h
    return f.save(name)


def tree(name, root, w=None, level_h=1.5, leaf_w=2.6, box_h=None, size=None,
         fc=BOX, ec=BOX_EDGE, notes=None):
    """Top-down tree.  root = (label, [children...]) or a plain label.

    notes: optional dict label -> small grey text placed under that node.
    """
    notes = notes or {}

    def norm(t):
        return (t, []) if isinstance(t, str) else (t[0], [norm(c) for c in t[1]])

    root = norm(root)

    def leaves(t):
        return 1 if not t[1] else sum(leaves(c) for c in t[1])

    def depth(t):
        return 1 if not t[1] else 1 + max(depth(c) for c in t[1])

    nl, d = leaves(root), depth(root)
    maxlines = 1

    def ml(t):
        nonlocal maxlines
        maxlines = max(maxlines, _nlines(t[0]))
        for c in t[1]:
            ml(c)

    ml(root)
    bh = box_h or 0.45 + 0.38 * maxlines
    W = w or nl * leaf_w + 0.4
    H = d * level_h + 0.6 + (0.5 if notes else 0)
    f = Fig(W, H)

    def place(t, x0, x1, lvl, parent=None):
        x = (x0 + x1) / 2
        y = H - 0.3 - bh / 2 - lvl * level_h
        f.box(x, y, t[0], w=leaf_w - 0.35, h=bh, fc=fc, ec=ec, size=size)
        if t[0] in notes:
            f.text(x, y - bh / 2 - 0.08, notes[t[0]], va="top", size=FS - 2,
                   color=GRAY, zorder=5, bbox=dict(fc="white", ec="none", pad=1))
        if parent:
            px, py = parent
            mid = y + bh / 2 + 0.3
            f.line((px, py - bh / 2), (px, mid), (x, mid))
            f.arrow((x, mid), (x, y + bh / 2))
        acc = x0
        tot = leaves(t)
        for c in t[1]:
            span = (x1 - x0) * leaves(c) / tot
            place(c, acc, acc + span, lvl + 1, (x, y))
            acc += span

    place(root, 0.2, W - 0.2, 0)
    return f.save(name)


def _vislen(s):
    """Rough printed width of a label in 'character units' (CJK = 2)."""
    import re
    s = re.sub(r"\\[a-zA-Z]+", "x", s)
    s = re.sub(r"[${}]", "", s)
    out = 0.0
    in_sub = False
    for ch in s:
        if ch in "_^":
            in_sub = True
            continue
        w = 1.9 if ord(ch) > 0x2E80 else 1.0
        out += w * (0.7 if in_sub else 1.0)
        in_sub = False if ch in " " else in_sub
    return out


def chain(name, items, labels=None, gap=1.1, box_h=0.8, size=None,
          below=None, above=None, pad=0.5, caption=None):
    """Horizontal pipeline.  items: list of str; a str starting with '[' is
    drawn as a box (brackets removed), '(+)' as an XOR circle, anything else
    as plain text.  labels: list of arrow labels (len(items) - 1) or None.
    below/above: dict index -> text drawn under/over that item (with an
    arrow pointing into it).  caption: dict index -> grey text right under
    that item (no arrow)."""
    caption = caption or {}
    below = below or {}
    above = above or {}
    widths = []
    for it in items:
        if it == "(+)":
            widths.append(0.5)
        else:
            s = it[1:-1] if it.startswith("[") else it
            longest = max(_vislen(l) for l in s.split("\n"))
            pad_box = 0.7 if it.startswith("[") else 0.1
            widths.append(max(0.5, 0.2 * longest + pad_box))
    W = sum(widths) + gap * (len(items) - 1) + 2 * pad
    H = box_h + 1.0 + (1.3 if below else (0.6 if caption else 0)) + (1.3 if above else 0)
    f = Fig(W, H)
    y = (1.3 if below else (0.6 if caption else 0)) + 0.5 + box_h / 2
    x = pad
    centers = []
    for it, wd in zip(items, widths):
        cx = x + wd / 2
        if it == "(+)":
            f.op(cx, y)
        elif it.startswith("["):
            f.box(cx, y, it[1:-1], w=wd, h=box_h, size=size)
        else:
            f.text(cx, y, it, size=size)
        centers.append((cx, wd))
        x += wd + gap
    for i in range(len(items) - 1):
        (c0, w0), (c1, w1) = centers[i], centers[i + 1]
        lab = labels[i] if labels else None
        f.arrow((c0 + w0 / 2 + 0.08, y), (c1 - w1 / 2 - 0.08, y), label=lab,
                loff=0.08)
    for i, s in below.items():
        cx, wd = centers[i]
        hh = 0.25 if items[i] == "(+)" else box_h / 2
        f.text(cx, y - hh - 1.0, s, va="top")
        f.arrow((cx, y - hh - 0.95), (cx, y - hh - 0.03))
    for i, s in caption.items():
        cx, wd = centers[i]
        f.text(cx, y - box_h / 2 - 0.1, s, va="top", size=FS - 1, color=GRAY)
    for i, s in above.items():
        cx, wd = centers[i]
        hh = 0.25 if items[i] == "(+)" else box_h / 2
        f.text(cx, y + hh + 1.0, s, va="bottom")
        f.arrow((cx, y + hh + 0.95), (cx, y + hh + 0.03))
    return f.save(name)


def vchain(name, items, side=None, w=None, step=1.15, box_w=3.0, box_h=0.7,
           side_text=None, left=None):
    """Vertical pipeline (top to bottom).  items as in chain().
    side: dict index -> text fed into that item from the right (arrow ←).
    side_text: dict index -> grey remark to the right (no arrow).
    left: dict index -> text fed in from the left (arrow →)."""
    side = side or {}
    side_text = side_text or {}
    left = left or {}
    n = len(items)
    W = w or box_w + 7.0
    H = n * step + 0.4
    f = Fig(W, H)
    cx = W / 2 if not left else W / 2 + 0.6
    ys = [H - 0.5 - i * step for i in range(n)]
    hh = []
    for it, y in zip(items, ys):
        if it.startswith("["):
            f.box(cx, y, it[1:-1], w=box_w, h=box_h)
            hh.append(box_h / 2)
        elif it == "(+)":
            f.op(cx, y)
            hh.append(0.22)
        else:
            f.text(cx, y, it)
            hh.append(0.22)
    for i in range(n - 1):
        f.arrow((cx, ys[i] - hh[i] - 0.05), (cx, ys[i + 1] + hh[i + 1] + 0.05))
    for i, s in side.items():
        x0 = cx + (box_w / 2 if items[i].startswith("[") else 0.25)
        f.arrow((x0 + 1.0, ys[i]), (x0 + 0.05, ys[i]))
        f.text(x0 + 1.15, ys[i], s, ha="left")
    for i, s in left.items():
        x0 = cx - (box_w / 2 if items[i].startswith("[") else 0.25)
        f.arrow((x0 - 1.0, ys[i]), (x0 - 0.05, ys[i]))
        f.text(x0 - 1.15, ys[i], s, ha="right")
    for i, s in side_text.items():
        x0 = cx + (box_w / 2 if items[i].startswith("[") else 0.6)
        f.text(x0 + 0.3, ys[i], s, ha="left", color=GRAY, size=FS - 1)
    return f.save(name)


def channel(name, enc="$e_k$", dec="$d_k$", key_label="安全通道",
            key_color=None, oscar=False):
    """Alice → e → insecure channel → d → Bob, with keys on a (secure)
    channel underneath.  key_label=None draws no key channel."""
    kc = key_color or GREEN_EDGE
    with_key = key_label is not None
    f = Fig(15, 4.2 if with_key else 4.0)
    y = 2.6 if with_key else 1.0
    f.text(0.8, y, "Alice", weight="bold", color=PARTY["Alice"])
    f.box(3.3, y, enc, w=1.4)
    f.box(11.0, y, dec, w=1.4)
    f.text(14.0, y, "Bob", weight="bold", color=PARTY["Bob"])
    f.arrow((1.4, y), (2.6, y), label="x")
    f.arrow((4.0, y), (5.4, y), label="y")
    f.box(7.15, y, "不安全通道", w=3.3, h=0.7, fc="#fbeaea", ec=RED)
    f.arrow((8.8, y), (10.3, y), label="y")
    f.arrow((11.7, y), (13.4, y), label="x")
    if with_key:
        f.text(7.15, 0.6, key_label, color=kc)
        f.text(3.3, 0.6, "k")
        f.text(11.0, 0.6, "k")
        f.arrow((3.6, 0.6), (6.0, 0.6), both=True, color=kc)
        f.arrow((8.3, 0.6), (10.7, 0.6), both=True, color=kc)
        f.arrow((3.3, 0.85), (3.3, y - 0.4))
        f.arrow((11.0, 0.85), (11.0, y - 0.4))
    if oscar:
        f.text(7.15, 3.5, "Oscar（壞人）", weight="bold", color=RED)
        f.arrow((7.15, y + 0.4), (7.15, 3.2), label="只看到 y", color=RED)
    return f.save(name)


def blackbox(name, top, bottom, label, key, key_note=None, box_w=2.6):
    """Block cipher as a black box: input on top, output below, key left."""
    f = Fig(10, 4.4)
    cx = 5.0
    f.text(cx, 4.0, top)
    f.arrow((cx, 3.7), (cx, 2.65))
    f.box(cx, 2.2, label, w=box_w, h=0.9, weight="bold")
    f.arrow((cx, 1.75), (cx, 0.75))
    f.text(cx, 0.4, bottom)
    f.text(cx - box_w / 2 - 1.3, 2.2, key, ha="right")
    f.arrow((cx - box_w / 2 - 1.2, 2.2), (cx - box_w / 2 - 0.05, 2.2))
    if key_note:
        f.text(cx + box_w / 2 + 0.4, 2.2, key_note, ha="left", color=GRAY, size=FS - 1)
    return f.save(name)
