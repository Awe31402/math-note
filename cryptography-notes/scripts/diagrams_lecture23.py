"""Diagrams for lecture23_note.md.  Run: python3 scripts/diagrams_lecture23.py"""

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN, GREEN_EDGE, RED, Fig, protocol

protocol("lecture23_signature_protocol", ["Alice", "Bob"], [
    ("Alice", "$k_{pr}$（私鑰）、$k_{pub}$（公鑰）"),
    ("msg", "Alice", "Bob", "$k_{pub}$"),
    ("Alice", "$s = sig(k_{pr}, m)$"),
    ("msg", "Alice", "Bob", "(m, s)"),
    ("Bob", "$ver(k_{pub}, m, s)$ = true / false"),
], col_w=6.0)

protocol("lecture23_lamport_one_bit", ["Alice", "Bob"], [
    ("Alice", "r（隨機）\nP = f(r)"),
    ("msg", "Alice", "Bob", "P"),
    ("Alice", "s = r"),
    ("msg", "Alice", "Bob", "(m, r)"),
    ("Bob", "f(r) =? P"),
])


def hash_chain(name, nodes, marks, w=1.7):
    """nodes: labels along the chain; marks: index -> (text, colour)."""
    n = len(nodes)
    f = Fig(n * w + 1.0, 2.6)
    xs = [1.0 + i * w for i in range(n)]
    for i, (x, s) in enumerate(zip(xs, nodes)):
        if i in marks:
            c = marks[i][1]
            fc = {RED: "#fbeaea", GREEN_EDGE: GREEN, ALT_EDGE: ALT}.get(c, BOX)
            f.box(x, 1.7, s, w=w - 0.5, h=0.65, fc=fc, ec=c)
            f.text(x, 0.75, marks[i][0], color=c, size=10)
            f.arrow((x, 1.0), (x, 1.35), color=c)
        else:
            f.text(x, 1.7, s)
        if i:
            f.arrow((xs[i - 1] + (w - 0.5) / 2 if i - 1 in marks else xs[i - 1] + 0.45, 1.7),
                    (x - (w - 0.5) / 2 if i in marks else x - 0.45, 1.7), label="f", loff=0.08)
    return f.save(name)


hash_chain("lecture23_wots_chain_example",
           ["r", "f(r)", "$f^2(r)$", "$f^3(r)$", "$f^4(r)$", "$f^5(r)$", "$f^6(r)$", "$f^7(r)$"],
           {0: ("私鑰", RED), 5: ("簽章（m = 5）", ALT_EDGE), 7: ("公鑰", GREEN_EDGE)})

protocol("lecture23_wots_attack_setup", ["Alice", "Oscar", "Bob"], [
    ("Alice", "$k_{pr}$ = r\n$k_{pub} = P = f^7(r)$"),
    ("msg", "Alice", "Bob", "$k_{pub}$"),
    ("Alice", "m = 5\n$s = f^5(r)$"),
    ("msg", "Alice", "Oscar", "(m, s)", "（放左邊，等一下要攻擊）"),
    ("Bob", "$v = f^{7-m}(s) = f^2(s)$\nv =? P"),
], widths=[5.0, 5.0, 5.0])

hash_chain("lecture23_wots_chain_general",
           ["r", "f(r)", "…", "$f^m(r)$", "…", "$f^{2^w-1}(r)$"],
           {0: ("私鑰", RED), 3: ("簽章 s", ALT_EDGE), 5: ("公鑰 P", GREEN_EDGE)}, w=2.1)
