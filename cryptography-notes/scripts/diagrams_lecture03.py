"""Diagrams for lecture03_note.md.  Run: python3 scripts/diagrams_lecture03.py"""

from diagram_lib import ALT, ALT_EDGE, Fig, tree

tree("lecture03_symmetric_tree",
     ("Symmetric Ciphers\n（對稱式密碼）", [
         "Stream Ciphers\n（串流密碼）",
         "Block Ciphers\n（區塊密碼）"]),
     leaf_w=4.2,
     notes={"Stream Ciphers\n（串流密碼）": "← 今天開始，約 2 週",
            "Block Ciphers\n（區塊密碼）": "之後約 4 週（DES、AES）"})

# Stream cipher encryption / decryption with key-stream generators
f = Fig(15, 5.2)
for gx in (4.0, 11.0):
    f.text(gx, 4.8, "金鑰 k")
    f.arrow((gx, 4.55), (gx, 3.85))
    f.box(gx, 3.45, "產生器", w=1.8, fc=ALT, ec=ALT_EDGE)
f.op(5.5, 1.0)
f.op(9.5, 1.0)
f.arrow((4.9, 3.45), (5.5, 3.45), (5.5, 1.22), label="$s_i$", lpos=0.4)
f.arrow((10.1, 3.45), (9.5, 3.45), (9.5, 1.22), label="$s_i$", lpos=0.4, lside="left")
f.text(0.6, 1.0, "$x_i$")
f.arrow((0.9, 1.0), (5.28, 1.0))
f.arrow((5.72, 1.0), (9.28, 1.0), label="$y_i$　（通道）")
f.arrow((9.72, 1.0), (13.8, 1.0))
f.text(14.2, 1.0, "$x_i$")
f.text(3.0, 0.3, "加密", size=10, color="#888888")
f.text(12.0, 0.3, "解密", size=10, color="#888888")
f.save("lecture03_stream_cipher")
