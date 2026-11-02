# matematicado

**Matemáticas aplicadas a vibraciones y monitorización estructural, para aprender por tu cuenta.**

Web: <https://me1catrr.github.io/matematicado/>

Cada herramienta matemática se aprende respondiendo a una pregunta sobre una estructura: ¿qué frecuencias y amortiguamientos tiene?, ¿por qué dos sensores ven picos distintos?, ¿cuánto hay que medir para separar dos modos? Todo se apoya en un edificio de tres plantas sintético, de respuesta conocida, para validar cada método contra la verdad. Hay simulaciones interactivas en el navegador, práctica en Julia (con pestaña Python), ejercicios autocorregibles y propuestas de trabajo con Claude Code.

## Temario

| Bloque | Páginas |
|---|---|
| **E** · Caso transversal | E · Un edificio de tres plantas |
| **A** · Álgebra lineal (`algebra/`) | A1 Matrices estructuradas · A2 Valores propios · A3 SVD |
| **S** · Sistemas dinámicos (`sistemas/`) | S1 Laplace y función de transferencia · S2 Espacio de estados · S3 Transformada Z |
| **F** · Señales (`senales/`) | F1 Fourier · F2 Hilbert y señal analítica |
| **P** · Probabilidad y procesos (`probabilidad/`) | P1 Procesos estocásticos · P2 Correlación |

Unas 33 h en total, con tres itinerarios más cortos (exprés de 4 h, esencial de unas 12 h e identificación de unas 20 h) descritos en la portada.

## Puesta en marcha

```bash
git clone https://github.com/me1catrr/matematicado.git
cd matematicado
julia --project=. -e 'using Pkg; Pkg.instantiate()'   # incluye Resonancia.jl desde GitHub
quarto preview                                        # vista previa del sitio
```

Python (opcional) con [uv](https://docs.astral.sh/uv/): `uv sync` y `uv run pytest python`.

## Estructura

- `algebra/`, `sistemas/`, `senales/`, `probabilidad/`, `caso/`: una carpeta por unidad, con su portada (`index.qmd`), una página por apartado (`a1-1.qmd`…), la «Práctica y cierre» (`practica.qmd`) y sus figuras TikZ en `fig/`.
- `_freeze/`: resultados de Julia ya calculados. La publicación en GitHub Actions no tiene Julia y los lee de aquí.
- `recursos/`: bibliografía, estilos TikZ, tema de las figuras de Makie y JavaScript de los laboratorios y los ejercicios.
- `scripts/`: filtros de Quarto, compilación de figuras TikZ y generación de datos y referencias.
- `datos/`: el edificio de tres plantas (sintético) y un registro real del puente de Torroja (CC BY 4.0).
- `python/`: versión probada del código de las pestañas Python. `referencia/`: resultados de Julia con los que se prueban Python y JavaScript.
- `pruebas/web/`: pruebas de navegador de los laboratorios.

## Origen

Este material es la sesión M2 de [Resonancia](https://me1catrr.github.io/resonancia/), un curso de autoformación en vibraciones, señales y monitorización estructural de la Universidad de Córdoba, separada en su propio repositorio a partir del commit `f677c80`. Las funciones que usa están en el paquete [Resonancia.jl](https://github.com/me1catrr/resonancia/tree/main/Resonancia.jl).

## Licencia

Textos, figuras y diapositivas: [CC BY-SA 4.0](LICENSE-CONTENIDO). Código: [MIT](LICENSE). Datos: la licencia de la ficha `.meta.toml` de cada conjunto.
