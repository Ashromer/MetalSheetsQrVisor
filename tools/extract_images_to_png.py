import os
import io
import sys
import hashlib
from PIL import Image

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF no está instalado.")
    print("Por favor, instala las dependencias ejecutando: pip install PyMuPDF Pillow")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow no está instalado.")
    print("Por favor, instala las dependencias ejecutando: pip install PyMuPDF Pillow")
    sys.exit(1)

def extract_pdf_images(pdf_path, output_dir="extracted_images_png", min_size=100, deduplicate=True):
    """
    Extrae todas las imágenes de un archivo PDF y las guarda en formato PNG.
    
    Args:
        pdf_path (str): Ruta al archivo PDF.
        output_dir (str): Directorio donde se guardarán las imágenes.
        min_size (int): Tamaño mínimo en píxeles (ancho o alto) para extraer (evita extraer iconos pequeños).
        deduplicate (bool): Si es True, no guarda imágenes que tengan el mismo hash MD5 (duplicados).
    """
    if not os.path.exists(pdf_path):
        print(f"Error: El archivo PDF '{pdf_path}' no existe.")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error al abrir el PDF: {e}")
        return

    print(f"Abierto: '{pdf_path}' ({len(doc)} páginas)")
    print(f"Guardando imágenes en la carpeta: '{output_dir}'")
    
    seen_hashes = set()
    total_extracted = 0
    total_saved = 0
    total_duplicates = 0
    total_skipped_small = 0

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        page_num = page_idx + 1
        image_list = page.get_images(full=True)
        
        if not image_list:
            continue
            
        print(f"Procesando página {page_num}/{len(doc)}: {len(image_list)} imágenes encontradas...")
        
        for img_idx, img_info in enumerate(image_list, start=1):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
            except Exception:
                continue
                
            image_bytes = base_image["image"]
            
            # Cargar imagen en Pillow
            try:
                img = Image.open(io.BytesIO(image_bytes))
            except Exception as e:
                print(f"  [!] No se pudo decodificar la imagen en xref {xref}: {e}")
                continue
                
            w, h = img.size
            
            # Filtrar por tamaño mínimo
            if w < min_size or h < min_size:
                total_skipped_small += 1
                continue
                
            total_extracted += 1
            
            # Deduplicación por hash MD5 del contenido de la imagen
            if deduplicate:
                img_hash = hashlib.md5(image_bytes).hexdigest()
                if img_hash in seen_hashes:
                    total_duplicates += 1
                    continue
                seen_hashes.add(img_hash)
            
            # Formatear nombre de archivo
            # Pág + índice de imagen en la página
            out_filename = f"pag_{page_num:03d}_img_{img_idx:02d}.png"
            out_path = os.path.join(output_dir, out_filename)
            
            try:
                # Conversión de modos de color para evitar problemas de compatibilidad con PNG en PIL
                if img.mode in ("CMYK", "YCbCr"):
                    img = img.convert("RGB")
                elif img.mode == "P":  # Palette mode
                    if "transparency" in img.info:
                        img = img.convert("RGBA")
                    else:
                        img = img.convert("RGB")
                
                img.save(out_path, format="PNG")
                total_saved += 1
                print(f"  [+] Guardada: {out_filename} ({w}x{h} px)")
            except Exception as e:
                print(f"  [!] Error al guardar {out_filename}: {e}")

    print("\n" + "="*50)
    print("Resumen de Extracción:")
    print(f"  Total imágenes en PDF (>= {min_size}px de dimensión): {total_extracted}")
    print(f"  Imágenes únicas guardadas en formato PNG: {total_saved}")
    if deduplicate:
        print(f"  Imágenes duplicadas omitidas (ej. logos repetidos): {total_duplicates}")
    print(f"  Imágenes muy pequeñas (< {min_size}px) omitidas: {total_skipped_small}")
    print(f"  Carpeta de salida: {os.path.abspath(output_dir)}")
    print("="*50)

if __name__ == "__main__":
    pdf_file = "Catalogo_Metalperfil.pdf"
    
    # Permitir pasar el archivo PDF como primer argumento
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]
        
    output_folder = "img_png"
    # Permitir pasar la carpeta de salida como segundo argumento
    if len(sys.argv) > 2:
        output_folder = sys.argv[2]
        
    extract_pdf_images(pdf_file, output_folder)
