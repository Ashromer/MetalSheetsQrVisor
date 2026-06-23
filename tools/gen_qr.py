"""Genera un QR por familia que apunta al visor 3D con deep-link (?family=...).

Requisito: pip install "qrcode[pil]"
Salida: assets/qr/qr_<anchor>.png

Si cambia el dominio/ruta del visor, edita BASE_URL y vuelve a ejecutar:
    python tools/gen_qr.py
"""
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_M

BASE_URL = "https://ashromer.github.io/MetalSheetsQrVisor/index.html"

# anchor (clave de URL y nombre de archivo) -> nombre legible
FAMILIES = {
    "pyramid": "Pyramid",
    "symmetric": "Symmetric",
    "asymmetric": "Asymmetric",
    "escaler": "Escaler",
    "kaotico": "Kaotico",
}

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "qr"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for anchor, name in FAMILIES.items():
        url = f"{BASE_URL}?family={anchor}"
        qr = qrcode.QRCode(
            version=None,
            error_correction=ERROR_CORRECT_M,
            box_size=20,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1c1b1a", back_color="white")
        out = OUT_DIR / f"qr_{anchor}.png"
        img.save(out)
        print(f"{name:11s} -> {out.name}  ({url})")


if __name__ == "__main__":
    main()
