---
name: alto-contraste
description: Adapta cualquier sitio web o app a alto contraste para usuarios de baja visión (WCAG 2.2 AA/AAA). Pregunta qué paleta quiere la persona (presets de We.Inc, ideas de Media.io o una paleta propia), aplica los colores mediante variables CSS, verifica cada par con contraste WCAG y entrega un documento .md con las variables. Úsalo cuando pidan "alto contraste", "baja visión", "accesibilidad visual", "adaptar la web/app para personas con baja visión", "paleta de contraste" o "modo alto contraste".
---

# Alto contraste para baja visión

## Objetivo
Dejar una web o app legible para personas con baja visión, con una paleta elegida por la persona, verificada con cifras WCAG y aplicada por variables, sin reescribir el HTML.

## Flujo obligatorio

### 1. Preguntar la paleta
Antes de tocar código, pregunta con opciones (usa `ask_user_input_v0` si está disponible):
- **Presets We.Inc** (5 paletas verificadas): Tinta sobre papel, Turno de noche, Libro del bosque, Azul puerto, Arcilla cálida. Ver `references/paletas.md`.
- **Ideas Media.io** (24 combinaciones de referencia, no verificadas): elegir una por nombre o por estado de ánimo. Ver `references/paletas.md`.
- **Paleta propia**: pedir fondo, texto, acento (o colores de marca). Si hay marca, mantener el color como acento solo si pasa la verificación; si no, proponer el ajuste mínimo de luminosidad.

Si la persona no sabe, recomienda "Turno de noche" (fondo oscuro, texto claro) o "Tinta sobre papel" (fondo claro, texto negro azulado) y pregunta cuál prefiere al ver las dos.

### 2. Preguntar el alcance
- **App o web propia** (hay código): aplicar variables CSS en el proyecto.
- **Web de terceros**: no se puede editar el sitio. Entregar el bloque CSS para una extensión de usuario (p. ej. una hoja de estilos inyectada) o el CSS para pegar en el tema del sitio.

### 3. Verificar antes de aplicar
Toda paleta, incluida cualquier de Media.io, pasa por `scripts/contraste.py`:

```bash
python3 scripts/contraste.py --paleta presets/we-inc-turno-de-noche.json
python3 scripts/contraste.py "#FFFFFF" "#111827"   # un par suelto
```

Para Media.io, asigna roles así: `fondo` = el neutro más oscuro o más claro; `texto` = el neutro de extremo opuesto; `texto_secundario` = otro neutro; `acento` = el color vivo; `texto_sobre_acento` = el neutro que más contraste dé sobre el acento. Si la paleta no pasa, di qué par falla y ajusta solo ese color (la luminosidad, no el matiz). No ofrezcas una paleta que no pase.

### 4. Aplicar con variables
Nombra las variables por función, nunca por color: `--fondo`, `--superficie`, `--texto`, `--texto-secundario`, `--acento`, `--texto-sobre-acento`, `--foco`, `--borde`, `--error`, `--exito`. Así cambiar de paleta es editar un bloque.

Usa `templates/paleta-personalizada.md` para generar el documento `.md` con las variables, los ratios y el bloque CSS. Entrégalo siempre que la persona haya armado una paleta propia y también como referencia de cualquier paleta elegida.

### 5. Reglas de accesibilidad (aplicar en todo el sitio)
- **Texto**: mínimo 7:1 (AAA) en texto normal y 4.5:1 en texto grande (18pt o 14pt en negrita). Si un par solo llega a AA, dilo en el informe.
- **No textual** (iconos, bordes de campos, anillo de foco, botones): mínimo 3:1.
- **Tamaño base**: `1.125rem` a `1.25rem` (18–20 px), relativo para que escale con el navegador. Nunca px fijos en el texto.
- **Interlineado**: mínimo 1.5. Separación entre párrafos: entre 1em y 2em (no obligatorio llegar a 2em si rompe el diseño).
- **Tipografía**: sans-serif de trazo grueso (Arial, Verdana, Tahoma, Open Sans). Sin cursiva para bloques de texto, sin fuentes finas ni decorativas.
- **Color no es el único canal**: errores, confirmaciones y estados llevan icono y texto.
- **Foco visible**: `:focus-visible` con `outline: 3px solid var(--foco)` y `outline-offset: 2px`, con doble anillo si el fondo es oscuro.
- **Áreas táctiles**: mínimo 24×24 px (WCAG 2.5.8 AA); recomendado 44–48 px (2.5.5 AAA).
- **Diseño**: una columna, sin texturas, degradados ni imágenes detrás del texto. Debe funcionar al 200 % de zoom y en 320 px de ancho sin scroll horizontal (1.4.10).
- **Preferencias del usuario**: respeta `prefers-color-scheme`, `prefers-contrast: more` y `prefers-reduced-motion`. No fuerces un modo que el sistema contradice sin ofrecer un botón para cambiarlo.
- **Hover** y **foco** deben ser más visibles que el estado normal, pero nunca dependen solo del hover (el teclado no lo tiene).

### 6. Auditar y entregar
- Revisar las páginas principales con axe DevTools o Lighthouse (categoría accesibilidad) y comprobar el zoom al 200 %.
- Entregar: el `.md` de variables, el bloque CSS aplicado y el resultado del script. Resume en una frase qué paleta se aplicó y qué pares quedaron en AA en lugar de AAA.

## Reglas
- No inventes ratios: calcúlalos con `scripts/contraste.py` o con la herramienta de We.Inc.
- No pidas más de dos o tres preguntas a la vez; el resto se asume y se declara.
- Si la persona pide "modo claro inverso", es una paleta más: pásala por el mismo flujo.
- Si el sitio es de terceros y no hay forma técnica de inyectar CSS, dilo claramente y no simules un cambio.

## Archivos
- `references/paletas.md`: presets We.Inc y 24 ideas de Media.io con sus HEX.
- `presets/*.json`: presets We.Inc listos para `contraste.py --paleta`.
- `scripts/contraste.py`: verificación WCAG 2.2 de pares y paletas.
- `templates/paleta-personalizada.md`: plantilla del documento de variables.
