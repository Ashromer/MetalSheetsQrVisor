# Prompts de imágenes — Placeholders de `catalogo.html`

> **Para:** Antigravity (Gemini) · generador de imágenes Pro
> **De:** Claude (diseño web) · 2026-06-25
> **Objetivo:** sustituir los 28 placeholders (`<div class="ph">`) de `catalogo.html` por imágenes reales.

> **ESTADO 2026-06-25:** 16/28 colocadas en el HTML (marcadas ✅ abajo).
> **Faltan 12** (marcadas ⬜). Notas:
> - 4 imágenes IA se descartaron por calidad y se revirtieron a placeholder (B1 latón, B3 combinación, C2 prototipo, E1 panorámica) — regenerar.
> - Los 5 huecos BIM (G1·G2·G3 plugins, H2·H3 herramientas) se rellenaron con **capturas reales** del líder
>   (`bim_plugin1/2/3.JPG`, `bim_tools_02/03.jpeg`). Solo queda **H1** (esquema cálculo de ancho) como placeholder.

## Cómo usar este documento
1. Genera cada imagen con el **prompt** indicado y el **aspect ratio** exacto (clave para que no haya *layout shift*).
2. Guárdala con el **nombre de archivo destino** que se indica, dentro de `img/catalogo/`.
3. Optimiza a JPG (calidad ~82), ancho máx. 1600 px. Las panorámicas, hasta 2200 px.
4. Avisa a Claude cuando estén listas y él hace el reemplazo HTML (`<div class="ph">…</div>` → `<img src="img/catalogo/…" loading="lazy">`).

## ⚠️ NO generar con IA — son CAPTURAS REALES
Las imágenes **#23, #24, #25 y #28** son capturas de pantalla del software/web real (plugins de Revit y el visor 3D `index.html`). **No las inventes**: pídeselas al líder o tómalas del entorno real, o quedarán falsas y romperán la credibilidad técnica.

---

## ESTILO GLOBAL DE MARCA (incluir en TODOS los prompts)
> Fotografía / render arquitectónico premium. Paleta: antracita y negro mate con acentos metálicos cálidos (latón, bronce, acero cepillado). Luz natural rasante que revela el relieve del plegado metálico. Composición limpia, minimalista, editorial. Sin texto, sin marcas de agua, sin personas salvo que se indique. Alta gama, revista de arquitectura, no aspecto "stock" ni MVP.

Pega este bloque de estilo **al final de cada prompt** (los prompts de abajo asumen este estilo común).

---

# BLOQUE A · FLOW — "El proceso" (4 imágenes)
**Serie coherente: misma luz, mismo lenguaje visual.** Aspect ratio **1:1** (casi cuadrado, formato tarjeta).

### ⬜ A1 — `img/catalogo/flow_proc_01_fachada.jpg` · `catalogo.html:532`
> Render conceptual de un paño de fachada arquitectónica desnudo y neutro, superficie lisa de hormigón claro con líneas de replanteo y modulación marcadas, listo para ser revestido. Sin perfiles aún. Luz lateral suave. Sensación de "lienzo en blanco" antes del diseño.

### ✅ A2 — `img/catalogo/flow_proc_02_opciones.jpg` · `catalogo.html:533`
> Bodegón cenital de cinco perfiles metálicos arquitectónicos plegados distintos (geometrías variadas: piramidal, ondulado, escalonado, simétrico), alineados en paralelo sobre fondo antracita mate, mostrando la variedad de formas disponibles para combinar. Latón y acero cepillado.

### ✅ A3 — `img/catalogo/flow_proc_03_acabado.jpg` · `catalogo.html:534`
> Mismo perfil metálico plegado repetido seis veces en abanico, cada copia con un acabado distinto: latón pulido, cobre, acero cepillado, lacado negro mate, blanco, y perforado. Muestra la personalización de material, color y perforación. Fondo neutro.

### ✅ A4 — `img/catalogo/flow_proc_04_fijacion.jpg` · `catalogo.html:535`
> Detalle macro de la junta entre dos paneles metálicos de fachada: a la izquierda fijación vista (tornillería metálica visible), a la derecha fijación oculta (junta limpia sin tornillos). Luz rasante que marca la sombra de la junta. Primer plano técnico y elegante.

---

# BLOQUE B · FLOW — "Composiciones" (6 imágenes)
**Fotografía de obra real / render fotorrealista de fachadas terminadas.** Aspect ratio **4:3**.

### ⬜ B1 — `img/catalogo/flow_comp_01_laton.jpg` · `catalogo.html:557`
> Fachada arquitectónica terminada revestida con perfiles metálicos en latón dorado, fotografiada al atardecer con luz cálida que hace brillar el metal. Composición FLOW de varios perfiles combinados. Edificio contemporáneo.

### ✅ B2 — `img/catalogo/flow_comp_02_cromatico.jpg` · `catalogo.html:558`
> Fachada metálica donde un mismo perfil ondulado se repite en varios colores alternados (tonos tierra, bronce, antracita), creando un ritmo cromático vibrante pero elegante en la envolvente del edificio.

### ⬜ B3 — `img/catalogo/flow_comp_03_combinacion.jpg` · `catalogo.html:559`
> Fachada que combina dos geometrías de perfil distintas en un mismo paño (zonas planas y zonas plegadas/onduladas), mostrando cómo conviven varias formas en una sola envolvente metálica.

### ✅ B4 — `img/catalogo/flow_comp_04_textura.jpg` · `catalogo.html:560`
> Fachada metálica de textura mixta: franjas lisas, onduladas y perforadas combinadas. Juego rico de luces y sombras sobre la piel del edificio. Acero cepillado y cobre.

### ✅ B5 — `img/catalogo/flow_comp_05_urbano.jpg` · `catalogo.html:561`
> Edificio con fachada metálica de perfiles plegados en contexto urbano de calle: vista desde la acera, con el cielo reflejado en el metal. Arquitectura contemporánea integrada en la ciudad.

### ✅ B6 — `img/catalogo/flow_comp_06_detalle.jpg` · `catalogo.html:562`
> Primer plano de la transición entre dos perfiles metálicos distintos en una fachada, mostrando el encuentro preciso entre dos geometrías y dos acabados. Detalle constructivo cuidado, luz rasante.

---

# BLOQUE C · UNIKO — "El proceso" (2 imágenes)
Aspect ratio **4:3** (formato `st-img` de la lista de pasos).

### ✅ C1 — `img/catalogo/uniko_proc_03_ingenieria.jpg` · `catalogo.html:584`
> Plano técnico / sección CAD de un perfil de chapa metálica plegada, con cotas, espesores, radios de plegado y líneas de construcción. Estética blueprint o vista de software BIM/CAD profesional. Líneas finas sobre fondo claro o azul técnico. Aspecto de ingeniería real.

### ⬜ C2 — `img/catalogo/uniko_proc_04_prototipo.jpg` · `catalogo.html:585`
> Foto de un prototipo físico de perfil de chapa metálica plegada a escala real, apoyado sobre una mesa de taller con fondo neutro. Luz rasante que revela cada pliegue y el acabado del metal. Muestra de validación previa a la fabricación en serie.

---

# BLOQUE D · UNIKO — "Ejemplos" (3 imágenes)
Aspect ratio **4:3**.

### ⬜ D1 — `img/catalogo/uniko_ej_01_frontal.jpg` · `catalogo.html:592`
> Vista frontal plana de un gran paño de fachada con una composición compleja de muchos perfiles metálicos a medida distintos, ortogonal a cámara, mostrando la riqueza geométrica de un diseño UNIKO exclusivo. Acabados metálicos variados.

### ✅ D2 — `img/catalogo/uniko_ej_02_cromatica.jpg` · `catalogo.html:593`
> La MISMA composición frontal de la imagen anterior (mismos perfiles y disposición), pero explorando una paleta de color distinta para mostrar la customización cromática. Vista frontal plana ortogonal.

### ✅ D3 — `img/catalogo/uniko_ej_03_esquina.jpg` · `catalogo.html:594`
> Detalle constructivo real de una esquina o punto singular de un edificio donde se encuentran varios sistemas de perfil metálico. Resolución elegante del quiebro de la fachada. Luz natural.

---

# BLOQUE E · ACABADOS — Panorámica (1 imagen)
Aspect ratio **21:9** (panorámica ancha, pieza destacada de la sección color).

### ⬜ E1 — `img/catalogo/acabados_panoramica.jpg` · `catalogo.html:671`
> Vista frontal amplia y panorámica de un gran paño de fachada metálica combinando una enorme variedad de perfiles plegados en muchísimos colores RAL distintos (carta de color completa), creando un mosaico cromático espectacular pero arquitectónicamente refinado. Imagen "wow" de portada de sección.

---

# BLOQUE F · APLICACIONES (6 imágenes)
Aspect ratio **4:3** (formato `app-gallery`).

### Exterior
### ✅ F1 — `img/catalogo/app_ext_01_general.jpg` · `catalogo.html:718`
> Vista general de un edificio completo con fachada exterior de perfiles metálicos arquitectónicos. Envolvente metálica como protagonista. Luz natural de día, cielo despejado.

### F2 — `img/catalogo/app_ext_02_detalle.jpg` · `catalogo.html:719`
> Detalle en primer plano de una fachada exterior metálica, zoom sobre la piel de perfiles plegados mostrando textura, relieve y acabado. Luz rasante.

### F3 — `img/catalogo/app_ext_03_solar.jpg` · `catalogo.html:720`
> Sistema de protección solar exterior con lamas metálicas tipo screen filtrando la luz del sol, proyectando sombras sobre el interior. Arquitectura bioclimática contemporánea.

### Interior
### F4 — `img/catalogo/app_int_01_revestimiento.jpg` · `catalogo.html:734`
> Revestimiento interior metálico de pared en un lobby o vestíbulo contemporáneo de alta gama. Perfiles metálicos cálidos (latón/cobre) como acabado interior elegante. Luz interior suave.

### F5 — `img/catalogo/app_int_02_singular.jpg` · `catalogo.html:735`
> Muro o techo interior singular revestido con perfiles metálicos de diseño, como elemento escultórico del espacio. Techo metálico de geometría destacada. Iluminación arquitectónica.

### F6 — `img/catalogo/app_int_03_lineal.jpg` · `catalogo.html:736`
> Sistema lineal metálico interior: lamas o perfiles lineales recorriendo un pasillo, recepción o espacio de tránsito. Ritmo lineal elegante. Acero cepillado o latón.

---

# BLOQUE G · BIM — "Tres plugins" (3 imágenes) — 🖥️ CAPTURAS REALES
Aspect ratio **4:3**. **NO generar con IA** — son capturas de la UI real de los plugins de Revit.

### G1 — `img/catalogo/plugin_01_generador.jpg` · `catalogo.html:776`
> CAPTURA REAL: interfaz del plugin "Generador de familias" mostrando la geometría del perfil (CAD/DXF) convirtiéndose en familia nativa de Revit. Ventana del plugin sobre Revit 2026.

### G2 — `img/catalogo/plugin_02_parametrizador.jpg` · `catalogo.html:777`
> CAPTURA REAL: plugin "Parametrizador de fachada" mostrando el muro cortina de Revit con paneles distribuidos/aleatorizados en la composición de la envolvente.

### G3 — `img/catalogo/plugin_03_twinmotion.jpg` · `catalogo.html:778`
> CAPTURA REAL: modelo de Revit enlazado con Twinmotion mostrando el render/seguimiento visual de la fachada.

---

# BLOQUE H · BIM — "Herramientas" (3 imágenes)
Aspect ratio **4:3**.

### H1 — `img/catalogo/viz_01_calculo.jpg` · `catalogo.html:783`
> Esquema técnico / diagrama de sección horizontal de una fachada metálica con la cota del espesor total acotada (predimensionado de ancho de envolvente). Estética de diagrama de ingeniería limpio, líneas finas, fondo claro. Puede generarse con IA como infografía técnica.

### H2 — `img/catalogo/viz_02_vr.jpg` · `catalogo.html:784`
> Composición que combina visualización avanzada: una imagen renderizada estática de fachada + alusión a recorrido interactivo + experiencia VR (por ejemplo, persona con gafas de realidad virtual revisando un modelo de edificio, o split-screen render/VR). Tecnología y arquitectura.

### H3 — `img/catalogo/viz_03_visor3d.jpg` · `catalogo.html:785` — 🖥️ CAPTURA REAL
> CAPTURA REAL del visor 3D web `index.html` de este mismo proyecto (la más fácil: screenshot directo del visor en el navegador). NO generar con IA.

---

## Resumen de cantidades
| Bloque | Sección | Nº imágenes | Tipo |
|---|---|---|---|
| A | FLOW · proceso | 4 | Render conceptual (serie) |
| B | FLOW · composiciones | 6 | Foto obra real |
| C | UNIKO · proceso | 2 | Plano técnico + foto prototipo |
| D | UNIKO · ejemplos | 3 | Render frontal + foto obra |
| E | Acabados | 1 | Render panorámico |
| F | Aplicaciones | 6 | Foto obra (ext/int) |
| G | Plugins | 3 | 🖥️ Capturas reales |
| H | Herramientas | 3 | 2 render/infografía + 1 🖥️ captura |
| | **TOTAL** | **28** | |
