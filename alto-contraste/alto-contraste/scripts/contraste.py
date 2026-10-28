#!/usr/bin/env python3
"""Comprueba contraste WCAG 2.2 (luminancia relativa, ratio truncado a 2 decimales).

Uso:
  python3 contraste.py "#FFFFFF" "#0A0D14"     # un par
  python3 contraste.py --paleta paleta.json    # pares estándar de una paleta
"""
import sys, json, math


def lum(hex_color):
    h = hex_color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Color no válido: {hex_color}")
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return math.floor((hi + 0.05) / (lo + 0.05) * 100) / 100


def nivel_texto(r, grande=False):
    aa, aaa = (3.0, 4.5) if grande else (4.5, 7.0)
    if r >= aaa:
        return "AAA"
    if r >= aa:
        return "AA"
    return "NO CUMPLE"


# (texto, fondo, tipo): "texto" = mínimo de texto; "no-texto" = mínimo 3:1 (WCAG 1.4.11)
PARES = [
    ("texto", "fondo", "texto"),
    ("texto_secundario", "fondo", "texto"),
    ("texto_sobre_acento", "acento", "texto"),
    ("error", "fondo", "texto"),
    ("acento", "fondo", "no-texto"),
    ("foco", "fondo", "no-texto"),
    ("borde", "fondo", "no-texto"),
]


def check_paleta(p):
    fallos = 0
    for a, b, tipo in PARES:
        if a not in p or b not in p:
            continue
        r = ratio(p[a], p[b])
        if tipo == "texto":
            n = nivel_texto(r)
            ok = n != "NO CUMPLE"
        else:
            ok = r >= 3.0
            n = "OK (3:1)" if ok else "NO CUMPLE"
        print(f"{a:20} {p[a]} sobre {b:8} {p[b]}  {r:>5}:1  {n}")
        fallos += 0 if ok else 1
    print("\nResultado:", "PALETA VÁLIDA" if fallos == 0 else f"{fallos} par(es) no cumplen")
    return fallos


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] != "--paleta":
        a, b = sys.argv[1], sys.argv[2]
        r = ratio(a, b)
        print(f"{a} sobre {b}: {r}:1")
        print(f"  texto normal: {nivel_texto(r)}   texto grande: {nivel_texto(r, grande=True)}")
        print(f"  no textual (iconos, bordes, foco): {'OK' if r >= 3 else 'NO CUMPLE'}")
    elif len(sys.argv) == 3 and sys.argv[1] == "--paleta":
        with open(sys.argv[2], encoding="utf-8") as f:
            sys.exit(1 if check_paleta(json.load(f)) else 0)
    else:
        print(__doc__)
        sys.exit(2)
