# Jose Fernando Garcia Sanchez

# P1.3 — Elegir

n = 300.000 historias clinicas, q = 5.000 consultas al dia y memoria limitado

## Costo de cada opcion (en operaciones, peor caso)

**Opcion 1: recorrer cada vez**
- Calculo: q × n = 5.000 × 300.000
- Total: **1.500 millones**

**Opcion 2: ordenar n log n + busqueda binaria**
- Calculo: n log n + q log n ≈ 300.000 × 18 + 5.000 × 18
- Total: **5,5 millones**

**Opcion 3: ordenar cuadratico + busqueda binaria**
- Calculo: n² + q log n ≈ 300.000² + 5.000 × 18
- Total: **90.000 millones**

## Mi eleccion

Elijo la **opcion 2**: hace unas 270 veces menos operaciones que la 1. Como no se puede duplicar la memoria, tengo que ordenar en el mismo lugar (por ejemplo con QuikSort), no con MergeSortt, que necesita otro arreglo

## Cuando cambiaria de opinion

Si hubiera 18 consultas o menos, me conviene la opcion 1: recorrer 18 veces cuesta unos 5,4 millones y ordenar cuesta unos 5,5 millones. Con 19 o mas gana la opcion 2. (Sale de igualar q × n = n log n + q log n, que da q ≈ 18)

## Apoyo de mi medicion

En P1.2, con n = 6.400 la solucion por pares tardo 1849,56 ms y mi cura 0,98 ms. Al duplicar n, la cuadratica se multiplicaba por ~x4 y la lineal por ~x2, o sea que lo cuadratico crece mucho mas rapido (por eso la opcion 3 es la peor)