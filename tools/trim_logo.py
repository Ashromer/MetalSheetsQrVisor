"""
trim_logo.py — Recorta el margen transparente del logo.

El original Metalperfil_white.png mide 3508x2479 px pero el logotipo real ocupa
solo ~23% x 17% del lienzo (el resto es transparente), por lo que en la web se veía
minúsculo. Este script recorta a la caja del contenido (alfa) + un pequeño margen.

Uso:
    pip install Pillow
    python tools/trim_logo.py
Genera Metalperfil_white_trim.png (el que usan index.html y catalogo.html).
"""
from PIL import Image

PAD = 12
im = Image.open("Metalperfil_white.png").convert("RGBA")
bbox = im.split()[3].getbbox()
crop = (max(0, bbox[0]-PAD), max(0, bbox[1]-PAD),
        min(im.size[0], bbox[2]+PAD), min(im.size[1], bbox[3]+PAD))
out = im.crop(crop)
out.save("Metalperfil_white_trim.png")
print("OK ->", out.size)
