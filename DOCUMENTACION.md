# Metalperfil — Visor 3D + Catálogo web · Documentación

Web estática (HTML/CSS/JS, sin framework ni build) alojada en **GitHub Pages**.
Repo `Ashromer/MetalSheetsQrVisor`, rama `main`.

- **Visor 3D:** https://ashromer.github.io/MetalSheetsQrVisor/ (`index.html`)
- **Catálogo:** https://ashromer.github.io/MetalSheetsQrVisor/catalogo.html

---

## 1. Stack y convenciones

- HTML/CSS/JS plano. Modelos 3D con `<model-viewer>` (CDN jsDelivr).
- **Tipografías**
  - Catálogo: **Cormorant Garamond** (títulos / texto elegante) + **Montserrat** (datos técnicos, nav, etiquetas).
  - Visor: Playfair Display + Inter (+ Cormorant Garamond para el titular de la banda roja).
- **Color de marca:** rojo `rgb(158, 39, 44)` / `#9E272C` (el real de la portada del PDF).
  `--red` en `catalogo.html`, `--brand-red-granate` en `index.html`.
- Estilo: editorial, minimalista, mucho aire. Cada sección del catálogo ocupa como mínimo
  el alto del monitor (`.screen`).

---

## 2. Estructura del repo

```
index.html          Visor 3D interactivo
catalogo.html       Catálogo (una página, scroll largo, data-driven)
DOCUMENTACION.md    Este archivo
CLAUDE.md.txt       Notas internas para asistentes de IA
Catalogo_Metalperfil.pdf   PDF original (fuente)
models/             Todos los .glb  (Familia_Tipo.glb)
assets/             Logos (Metalperfil_white.png y _trim.png)
img/                Imágenes que SÍ se sirven en la web (renders, desarrollos…)
tools/              Scripts Python reproducibles (extracción PDF, recorte logo)
source/             Material fuente NO servido (planos, PDFs); lo pesado está en .gitignore
```

Rutas **sensibles a mayúsculas/minúsculas** (GitHub Pages es case-sensitive).

---

## 3. Visor 3D (`index.html`)

Selector de **familia** (desplegable) + **tipo** (botones) + **color** (muestras) sobre un
`<model-viewer>`. Todo se genera desde el objeto `catalog`:

```js
Familia: { label, prefix, types, anchor }
```
- `label`: nombre visible (puede diferir del archivo, p.ej. archivo `Symetric_` ↔ label `Symmetric`).
- `prefix`: ruta+prefijo EXACTO del .glb (`models/Pyramid_`).
- `types`: sufijos de archivo; string, o `{label, file}` cuando el nombre visible difiere
  (Kubo: `{label:'17·17·17', file:'171717'}`).
- `anchor`: sección del catálogo a la que enlaza el botón "Catálogo".

Familias en el visor (10, las que tienen .glb): Pyramid, Symmetric, Asymmetric, Escaler,
Kaotico, Origami, AcerOnda, Kubo, Nordik, Ritmiko.

**Claves a NO romper** (costó hacerlas funcionar):
- CDN jsDelivr de `@google/model-viewer` (no googleapis).
- El evento `load` solo oculta el spinner y aplica color; **nada de mover la cámara ahí**
  (cuelga con "rAF timed out").
- `.viewer-container` necesita **altura fija en vh** (`height`), **nunca `flex`** → con flex
  el visor queda a 0px y desaparece. (`bottom-panel` sí es `flex:0 0 auto` para no dejar
  hueco negro; el `body` es negro para que un posible sobrante combine.)
- Órbita: `min/max-camera-orbit` abiertos (`auto 0deg/180deg`) para girar 360° y ver todos
  los lados; `disable-pan` mantiene el giro centrado en la pieza.
- Nombres de .glb con espacio (`Nordik_24 A.glb`): el `src` pasa por `encodeURI()`.

---

## 4. Catálogo (`catalogo.html`)

Una sola página. **Todo el contenido por familia vive en el array `FAMILIES`** del `<script>`
final; el resto de secciones son HTML directo. Orden de la página:

1. **Portada** roja a pantalla completa (`img/p01_1.jpeg`) con el titular abajo-izquierda.
2. **Sistemas y productos** (contenido de la pág. 2 del catálogo): fijación vista/oculta + gama.
3. **La colección** (texto + foto de proceso).
4. **Índice** — dos líneas de tiempo (fijación vista / oculta).
5. **Origen / Quiénes somos**, **Trajes a medida**.
6. **Familias** (render dinámico de `FAMILIES`).
7. **Materialidad (Acabados)**, **BIM**, **Contacto**, footer.

### 4.1 Índice (líneas de tiempo)
Calcado al catálogo (pág. 04-05). Arrays implícitos `FAMILIES.slice(0,6)` (vista) y
`.slice(6)` (oculta). Cada entrada = **mini-render (B/N → color al hover)** + **número +
nombre** + **tramo de perfil con la forma real** (SVG, mapa `PROFILES`). Las familias sin
perfil trazado usan el genérico `SEG_GEN` (clase `.gen`, línea discontinua). `buildTimeline()`.

### 4.2 Esquema de una familia en `FAMILIES`
```js
{
  num, name, anchor, pages, status,        // status: 'real' | 'partial' | 'placeholder'
  desc,                                     // descripción (justificada)
  config: { 'Longitud mínima': '…', … },    // Propiedades técnicas
  materials: MAT,                           // chips
  thumb, heroRender,                        // heroRender = pieza (no edificio), sin recortar
  desarrollo,                               // img de perfiles con cotas (entre intro y dims)
  types: [{ lab, ancho, altura, angulo, img }],  // tabla Dimensiones (+ siluetas si no hay desarrollo)
  model: { prefix, types },                 // visor 3D con selector de tipo + paleta RAL
  renders: ['img/…'],                       // renders editoriales salteados con texto inspiracional
  warn                                      // aviso amarillo (datos a verificar)
}
```
Orden de bloques por familia: cabecera `NN. Nombre` (rojo) + descripción + render de la pieza
→ **Desarrollos** → Propiedades técnicas → Materiales → **Dimensiones** → **Visor 3D + RAL**
→ **Acabados / renders**.

Para **completar una familia**: rellenar los campos y poner `status:'real'`.

### 4.3 Visor 3D por familia + RAL
`viewerBlock()` genera un `<model-viewer>` con botones de tipo y muestras **RAL** (array `RAL`).
`initViewers()` los cablea (carga de modelo y recoloreado con `setBaseColorFactor`).

### 4.4 Secciones de contenido PROPUESTO (a confirmar con la empresa)
Marcadas en la web con `.note` "Propuesta":
- **Acabados/Materialidad**: soportes (galvanizado/Aluzinc, prelacado, inoxidable, corten,
  aluminio/zinc/cobre), carta RAL, efectos (mate, satinado, metalizado, madera, óxido,
  texturado, arenado, anodizado, PVDF), perforado. Basado en práctica del sector.
- **BIM**: familias paramétricas Revit/.rfa, IFC, datos integrados, LOD 200-350, descargas.

---

## 5. Estado del contenido por familia

| # | Familia | Estado | 3D (.glb) | Notas |
|---|---|---|---|---|
| 01 | Pyramid | **real** | sí | config + dimensiones + desarrollos + renders |
| 02 | Symmetric | **real** | sí | tipos 23/25/29/40 con ángulos; falta `config` |
| 03 | Asymmetric | parcial | sí | nombres de tipo reales; ancho útil y descripción pendientes |
| 04 | Escaler | placeholder | sí | — |
| 05 | Kaotico | placeholder | sí | — |
| 06 | Origami | placeholder | sí | — |
| 07 | Onda | placeholder | sí (`AcerOnda_`) | — |
| 08 | Kubo | placeholder | sí | tipos 17·17·17… |
| 09 | Nordik | placeholder | sí | tipos 24 A/B/C |
| 10 | Alterno | placeholder | no | sin .glb |
| 11 | Skala | placeholder | no | sin .glb |

Extra solo en el visor: **Ritmiko** (tiene .glb, sin sección de catálogo aún → ancla `indice`).

**Pyramid — datos a verificar:** altura de P45 (15 mm) y ancho de P68 (893/793 mm) se
contradicen en el PDF; asignación perfil↔tipo provisional.

Inconsistencias de nombre archivo↔comercial: `Symetric/Asymetric/Kaotiko` (.glb) vs
Symmetric/Asymmetric/Kaotico (catálogo); `AcerOnda` ↔ Onda.

---

## 6. Imágenes y assets

- `img/pNN_i.jpeg|png` — extraídos del PDF (página NN, índice i). Ver `img/_manifest.json`.
- `img/desarrollo_{pyramid,symmetric,asymmetric}.png` — perfiles con cotas recortados de
  `source/paginas/` (págs. 07/10/13).
- `assets/Metalperfil_white_trim.png` — logo recortado (el original tenía ~77% de margen
  transparente y se veía minúsculo). **Es el que usan los HTML.**
- `models/` — 37 `.glb` (`Familia_Tipo.glb`).
- `source/` — material fuente NO servido: planos PDF, y `paginas/` (46 PNG del catálogo) +
  `MIGUEL-1.pdf`, ambos en `.gitignore` por peso (~68 MB / 26 MB).

> El PDF original es en gran parte una **maqueta** (lorem ipsum); solo Pyramid y Symmetric
> traen datos reales. Los **renders** del PDF sí son reales y de alta resolución.

---

## 7. Herramientas (`tools/`)

Requiere Python 3 + `pip install PyMuPDF Pillow`. Desde la raíz del repo:

- `python tools/extract_pdf.py` → re-extrae imágenes (≥400 px, deduplicadas) a `img/` +
  `img/_manifest.json` + `img/_texto.txt`. Ejecutar cada vez que el cliente sube un PDF nuevo.
- `python tools/trim_logo.py` → regenera `assets/Metalperfil_white_trim.png`.

---

## 8. Flujo de trabajo (git / despliegue)

- No hay `git` en el PATH del equipo; se usa el de **GitHub Desktop**
  (`%LOCALAPPDATA%\GitHubDesktop\app-<ver>\resources\app\git\cmd\git.exe`).
- `commit` + `push` a `main`; GitHub Pages redespliega solo en 1-2 min.
- No subir a `img/` archivos pesados que no se usen en la web (van a `source/` + `.gitignore`).
  Ojo: en `.gitignore` **no** poner comentarios en la misma línea que el patrón.

---

## 9. Tareas pendientes

1. Rellenar las familias **placeholder** (textos, dimensiones, tipos, renders) según el
   cliente complete el PDF → volcar a `FAMILIES` y poner `status:'real'`.
2. **Índice — perfiles por pieza:** el cliente dará **PNG recortados del perfil de cada
   familia**; sustituir entonces los `PROFILES` (SVG) por imágenes. Hoy solo Pyramid y
   Symmetric llevan SVG trazado; Asymmetric y el resto usan el genérico (`.gen`).
3. **"Tipos"** (antes "Desarrollos"): la imagen actual está recortada del PDF; el cliente
   dará versión en **alta resolución** → sustituir `desarrollo_*.png`.
4. **Acabados:** las "burbujas" de material son gradientes CSS de muestra; valorar fotos
   reales de cada acabado. Confirmar gama real (corten, perforados, efectos…) con la empresa.
5. Confirmar/ajustar contenido **propuesto** de Acabados y **BIM**.
6. **Datos de contacto** reales (footer y sección Contacto).
7. Verificar dimensiones de Pyramid (P45 / P68).
8. (Opcional) Limpiar del historial de git los 68 MB de PNGs colados en `1fb22be`
   (reescritura + `push --force`).

### Estado de hoy (última sesión)
Hechos: índice con líneas de tiempo (mini-render B/N→color + perfil SVG), título "Índice"
grande sin etiquetas vista/oculta; portada con titular arriba; sección "Sistemas y productos"
(pág. 2) con imágenes; bloque "Tipos" por familia; "Proyectos de referencia" (antes "Acabados")
en cada familia; Materialidad con burbujas + tira de muro; BIM con imágenes/texto intercalados.
Esperando del cliente: PNG de perfiles por familia, imágenes de "Tipos" en alta resolución,
y confirmación de Acabados/BIM.

### Actualización 2026-06-19 (sesión Claude)
**Fuente única de datos:** `02_PROYECTO/_PERFILES_MASTER/` (fuera del repo). El DXF
`01_REFERENCIAS/planos_cad/PERFILES ARQUITECTÓNICOS DE FACHADA.dxf` es el origen; de ahí salen
medidas y perfiles. Ver su `README.md`.

- **Catálogo a 11 familias** (Pyramid, Symmetric, Asymmetric, Escaler, Kaotico, Origami, Onda,
  Kubo, Nordik, Alterno, Skala). Aqqua/Cubik/Triangle = grupo "Singular"/oculta, **no salen**.
  Mapeo nombre: AcerOnda=Onda, Symetric=Symmetric, Asymetric=Asymmetric, Kaotiko=Kaotico.
- **Medidas reales del DXF** en todas las familias (resuelven contradicciones del PDF: Pyramid
  P45 altura ≈47, "Pyramid 33"→39). Skala sin geometría (capa DXF mal puesta); Nordik 50A idem.
- **Índice — perfiles SVG ahora REALES**, generados del DXF con
  `_PERFILES_MASTER/make_profiles_svg.py` (un módulo por familia, altura relativa real, ancho
  completo = continuos). Pegar el output en el objeto `PROFILES` de catalogo.html. Alterno/Skala
  reutilizan el perfil e imagen de Nordik como placeholder (`PROFILES.alterno = PROFILES.skala = PROFILES.nordik`).
- **Miniaturas del índice** = recortes `img/0X_Familia_cut.png` (autorecortados al contenido,
  transparentes, `aspect-ratio:2.9/1`, `overflow:visible` para que el hover-zoom no recorte).
- **Fichas "Tipos y dimensiones"** (`typeCards()`): render por tipo (3/4, `contain`, entero) +
  Ancho/Alto/Ángulo. Sustituye la antigua tabla de dimensiones.
- **Descripciones por familia en cursiva** (`.fam-desc`), redactadas por Claude.
- **Acabados/Perforado**: patrón CSS real de perforación (no foto).
- **BIM**: añadido apartado "Tecnología aplicada · visor online e interactividad".
- **Favicon**: `assets/Metalperfil_red.png` (logo granate) en catalogo.html e index.html.
- **Git**: el clon perdió el `.git` y se reconectó por terminal (remoto `Ashromer/MetalSheetsQrVisor`).
  `.gitignore` debe ignorar `source/paginas/` y `source/*.pdf` (si no, se cuelan ~90 MB).

**Pendiente:** perfil acotado de **Symmetric** (quitado; el recorte salía mal — rehacer desde la
página correcta del catálogo, como el de Asymmetric). Renders por tipo reales para las familias
sin imagen. Limpiar la captura `Captura_correccion.JPG` del repo.

### Actualización 2026-06-22 (sesión Claude)
**Norma del líder:** el **PDF/PNG del catálogo manda** como documento de referencia (revierte lo
del DXF como fuente única para la web). Se copia del PDF; se señalan sus errores pero gobierna él.

- **Nueva sección "Fijación oculta"** (`#oculta`, tras la gama): explica el sistema 02 (piel
  continua sin anclajes) con 4 tarjetas (Rollforming/Custom/Screenpanel/Lamas, dibujos SVG de
  marca) + **configurador interactivo** (`#ocComposer`/`#ocWall`) que recompone un paño según el
  sistema (anchos orientativos del diagrama de gama). Enlace nuevo en el nav. CSS/JS vanilla,
  `prefers-reduced-motion` respetado.
- **`img/` refrescado desde el PDF nuevo (46 pág.)**: borradas las 57 imágenes extraídas viejas
  y re-extraídas 66 con `tools/extract_pdf.py`. Desapareció `p14_3` → Asymmetric se queda con
  `p14_1`+`p14_2`. `gama_pag02.png` regenerada de la pág. 2 actual.
- **Desarrollos acotados rehechos del PDF (8)**: `desarrollo_{pyramid,symmetric,asymmetric,escaler,
  kaotico,kubo,nordik,onda}.png`, recortados de la 1ª hoja de cada familia (págs. PDF 7/10/13/16/
  19/28/31/25) con auto-trim. Origami/Alterno/Skala = spreads "PLACEHOLDER" → sin desarrollo real.
  Enlazados en `FAMILIES` (`desarrollo:`).
- **Aviso de coherencia:** las cifras del desarrollo (p.ej. "Pyramid 33 / ancho 894") vienen del
  PDF y aún difieren de la tabla `FAMILIES` (sacada del DXF: 39 / 882). Pendiente unificar la tabla
  al PDF si el líder lo confirma.
