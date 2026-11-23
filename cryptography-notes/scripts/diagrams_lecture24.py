"""Diagrams for lecture24_note.md.  Run: python3 scripts/diagrams_lecture24.py"""

from diagram_lib import _vislen, ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN, GREEN_EDGE, RED, Fig

# MSS = many WOTS key pairs, one public key
f = Fig(13, 4.4)
f.frame(0.4, 0.4, 7.6, 3.9, "MSS", ec=BOX_EDGE, ls="-")
for i, s in enumerate(["$(k_{pr,0}, k_{pub,0})$", "$(k_{pr,1}, k_{pub,1})$", "⋮",
                       "$(k_{pr,2^T-1}, k_{pub,2^T-1})$"]):
    f.text(2.6, 3.3 - i * 0.75, s)
f.text(6.2, 2.15, "$2^T$ 組\nWOTS 金鑰對", color=GRAY, size=10)
f.arrow((7.9, 2.15), (9.6, 2.15))
f.box(11.0, 2.15, "一把 $K_{pub}$", w=2.4, fc=GREEN, ec=GREEN_EDGE)
f.save("lecture24_mss_overview")


def merkle(name, levels, W, path=None, own=None, labels=None, top_note=None,
           leaves_extra=(), h=None, simple=False):
    """levels: list from root to leaves, each a list of node labels.
    path / own: sets of labels drawn as auth-path (sent) / self-computed."""
    path = path or set()
    own = own or set()
    nlev = len(levels) + len(leaves_extra)
    H = h or nlev * 1.25 + 0.6
    f = Fig(W, H)
    x0 = 2.8 if labels else 0.6
    span = W - x0 - 0.4
    pos = {}
    for li, row in enumerate(levels):
        y = H - 0.6 - li * 1.25
        n_full = 2 ** li
        for i, s in enumerate(row):
            if s is None:
                continue
            x = x0 + span * (i + 0.5) / n_full
            pos[(li, i)] = (x, y)
            bw = max(0.9, 0.2 * _vislen(s) + 0.5)
            if s in path:
                f.box(x, y, s, w=bw, h=0.6, fc=ALT, ec=ALT_EDGE)
            elif s in own:
                f.box(x, y, s, w=bw, h=0.6, fc=BOX, ec=BOX_EDGE, round_=False)
            elif simple:
                f.text(x, y, s)
            else:
                f.box(x, y, s, w=bw, h=0.6, fc="white", ec="#777777")
            if li and (li - 1, i // 2) in pos and not simple:
                px, py = pos[(li - 1, i // 2)]
                f.line((x, y + 0.3), (x, (y + py) / 2), (px, (y + py) / 2), (px, py - 0.3), color="#555555", lw=1.1)
        if labels:
            f.text(0.3, y, labels[li], ha="left", size=10, color=GRAY)
    last = len(levels) - 1
    for k, (row, lab) in enumerate(leaves_extra):
        y = H - 0.6 - (last + 1 + k) * 1.25
        for i, s in enumerate(row):
            if s is None:
                continue
            x = x0 + span * (i + 0.5) / 2 ** last
            if (last, i) in pos and k == 0 and not simple:
                f.arrow((x, y + 0.25), (x, pos[(last, i)][1] - 0.3), color="#555555", lw=1.0)
            f.text(x, y, s)
        if lab:
            f.text(0.3, y, lab, ha="left", size=10, color=GRAY)
    return f, pos


# Two leaves
f, pos = merkle("lecture24_merkle_two", [["$K_{pub} = H(A_0 \\| A_1)$"], ["$A_0$", "$A_1$"]], 9,
                leaves_extra=[(["$Y_0$", "$Y_1$"], None), (["$X_0$", "$X_1$"], None)])
f.text(7.9, 2.5, "← WOTS 公鑰", ha="left", size=10, color=GRAY)
f.text(7.9, 1.25, "← WOTS 私鑰", ha="left", size=10, color=GRAY)
f.text(pos[(1, 0)][0] - 0.2, 3.1, "$A_0 = H(Y_0)$", ha="right", size=9, color=GRAY)
f.text(pos[(1, 1)][0] + 0.2, 3.1, "$A_1 = H(Y_1)$", ha="left", size=9, color=GRAY)
f.save("lecture24_merkle_two")

levels = [["D"], ["$C_0$", "$C_1$"], [f"$B_{i}$" for i in range(4)], [f"$A_{i}$" for i in range(8)]]
f, pos = merkle("lecture24_merkle_full", levels, 15,
              labels=["level 3（根）", "level 2", "level 1", "level 0（葉）", ""],
              leaves_extra=[([f"$Y_{i}$" for i in range(8)], "WOTS 公鑰"),
                            ([f"$X_{i}$" for i in range(8)], "WOTS 私鑰")])
f.text(pos[(0, 0)][0] + 0.6, pos[(0, 0)][1], "= $K_{pub}$", ha="left", color=GREEN_EDGE)
f.save("lecture24_merkle_full")

# Authentication path for leaf 3
lv = [["D ✔"], ["$C_0$", "$C_1$"], ["$B_0$", "$B_1$", None, None],
      [None, None, "$A_2$", "$A_3$", None, None, None, None]]
f, pos = merkle("lecture24_auth_path", lv, 15,
                path={"$C_1$", "$B_0$", "$A_2$"}, own={"D ✔", "$C_0$", "$B_1$", "$A_3$"},
                labels=["level 3", "level 2", "level 1", "level 0", ""],
                leaves_extra=[([None, None, None, "$Y_3$", None, None, None, None], "")])
x, y = pos[(0, 0)]
f.text(x + 0.7, y, "（比對 $K_{pub}$）", ha="left", size=10, color=GREEN_EDGE)
yy = 1.25
f.text(pos[(3, 3)][0] + 0.4, yy, "← 送", ha="left", size=10, color=ALT_EDGE)
f.box(11.0, 0.6, "", w=0.5, h=0.35, fc=ALT, ec=ALT_EDGE)
f.text(11.4, 0.6, "= 認證路徑（Alice 送的）", ha="left", size=10)
f.box(11.0, 1.2, "", w=0.5, h=0.35, fc=BOX, ec=BOX_EDGE, round_=False)
f.text(11.4, 1.2, "= Bob 自己算的", ha="left", size=10)
f.save("lecture24_auth_path")

# Bare tree (for the index arithmetic)
levels = [["D"], ["$C_0$", "$C_1$"], [f"$B_{i}$" for i in range(4)], [f"$A_{i}$" for i in range(8)]]
f, _ = merkle("lecture24_tree_simple", levels, 11,
              leaves_extra=[([f"$Y_{i}$" for i in range(8)], None)])
f.save("lecture24_tree_simple")
