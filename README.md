# Análisis de Algoritmos

Caso: consolidación diaria de asistencia, permisos y vacaciones.

## Introducción

Mi repositorio reúne el trabajo del curso aplicado a un caso real: la consolidación diaria de asistencia, permisos y vacaciones. Cada día RRHH cruza el reporte del reloj checador con las listas de empleados, permisos y vacaciones para detectar faltas, retrasos y omisiones. Son unos 300 empleados y 1.200 registros por día. Hoy se hace en Excel con BUSCARV y CONTAR.SI.CONJUNTO y tarda cerca de una hora diaria, porque esas funciones recorren toda la lista por cada marcación (O(n²)).

A lo largo de los hitos, las prácticas y los parciales se analizó ese costo, se compararon estructuras y algoritmos y se midió con evidencia. Para buscar y contar por código de empleado se eligió una tabla hash, y para ordenar el reporte, el sort de Python. Las estrategias (voraz y programación dinámica) y los grafos se estudiaron, y se concluyó que el proceso no los necesita, así que se practicaron con un caso análogo. Las mediciones lo respaldan: con 9.600 datos la tabla hash fue unas 1.225 veces más rápida que la lista.

Las carpetas de cada hito (`h1/`, `h2/`, `h3/`), las prácticas, los parciales y la integradora están en la raíz del repositorio, con los nombres con los que se entregaron en cada tarea.

## Hitos del caso

**H1, el proceso y su costo:** [h1/h1.md](h1/h1.md) y la muestra de datos [h1/muestra.xlsx](h1/muestra.xlsx).

**H2, la estructura de datos:**
- [Inventario de operaciones](h2/inventario.md)
- [Estructura elegida y costo de cada operación](h2/estructura.md)
- [Medición](h2/medicion.md) y su código [medicion.py](h2/medicion.py)

**H3, la estrategia:**
- [Estrategia: voraz o dinámica](h3/estrategia.md)
- [Comparación medida](h3/comparacion.md) y su código [comparacion.py](h3/comparacion.py)
- [Mi caso como grafo](h3/grafo.md)

## Prácticas

- **c3:** [tabla de mediciones](practicas/c3/tabla_mediciones.md)
- **c4:** [búsqueda binaria a mano](practicas/c4/busqueda_binaria_a_mano.md) y [lineal contra binaria](practicas/c4/comparacion_lineal_vs_binaria.md)
- **c5:** [torneo de ordenamientos](practicas/c5/torneo_ordenamientos.md)
- **c6:** [recurrencias con el teorema maestro](practicas/c6/recurrencias_teorema_maestro.md) y [elección del ordenamiento](practicas/c6/eleccion.md)

## Parciales

- **Parcial 1:** [análisis](parcial1/analisis.md), [medición](parcial1/medicion.md) y [elección](parcial1/eleccion.md)
- **Parcial 2:** [elección](parcial2/eleccion.md), [medición](parcial2/medicion.md) y [código](parcial2/pedidos.py)

## Integradora

- [Análisis](integradora/analisis.md) y [medición](integradora/medicion.md)