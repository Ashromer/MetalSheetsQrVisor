@echo off
title Metalperfil - Extractor de Catalogo PDF
echo Instalando dependencias necesarias (PyMuPDF, Pillow)...
pip install PyMuPDF Pillow
echo.
echo Ejecutando extraccion de renders y texto desde Catalogo_Metalperfil.pdf...
python tools/extract_pdf.py
echo.
echo Proceso finalizado. Las imagenes se han guardado en la carpeta 'img/'
pause
