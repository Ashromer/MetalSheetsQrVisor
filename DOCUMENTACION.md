# Metalperfil — Visor 3D + Catálogo web · Documentación

Web estática (HTML/CSS/JS, sin framework ni build) alojada en **GitHub Pages**.
Repo `Ashromer/MetalSheetsQrVisor`, rama `main`.

- **Visor 3D:** https://ashromer.github.io/MetalSheetsQrVisor/ (`index.html`)
- **Catálogo:** https://ashromer.github.io/MetalSheetsQrVisor/catalogo.html

> Actualizado 2026-06-29. El catálogo se reescribió a una narrativa de marca
> **Sistema · Forma · Material · Acabado** (Origami™ / Flow™ / Uniko™) con **5 familias**.
> Esta doc refleja ese estado; descarta versiones anteriores que hablaban de 11 familias.

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

Una sola página, narrativa **Sistema · Forma · Material · Acabado**. Orden de secciones:

1. **Hero** (1/3 banda roja + render a sangre, texto a caballo).
2. **La fachada como identidad** / **Cada forma nace de una intención** (editorial de marca).
3. **Concepto** — las cuatro decisiones (Sistema · Forma · Material · Acabado), grid de 4 tarjetas.
4. **Tres propuestas de valor** — Origami™ / Flow™ / Uniko™ (panel oscuro).
5. **02 · Dos sistemas** — fijación vista vs oculta (diagrama ramificado + gamas SVG).
6. **03 · Origami™** — render dinámico de las 5 familias (`FAMILIES` → `famList`).
7. **04 · Flow™** — combinación de perfiles (proceso 4 pasos, matriz de mezcla, composiciones).
8. **05 · Uniko™** — servicio a medida (proceso 5 pasos, ejemplos).
9. **06 · Materia** / **07 · Acabados & color** (`FINISHES` → `finGrid`) / **08 · Perforación**.
10. **09 · Aplicaciones** (exterior / interior).
11. **BIM / del diseño a la obra** — flujo, 3 plugins propios, herramientas.
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
| 01 | Pyramid | real | sí | `img/propuesta/fam_pyramid.jpg` |
| 02 | Symmetric | real | sí (`Symetric_`) | `img/propuesta/fam_symmetric.jpg` |
| 03 | Asymmetric | real | sí (`Asymetric_`) | `img/p14_1.jpeg` (recorte crudo — pendiente render curado) |
| 04 | Escaler | real | sí | `img/propuesta/escaler_front.jpg` |
| 05 | Kaotico | real | sí (`Kaotiko_`) | `img/propuesta/fam_kaotico.jpg` |

Inconsistencias nombre archivo↔comercial: `Symetric/Asymetric/Kaotiko` (.glb) vs
Symmetric/Asymmetric/Kaotico (web). Se resuelven en el mapeo `label`/`prefix`.

**Bloques aún en PLACEHOLDER** (esperan foto real del cliente): composiciones de Flow,
prototipo y frontal de Uniko, varias aplicaciones interiores. **Contacto** con datos genéricos
(`info@metalperfil.com`, sin teléfono/dirección).

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

## 8. Tareas pendientes (al 2026-06-29)

1. **Decisión del líder:** las 5 familias con `.glb` pero sin sección (AcerOnda, Kubo, Nordik,
   Origami, Ritmiko) → exponer en el visor/catálogo o retirar sus `.glb`.
2. **Render curado de Asymmetric** (hoy usa el recorte crudo `img/p14_1.jpeg`).
3. **Fotos reales** para los bloques PLACEHOLDER (Flow, Uniko, Aplicaciones).
4. **Datos de contacto reales** (footer y sección Contacto): email, teléfono, dirección.
5. **Limpieza de assets huérfanos** (~40 MB de extracciones `pNN_*`, `desarrollo_*`, variantes
   de `propuesta/` no enlazadas) → mover a `source/` o borrar.
6. **Optimización de imágenes:** convertir los JPEG ~1 MB a WebP/AVIF (reduce ~50% el peso).
7. **Limpieza de raíz:** `propuesta.html` y `run_extraction.bat` (vacíos), `Captura_correccion.JPG`,
   backups `catalogo_backup_*.html` / `catalogo_clasico.html`.
8. (Opcional) `sitemap.xml` + `robots.txt` para Pages.
9. Confirmar con la empresa la **gama real de Acabados** (corten, perforados, efectos…).
