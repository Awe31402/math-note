"""Diagrams for lecture07_note.md.  Run: python3 scripts/diagrams_lecture07.py"""

from diagram_lib import blackbox

blackbox("lecture07_aes_blackbox", "128 bit 明文", "128 bit 密文", "AES",
         "金鑰", key_note="金鑰：128 / 192 / 256 bit")
