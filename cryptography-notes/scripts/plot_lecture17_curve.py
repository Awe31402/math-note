"""Plot E: y^2 = x^3 + 2x + 2 over R and over GF(17), labelling every kP.

Used by lecture17_note.md section 1.1. Run from anywhere:
    python3 scripts/plot_lecture17_curve.py
Output: images/lecture17_curve_mod17.png (next to this scripts/ folder).

The points are computed with the lecture 16 point-addition formulas starting
from the generator P = (5, 1), then cross-checked against the table in the
note and against a brute-force enumeration of all solutions mod 17.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

A, B, MOD = 2, 2, 17
GEN = (5, 1)
O = None  # point at infinity

# Table from lecture17_note.md section 1.1 (textbook Example 9.6), k = 1..18
NOTE_TABLE = [
    (5, 1), (6, 3), (10, 6), (3, 1), (9, 16), (16, 13), (0, 6), (13, 7),
    (7, 6), (7, 11), (13, 10), (0, 11), (16, 4), (9, 1), (3, 16), (10, 11),
    (6, 14), (5, 16),
]


def add(p, q):
    """Point addition / doubling on E over GF(MOD) (lecture 16 formulas)."""
    if p is O:
        return q
    if q is O:
        return p
    (x1, y1), (x2, y2) = p, q
    if x1 == x2 and (y1 + y2) % MOD == 0:
        return O  # Q = -P (covers doubling with y1 = 0)
    if p == q:
        s = (3 * x1 * x1 + A) * pow(2 * y1, -1, MOD) % MOD
    else:
        s = (y2 - y1) * pow(x2 - x1, -1, MOD) % MOD
    x3 = (s * s - x1 - x2) % MOD
    y3 = (s * (x1 - x3) - y1) % MOD
    return (x3, y3)


def multiples(gen):
    """Return [P, 2P, ...] up to (but excluding) the first O."""
    pts, cur = [], gen
    while cur is not O:
        pts.append(cur)
        cur = add(cur, gen)
    return pts


def check(pts):
    assert pts == NOTE_TABLE, "computed kP differ from the note's table"
    brute = {(x, y) for x in range(MOD) for y in range(MOD)
             if (y * y - (x ** 3 + A * x + B)) % MOD == 0}
    assert len(brute) == 18 and brute == set(pts), "brute force mismatch"
    for k, (x, y) in enumerate(pts, start=1):  # kP and (19-k)P are inverses
        assert pts[19 - k - 1] == (x, (-y) % MOD)
    print(f"checks passed: {len(pts)} points, #E = {len(pts) + 1}")


def plot(pts, out):
    fig, (ax_r, ax_p) = plt.subplots(1, 2, figsize=(13, 6.2),
                                     gridspec_kw={"width_ratios": [1, 1.25]})

    # Left: the same equation over the reals
    xs = np.linspace(-1.5, 4, 4000)
    rhs = xs ** 3 + A * xs + B
    ok = rhs >= 0
    ys = np.sqrt(rhs[ok])
    ax_r.plot(xs[ok], ys, color="C0", lw=2)
    ax_r.plot(xs[ok], -ys, color="C0", lw=2)
    ax_r.axhline(0, color="gray", lw=0.8)
    ax_r.axvline(0, color="gray", lw=0.8)
    ax_r.set_title(r"over $\mathbb{R}$:  $y^2 = x^3 + 2x + 2$")
    ax_r.set_xlabel("x")
    ax_r.set_ylabel("y")
    ax_r.set_xlim(-1.5, 4)
    ax_r.set_ylim(-8.5, 8.5)
    ax_r.grid(alpha=0.3)

    # Right: the 18 affine points over GF(17), each labelled kP
    ax_p.axhline(MOD / 2, color="gray", ls="--", lw=1)
    ax_p.text(16.6, MOD / 2 + 0.15, "y = 8.5\n(kP ↔ (19−k)P)", ha="right",
              va="bottom", fontsize=8, color="gray")
    for k, (x, y) in enumerate(pts, start=1):
        special = k in (1, 18)
        ax_p.scatter(x, y, s=70 if special else 45, zorder=3,
                     color="C3" if special else "C0")
        label = "P" if k == 1 else ("18P = −P" if k == 18 else f"{k}P")
        ax_p.annotate(label, (x, y), xytext=(5, 5), textcoords="offset points",
                      fontsize=9, color="C3" if special else "black",
                      fontweight="bold" if special else "normal")
    ax_p.set_title(r"over GF(17):  $y^2 \equiv x^3 + 2x + 2$  (mod 17)"
                   "\n18 points + $\\mathcal{O}$ (= 19P, no coordinates)")
    ax_p.set_xlabel("x")
    ax_p.set_ylabel("y")
    ax_p.set_xticks(range(MOD))
    ax_p.set_yticks(range(MOD))
    ax_p.set_xlim(-0.7, 17.3)
    ax_p.set_ylim(-0.7, 17.3)
    ax_p.set_aspect("equal")
    ax_p.grid(alpha=0.3)

    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=150)
    print(f"saved {out}")


if __name__ == "__main__":
    points = multiples(GEN)
    check(points)
    plot(points, Path(__file__).resolve().parent.parent / "images"
         / "lecture17_curve_mod17.png")
