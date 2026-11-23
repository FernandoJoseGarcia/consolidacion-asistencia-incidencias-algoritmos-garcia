# Estrategia de mi caso

Caso: consolidación diaria de asistencia, permisos y vacaciones.

## Respuesta

**NO.** Mi caso real no admite un voraz ni una dinámica.

## Por qué no, con las propiedades

Un voraz necesita dos propiedades: la elección voraz (existe una solución óptima que empieza con la elección que haría el voraz) y la subestructura óptima. Una dinámica necesita que los subproblemas se repitan y también la subestructura óptima.

| Propiedad                                    | Mi caso real |
|----------------------------------------------|--------------|
| Decisión que se repite, con algo a optimizar | No           |
| Elección voraz                               | No aplica    |
| Subestructura óptima                         | No aplica    |
| Subproblemas que se repiten                  | No           |

Mi proceso no tiene una decisión que se repita con un resultado que optimizar. Cada día cruza las marcaciones con empleados, permisos y vacaciones, y el resultado (faltas, retardos y omisiones justificadas) queda fijado por los datos: no elijo entre opciones ni hay algo que maximizar o minimizar. Cada marcación es independiente y se revisa una sola vez, así que no hay subproblemas que se repitan ni un óptimo que armar con óptimos de pedazos más chicos.

Lo que sí mejora mi proceso es la estructura de datos (la tabla hash del H2), no una estrategia voraz ni dinámica.

## Problema análogo (`comparacion.md`)

Como mi caso real no aplica, uso un **caso analógico**: elegir qué incidencias revisar con tiempo limitado, para maximizar la gravedad revisada. Ahí sí aplican las propiedades:

| Propiedad                   | Problema análogo         |
|-----------------------------|--------------------------|
| Elección voraz              | NO (contraejemplo abajo) |
| Subestructura óptima        | SÍ                       |
| Subproblemas que se repiten | SÍ                       |

**Contraejemplo del voraz:** A (10 minutos, gravedad 60), B (20, 100) y C (30, 120) con 50 minutos. El voraz toma primero la de más gravedad por minuto (A y B) y suma 160, pero lo mejor es B y C, con 220.

**Subestructura óptima:** lo mejor con las primeras i incidencias y m minutos se arma con lo mejor de pedazos más chicos (con la incidencia i o sin ella).

**Subproblemas que se repiten:** muchas combinaciones llegan al mismo punto (i, m), y la tabla lo calcula una sola vez.

Por eso la estrategia adecuada es la **programación dinámica**. En mi medición, con 24 incidencias fue unas 2.100 veces más rápida que la fuerza bruta.