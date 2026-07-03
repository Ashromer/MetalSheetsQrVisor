# Metalperfil — Visor 3D + Catálogo web · Documentación

Web estática (HTML/CSS/JS, sin framework ni build) alojada en **GitHub Pages**.
Repo `Ashromer/MetalSheetsQrVisor`, rama `main`.

- **Visor 3D:** https://ashromer.github.io/MetalSheetsQrVisor/ (`index.html`)
- **Catálogo:** https://ashromer.github.io/MetalSheetsQrVisor/catalogo.html

> Actualizado 2026-07-03, sincronizado con el PDF **260701_Catalogo Metalperfil** (35 págs.).
> Narrativa **Sistema · Forma · Material · Acabado** (Origami™ / Flow™ / Uniko™), **5 familias**.
> El orden replica el catálogo: **Dos Sistemas va ANTES que las tres propuestas y las formas**.
> Los datos técnicos (anchos/alturas/nombres) siguen la **tabla maestra** `02_PROYECTO/_PERFILES_MASTER`,
> NO el PDF (el 260701 trae erratas: "Eskaler 54"/"Kaotico 72", medidas de Eskaler copiadas de Symmetric).

---

## 1. Stack y convenciones

- HTML/CSS/JS plano. Modelos 3D con `<model-viewer>` (CDN jsDelivr, **versión fijada `@4.0.0`**).
- **Tipografías** (las dos páginas): **Cormorant Garamond** (títulos / texto elegante) +
  **Montserrat** (datos técnicos, navegación, etiquetas). Cargadas de Google Fonts con `preconnect`.
- **Color de marca:** granate `rgb(122, 28, 40)`. Token `--red` en `catalogo.html`,
  `--brand-red-granate` en `index.html`. Acento bronce `--bronze: #9a6b3a`.
- Estilo: editorial, minimalista, mucho aire. Cada sección del catálogo ocupa al menos el alto
  del monitor (`.screen`). Glassmorphism con mesura (`backdrop-filter` solo en `.fam-product`).
- A11y / rendimiento: `prefers-reduced-motion` respetado en ambas páginas; `loading="lazy"` en
  imágenes; contenedores con `aspect-ratio` para evitar layout shift; skip-link en el catálogo.

---

## 2. Estructura del repo

```
index.html          Visor 3D interactivo (5 familias)
catalogo.html       Catálogo (una página, scroll largo, data-driven)
DOCUMENTACION.md    Este archivo
CLAUDE.md.txt       Notas internas para asistentes de IA
Catalogo_Metalperfil.pdf   PDF original (fuente) — se sirve para descarga
models/             Todos los .glb  (Familia_Tipo.glb)
img/                Imágenes servidas:
  img/propuesta/    renders editoriales y de familia, SVG de diagramas
  img/catalogo/     fotos de proceso Flow/Uniko, capturas de plugins BIM
  img/types/        render por tipo (type_<familia>_<medida>.jpg) — fichas y posters 3D
  img/NN_*_cut.png  recorte de producto (pieza suelta) por familia
assets/             Logos, favicon y QR (assets/qr/qr_<familia>.png)
source/             Material fuente NO servido (PDF, páginas); lo pesado en .gitignore
tools/              Scripts Python reproducibles (extracción PDF, recorte logo)
```

Rutas **sensibles a mayúsculas/minúsculas** (GitHub Pages es case-sensitive).

---

## 3. Visor 3D (`index.html`)

Selector de **familia** (desplegable) + **tipo** (botones) + **color** (muestras RAL) sobre un
`<model-viewer>`. Todo se genera desde el objeto `catalog`:

```js
Familia: { label, prefix, types, anchor }
```
- `label`: nombre visible (puede diferir del archivo, p.ej. archivo `Symetric_` ↔ label `Symmetric`).
- `prefix`: ruta+prefijo EXACTO del .glb (`models/Pyramid_`).
- `types`: sufijos de archivo (string), o `{label, file}` cuando el nombre visible difiere.
- `anchor`: sección del catálogo a la que enlaza el botón "Catálogo".

**Familias expuestas en el visor (5):** Pyramid, Symmetric (`Symetric_`), Asymmetric
(`Asymetric_`), Escaler, Kaotico (`Kaotiko_`). Coinciden con las del catálogo.

> ⚠️ En `models/` hay además `.glb` de **AcerOnda, Kubo, Nordik, Origami, Ritmiko** que NO se
> exponen hoy en el visor ni en el catálogo. Decisión pendiente del líder: exponerlas o retirarlas.

**Deep-link por QR:** `index.html?family=<anchor>&type=<medida>`. `resolveFamily()` acepta clave,
label o anchor (case-insensitive). Los QR del catálogo (`assets/qr/qr_<familia>.png`) apuntan aquí.

**Recoloreado:** `applyColor()` recorre `model.materials` y aplica
`pbrMetallicRoughness.setBaseColorFactor()` con el RAL elegido (array `colors`).

**Claves a NO romper** (costó hacerlas funcionar):
- CDN jsDelivr de `@google/model-viewer@4.0.0` (no googleapis). **Versión fijada** a propósito:
  no volver a `/dist/` sin versión (un breaking change de la librería rompería el visor en silencio).
- El evento `load` solo oculta el spinner y aplica color; **nada de mover la cámara ahí**
  (cuelga con "rAF timed out").
- `.viewer-container` necesita **altura fija en vh** (`height`), **nunca `flex`** → con flex
  el visor queda a 0px y desaparece. El `bottom-panel` sí es `flex:0 0 auto`.
- Órbita: `min/max-camera-orbit` abiertos (`auto 0deg/180deg`) para girar 360°; `disable-pan`
  mantiene el giro centrado en la pieza.
- Nombres de .glb con espacio (`Nordik_24 A.glb`): el `src` pasa por `encodeURI()`.

---

## 4. Catálogo (`catalogo.html`)

Una sola página, narrativa **Sistema · Forma · Material · Acabado**. Orden de secciones (= PDF 260701):

1. **Hero** (1/3 banda roja + render a sangre, texto a caballo).
2. **La fachada como identidad** / **Cada forma nace de una intención** (editorial de marca).
3. **Concepto** — las cuatro decisiones (Sistema · Forma · Material · Acabado), grid de 4 tarjetas.
4. **02 · Dos sistemas** — primero la banda **"La gama completa de Metalperfil"** (10 iconos SVG;
   en granate lo incluido en catálogo) y después el desglose vista/oculta (fotos reales +
   esquemas de sección del PDF `esq_fix_*.webp` + gamas SVG).
5. **03 · Tres caminos** — Origami™ / Flow™ / Uniko™ (panel oscuro).
6. **04 · Origami™** — render dinámico de las 5 familias (`FAMILIES` → `famList`),
   con chips de **Aplicaciones recomendadas** por familia (datos del PDF pág. 17).
7. **05 · Flow™** — estrategias A·Mezcla / B·Ritmo / C·Perforación (SVG), matriz, tira de 5 familias, composiciones.
8. **06 · Uniko™** — servicio a medida (5 pasos con fotos reales del PDF, ejemplos).
9. **07 · Materia** (8 texturas reales en 2 grupos) / **08 · Acabados & color** (`FINISHES` → `finGrid`) / **09 · Perforación** (beneficios con foto).
10. **10 · Aplicaciones** (exterior / interior) — sección propia de la web; el PDF ya no la tiene.
11. **Construimos soluciones** — intro, **6 servicios de oficina técnica** (tarjetas con icono SVG),
    **panel oscuro de sostenibilidad / rendimiento verificable** (PDF pág. 33) y después el bloque
    BIM: flujo, 3 plugins propios y herramientas.
12. **Cierre**, **footer / contacto**.

### 4.1 Esquema de una familia en `FAMILIES`
```js
{
  num, name, anchor, tag,                    // tag = lema en cursiva
  attrs: [...],                              // chips (atributos)
  desc,                                      // descripción larga (.fam-desc)
  render,                                    // render de la pieza en arquitectura
  product,                                   // recorte de pieza suelta (img/NN_*_cut.png)
  types: [{ lab, ancho, altura, angulo?, img }],  // fichas "Tipos y dimensiones"
  model: { prefix, types }                   // visor 3D inline por familia + selector de tipo
}
```
Render JS: `famList` construye cada `article.fam-block` (render+producto, num+nombre+tag+desc,
chips, perfil SVG `PROFILES[anchor]`, visor 3D con posters `img/types/type_<anchor>_<file>.jpg`,
tabla "Tipos y dimensiones", ficha técnica con QR a `index.html?family=<anchor>`).

**`PROFILES`** = paths SVG reales de la fibra neutra (del DXF), `viewBox="0 17 100 10"`.
Las 5 familias actuales tienen perfil real trazado.

### 4.2 Acabados (`FINISHES`)
Array de familias de acabado (Solid Colors, Metallic, Anodic, Textured, Matt, Wood, Corten,
Custom). Chips de color (`sw`) o gradiente (`grad`) generados a `finGrid`. **Muestra orientativa**
de práctica del sector — confirmar gama real con la empresa.

### 4.3 SEO / social
`catalogo.html` lleva `meta description`, Open Graph, Twitter Card, canonical y JSON-LD
(`Organization`). `index.html` lleva el equivalente (añadido 2026-06-29).

---

## 5. Estado del contenido

| # | Familia | Catálogo | 3D (.glb) | Render de familia |
|---|---|---|---|---|
| 01 | Pyramid | real | sí | `img/propuesta/fam_pyramid.webp` |
| 02 | Symmetric | real | sí (`Symetric_`) | `img/catalogo/fam_symmetric.webp` (foto real del PDF 260701) |
| 03 | Asymmetric | real | sí (`Asymetric_`) | `img/catalogo/fam_asymmetric.webp` (foto real del PDF 260701) |
| 04 | Escaler | real | sí | `img/propuesta/escaler_front.webp` |
| 05 | Kaotico | real | sí (`Kaotiko_`) | `img/catalogo/fam_kaotico.webp` (foto real del PDF 260701) |

Inconsistencias nombre archivo↔comercial: `Symetric/Asymetric/Kaotiko` (.glb) vs
Symmetric/Asymmetric/Kaotico (web). Se resuelven en el mapeo `label`/`prefix`.

**Bloques aún en PLACEHOLDER — 8** (también son placeholder en el propio PDF 260701):
3 composiciones Flow (B1 latón, B2 ritmo cromático, B3 combinación), 1 ejemplo frontal Uniko
(D1), protección solar exterior (F3), 2 aplicaciones interiores (F5, F6) y el esquema de
cálculo de ancho (H1). **Contacto** con datos genéricos (el PDF también los trae ficticios).

---

## 6. Herramientas (`tools/`)

Requiere Python 3 + `pip install PyMuPDF Pillow`. Desde la raíz del repo:

- `python tools/extract_pdf.py` → re-extrae imágenes (≥400 px, deduplicadas) a `img/` +
  `img/_manifest.json` + `img/_texto.txt`. Ejecutar cada vez que el cliente sube un PDF nuevo.
- `python tools/trim_logo.py` → regenera `assets/Metalperfil_white_trim.png`.

---

## 7. Flujo de trabajo (git / despliegue)

- No hay `git` en el PATH del equipo; se usa el de **GitHub Desktop**
  (`%LOCALAPPDATA%\GitHubDesktop\app-<ver>\resources\app\git\cmd\git.exe`).
- `commit` + `push` a `main`; GitHub Pages redespliega solo en 1-2 min.
- No subir a `img/` archivos pesados que no se usen en la web (van a `source/` + `.gitignore`).
  Ojo: en `.gitignore` **no** poner comentarios en la misma línea que el patrón (ya coló 68 MB una vez).

---

## 8. Tareas pendientes (al 2026-07-03)

1. **Decisión del líder:** las 5 familias con `.glb` pero sin sección (AcerOnda, Kubo, Nordik,
   Origami, Ritmiko) → exponer en el visor/catálogo o retirar sus `.glb`.
2. **Fotos reales** para los 8 bloques PLACEHOLDER restantes (ver §5) — también faltan en el PDF.
3. **Datos de contacto reales** (footer y sección Contacto): email, teléfono, dirección.
4. **Corregir el InDesign** (avisar a maquetación): "Eskaler/Eskala/Skala" (3 grafías), "Kaotico 72"
   vs 73, dimensiones de Eskaler copiadas de Symmetric, Pyramid 68 con 893/793 contradictorios;
   la referencia son los datos de `_PERFILES_MASTER`.
5. **Limpieza de raíz:** `propuesta.html` y `run_extraction.bat` (vacíos), `catalogo_clasico.html`;
   imágenes ya no enlazadas (`img/catalogo/flow_proc_0*.webp`, `img/propuesta/uniko_sketch/building`,
   `perf_interior`, `material_samples`… verificar con grep antes de borrar).
6. (Opcional) `sitemap.xml` + `robots.txt` para Pages.
7. Confirmar con la empresa la **gama real de Acabados** (corten, perforados, efectos…).
