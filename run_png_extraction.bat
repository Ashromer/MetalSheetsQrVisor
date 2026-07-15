@echo off
title Metalperfil - Extractor de Imagenes a PNG
echo Instalando dependencias necesarias (PyMuPDF, Pillow)...
pip install PyMuPDF Pillow
echo.
echo Ejecutando extraccion de imagenes en PNG desde Catalogo_Metalperfil.pdf...
python tools/extract_images_to_png.py Catalogo_Metalperfil.pdf img_png
echo.
echo Proceso finalizado. Las imagenes se han guardado en la carpeta 'img_png/'
pause
