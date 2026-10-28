# Paleta de alto contraste: {{NOMBRE_DEL_PROYECTO}}

**Fecha:** {{FECHA}}
**Origen de la paleta:** {{We.Inc / Media.io / Propia}}
**Nivel objetivo:** WCAG 2.2 AAA en texto principal, AA mínimo en el resto.

## 1. Variables

| Variable | Función | HEX | Fondo donde se usa | Ratio | Nivel |
|---|---|---|---|---|---|
| `--fondo` | Fondo de página | {{#HEX}} | — | — | — |
| `--superficie` | Tarjetas, paneles | {{#HEX}} | `--texto` | {{r}}:1 | {{nivel}} |
| `--texto` | Texto principal | {{#HEX}} | `--fondo` | {{r}}:1 | {{nivel}} |
| `--texto-secundario` | Fechas, notas, pies | {{#HEX}} | `--fondo` | {{r}}:1 | {{nivel}} |
| `--acento` | Botones, enlaces, insignias | {{#HEX}} | `--fondo` (no textual) | {{r}}:1 | {{nivel}} |
| `--texto-sobre-acento` | Texto dentro de botones | {{#HEX}} | `--acento` | {{r}}:1 | {{nivel}} |
| `--foco` | Anillo de foco | {{#HEX}} | `--fondo` (no textual) | {{r}}:1 | {{nivel}} |
| `--borde` | Bordes de campos y botones | {{#HEX}} | `--fondo` (no textual) | {{r}}:1 | {{nivel}} |
| `--error` | Mensajes de error (con icono y texto) | {{#HEX}} | `--fondo` | {{r}}:1 | {{nivel}} |
| `--exito` | Confirmaciones (con icono y texto) | {{#HEX}} | `--fondo` | {{r}}:1 | {{nivel}} |

Los ratios se obtienen con `scripts/contraste.py --paleta`. Cualquier fila en "NO CUMPLE" debe corregirse antes de publicar.

## 2. Bloque CSS

```css
:root {
  --fondo: {{#HEX}};
  --superficie: {{#HEX}};
  --texto: {{#HEX}};
  --texto-secundario: {{#HEX}};
  --acento: {{#HEX}};
  --texto-sobre-acento: {{#HEX}};
  --foco: {{#HEX}};
  --borde: {{#HEX}};
  --error: {{#HEX}};
  --exito: {{#HEX}};

  font-size: 1.125rem; /* 18px base, escala con el navegador */
  line-height: 1.5;
  color-scheme: {{light|dark}};
}

body {
  background: var(--fondo);
  color: var(--texto);
  font-family: Verdana, Tahoma, Arial, sans-serif;
}

a, button { color: var(--acento); }

button, .btn-primario {
  background: var(--acento);
  color: var(--texto-sobre-acento);
  min-height: 48px;
  min-width: 48px;
  border: 2px solid var(--borde);
}

:focus-visible {
  outline: 3px solid var(--foco);
  outline-offset: 2px;
}

input, select, textarea {
  background: var(--superficie);
  color: var(--texto);
  border: 2px solid var(--borde);
}

@media (prefers-contrast: more) {
  :root { --texto-secundario: var(--texto); }
}
```

## 3. Modo alternativo
{{Si la persona pidió modo claro inverso o un segundo preset, repetir la tabla y el bloque con sus HEX. Si no, eliminar esta sección.}}

## 4. Verificación
- [ ] `contraste.py --paleta` sin pares "NO CUMPLE"
- [ ] Axe o Lighthouse sin errores de contraste en páginas principales
- [ ] Zoom 200 % sin scroll horizontal; 320 px de ancho en una columna
- [ ] Foco visible con teclado en todos los controles
- [ ] Ningún dato transmitido solo por color

## 5. Notas
{{Decisiones tomadas, pares que quedaron en AA, cambios pendientes.}}
