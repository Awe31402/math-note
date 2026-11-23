"""Diagrams for lecture14_note.md.  Run: python3 scripts/diagrams_lecture14.py"""

from diagram_lib import protocol, tree

tree("lecture14_course_map",
     ("密碼學", [
         "對稱式",
         ("非對稱式", ["RSA", "離散對數（DL）", "橢圓曲線（ECC）"]),
         "協定\n（數位簽章、雜湊……）"]),
     leaf_w=3.4, level_h=2.0,
     notes={"對稱式": "✔ 完成", "非對稱式": "← 現在在這裡（正中間）",
            "RSA": "✔", "離散對數（DL）": "← 進行到一半",
            "橢圓曲線（ECC）": "之後兩週", "協定\n（數位簽章、雜湊……）": "之後"})

protocol("lecture14_dh", ["Alice", "Bob"], [
    (("Alice", "選 a ∈ {2, …, p−2}\n$A = \\alpha^a$ mod p"),
     ("Bob", "選 b ∈ {2, …, p−2}\n$B = \\alpha^b$ mod p")),
    ("msg", "Alice", "Bob", "A"),
    ("msg", "Bob", "Alice", "B"),
    (("Alice", "$k_{AB} = B^a$ mod p"), ("Bob", "$k_{AB} = A^b$ mod p")),
])
