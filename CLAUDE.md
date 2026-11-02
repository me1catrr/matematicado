# matematicado — instrucciones para Claude Code

## Qué es
Web de autoformación en Quarto: *matemáticas aplicadas a vibraciones y monitorización
estructural*. Responsable único: Rafael Castro Triguero (GitHub `me1catrr`). Se publica en
https://me1catrr.github.io/matematicado/. Procede de la sesión M2 de Resonancia
(`me1catrr/resonancia`, commit f677c80), donde M2 se ha quedado en una clase de 4 h que enlaza aquí.

## Temario e identificadores
Cinco bloques: E (`caso/`), A (`algebra/`), S (`sistemas/`), F (`senales/`) y P (`probabilidad/`).
Cada unidad (A1, S2…) es una carpeta con tres tipos de página:
- `index.qmd`, la **portada**: introducción, «Cómo se lee esta unidad», objetivos y prerrequisitos
  y la tabla de apartados. Su cabecera declara `id`, `bloque`, `requiere` (ids de esta web) y
  `previo-resonancia` (unidades de Resonancia).
- `a1-1.qmd`, `a1-2.qmd`…, **un apartado por página**, con `id: A1.1` y `unidad: A1`. Su título
  empieza por el id. Los ejercicios intercalados y el laboratorio del apartado van en su página.
- `practica.qmd`, **«Práctica y cierre»**: práctica guiada, «Pídeselo a Claude», ejercicios,
  «La doy por superada si…» y «Qué no dice esta unidad».

La barra lateral (bloque → unidad → apartados) está en `_quarto.yml`. La tabla del temario, el
mapa de dependencias (`recursos/fig/mapa.tex`) y los itinerarios están en `index.qmd`.
No inventes páginas ni identificadores: propón el cambio y espera aprobación.
Cada apartado repite el bloque de configuración de Julia de su unidad (`using`, `include` del tema
y datos) y recalcula lo que necesite; las funciones nuevas van a Resonancia.jl. Las referencias
cruzadas a otra página se escriben como enlace (`[Teorema 1 de A2.1](a2-1.qmd#thm-espectral)`),
porque Quarto no numera entre páginas de un sitio web.
Los `id` de los ejercicios (`m2-…`) se conservan de Resonancia porque son las claves de
`localStorage`: no los cambies. Resonancia enlaza a los apartados desde su M2, M3, M7, J1 y J3.
Las anclas de la antigua página única (`index.html#a1-4`) redirigen al apartado con el script
del final de cada portada: si mueves un apartado, actualiza ese mapa y avisa.

## Convenciones de contenido
- Español de España. Término técnico inglés entre paréntesis la primera vez. Unidades SI.
  Notación: f (Hz), ω (rad/s), ζ, M, C, K.
- Julia primero, con pestaña Python. Toda página que ejecute Julia lleva `engine: julia`.
  Nunca Jupyter ni IJulia. El Python de las pestañas no se ejecuta: su versión probada está en
  `python/`, con pytest contra `referencia/matrices.json` (generado por `scripts/generar_referencia.jl`).
- Figuras con CairoMakie (tema en `recursos/_tema.jl`). Datos aleatorios con semilla fija.
- No reproduzcas texto de libros ni de fuentes con copyright: redacta con palabras propias y cita
  con `recursos/bibliografia.bib` (campos `keywords` y `verificado`). Las páginas que citan llevan
  `citation-location: margin`.
- Plantilla de unidad: portada (objetivos y prerrequisitos); apartados con teoría en tres capas
  (intuición, fundamento, aplicación) y laboratorios; «Práctica y cierre» (práctica guiada,
  «Pídeselo a Claude» con *Verifica*, ejercicios, «La doy por superada si…», «Qué no dice esta unidad»).
- Cajas, ejercicios intercalados (`::: {.ejercicio tipo="…" id="…" respuesta="…"}`) y laboratorios
  (`.laboratorio .solo-pantalla` con su figura en `.solo-impresion`): como en Resonancia; véanse
  `styles.css`, `scripts/ejercicios.lua` y `recursos/js/ejercicios.js`. Toda respuesta numérica
  se comprueba antes en Julia.

## Código y entornos
- Un entorno Julia en la raíz. `Resonancia` entra desde GitHub (subcarpeta `Resonancia.jl`,
  fijado a un commit). Las funciones reutilizables van a Resonancia.jl, en su repositorio, con
  docstring y test; aquí no se copian funciones entre páginas. Para subir de versión: nuevo commit
  en Resonancia y `Pkg.add(url=…, subdir="Resonancia.jl", rev=…)` con confirmación.
- `recursos/js/matematicas.js` es copia del de Resonancia (lo usan los laboratorios). Si cambia
  allí, se actualiza aquí y se pasan sus pruebas.
- Python con `uv` (`pyproject.toml`). No uses conda.
- `_freeze/`: toda página con Julia se commitea con su `_freeze/`. Tras editarla,
  `quarto render <fichero>` y, en el mismo commit, la página y los ficheros de `_freeze/` que
  cambien. La publicación (GitHub Actions, sin Julia) lee `_freeze/`.
- TikZ: `fig/nombre.tex` con `\usepackage{resonancia}` (estilo en `recursos/tikz/resonancia.sty`);
  se compila con `julia --project=. scripts/compilar_tikz.jl` y se commitean `.tex` y `.svg`.

## Comprobaciones
- `quarto render` (o `quarto render <fichero>` tras editar una página).
- `julia --project=. scripts/compilar_tikz.jl --comprobar`.
- `deno test --no-check --allow-read recursos/js/` (con el Deno de Quarto).
- `uv run pytest python` y, con el sitio compilado y Chromium, `uv run pytest pruebas/web`.

## Forma de trabajar
- Antes de cambios que afecten a varios ficheros, presenta un plan y espera aprobación.
- Nunca ejecutes `git push`, `quarto publish` ni cambies la configuración de GitHub sin petición explícita.
- Commits pequeños, mensaje en español en imperativo: «Añade el itinerario esencial».
- Lo pendiente está en `ROADMAP.md`; el registro histórico de la fase en Resonancia, en `_plan/`.
