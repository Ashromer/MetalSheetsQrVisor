"""
extract_pdf.py — Extrae renders y texto de Catalogo_Metalperfil.pdf.

Uso (desde la raíz del repo, con Python 3 + PyMuPDF y Pillow instalados):
    pip install PyMuPDF Pillow
    python tools/extract_pdf.py

Genera:
    img/pNN_i.<ext>     imágenes únicas (>=400 px), nombradas por página PDF + índice.
    img/_manifest.json  inventario (página, archivo, tamaño; y reutilizaciones deduplicadas).
    img/_texto.txt      volcado de texto de todas las páginas (UTF-8).

El PDF son 46 hojas = pliegos de 2 páginas impresas. Solo la familia Pyramid
trae contenido real; el resto del PDF es maqueta provisional (lorem ipsum).
Las imágenes (renders) sí son reales y de alta resolución.
"""
import fitz, os, hashlib, json

PDF = "Catalogo_Metalperfil.pdf"
MIN_PX = 400  # descarta iconos/decoración pequeña

def main():
    doc = fitz.open(PDF)
    os.makedirs("img", exist_ok=True)
    seen, manifest, texto = {}, [], []

    for i, page in enumerate(doc):
        pno = i + 1
        texto.append(f"\n===== PDF PAG {pno} =====\n{page.get_text()}")
        idx = 0
        for img in page.get_images(full=True):
            try:
                d = doc.extract_image(img[0])
            except Exception:
                continue
            w, h = d["width"], d["height"]
            if max(w, h) < MIN_PX:
                continue
            data = d["image"]
            hsh = hashlib.md5(data).hexdigest()
            if hsh in seen:
                manifest.append({"page": pno, "reuse_of": seen[hsh], "w": w, "h": h})
                continue
            idx += 1
            name = f"p{pno:02d}_{idx}.{d['ext']}"
            with open(os.path.join("img", name), "wb") as f:
                f.write(data)
            seen[hsh] = name
            manifest.append({"page": pno, "file": name, "w": w, "h": h, "ext": d["ext"]})

    json.dump(manifest, open("img/_manifest.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open("img/_texto.txt", "w", encoding="utf-8").write("\n".join(texto))
    uniq = [m for m in manifest if "file" in m]
    print(f"OK — {len(uniq)} imágenes únicas, {len(manifest)-len(uniq)} reutilizadas (dedup).")

if __name__ == "__main__":
    main()
