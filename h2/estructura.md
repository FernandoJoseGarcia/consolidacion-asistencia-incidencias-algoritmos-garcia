# Estructura de mi caso

Proceso: consolidación diaria de asistencia, permisos y vacaciones (H1).

## Estructura que elijo

Elijo la **tabla hash con el código de empleado como clave**. Voy a tener una tabla para los empleados, otra para los permisos y otra para las vacaciones, y un diccionario con un contador por código para las marcaciones. Así, cada marcación del reporte va directo al casillero de su empleado en vez de recorrer una lista.

## Costo de cada operación

| Operación         | Veces por día      | Costo         | Por qué                                 |
|-------------------|--------------------|---------------|-----------------------------------------|
| Buscar por clave  | 1.200              | O(1) promedio | la función hash va directo al casillero |
| Contar por clave  | 1.200              | O(1) promedio | un contador por código en su casillero  |
| Insertar          | 1.200              | O(1) promedio | calcula el casillero y agrega ahí       |
| Borrar un valor   | casi ninguna       | O(1) promedio | va directo al casillero y lo quita      |
| Menor o siguiente | 600                | O(n)          | sin orden, hay que mirar todos          |
| Rango de valores  | 1 por semana o mes | O(n)          | sin orden, hay que mirar todos          |
| Recorrer en orden | 1                  | O(n log n)    | hay que ordenar antes de recorrer       |

El costo O(1) es **en promedio**: depende de que la función hash reparta bien los códigos y de que la tabla no se llene. En el peor caso (una mala función que mande todo al mismo casillero) buscar vuelve a O(n).

El menor o el siguiente y el rango cuestan O(n) porque la tabla hash no guarda orden: para saber cuál es el menor hay que mirar todos los valores. Recorrer en orden cuesta O(n log n) porque primero hay que ordenar. En mi caso el menor o el siguiente se calcula sobre solo 4 marcaciones por empleado y recorrer en orden pasa una vez por día (con el sort de `c6`, ordenar un día de registros tarda menos de 1 ms), así que casi no pesan.

## Por qué la elijo

Lo que más hago es buscar y contar por clave exacta: 2.400 operaciones por día (1.200 búsquedas y 1.200 conteos). Hoy con CONTAR.SI.CONJUNTO solo contar son 1.200 × 1.200 = 1.440.000 comparaciones por día, y con la tabla hash son 1.200 accesos de costo O(1).

Mi medición lo confirma: contando marcaciones por empleado, con 1.200 datos la lista (ingenua) fue unas 355 veces más lenta que el hash y con 9.600 datos unas 1.225 veces más lenta, porque la lista es O(n²) y el hash es O(n).

Descarto el arreglo y la lista porque buscar y contar les cuesta O(n) cada vez. El árbol balanceado también sirve (buscar y contar en O(log n)), pero lo que me da de más es el orden y los rangos, que casi no uso, y por eso me quedo con el hash, que es más barato en lo que más hago.

## Lo que sufre y cómo lo manejo

- **Orden y rangos:** el rango de fechas se pide una vez por semana o mes, el menor o el siguiente es sobre 4 marcaciones y recorrer en orden pasa una vez por día, así que pagar O(n) u O(n log n) ahí es poco.
- **Función hash:** uso una que reparta bien los códigos de empleado (por ejemplo el código módulo la cantidad de casilleros) para no caer en el peor caso.
- **Tabla que se llena:** el factor de carga (datos entre casilleros) se mantiene por debajo de 0,75 y, si lo pasa, se duplican los casilleros y se reubican las claves (rehash). Ese costo ocasional se paga en promedio.
- **Memoria extra:** la tabla guarda casilleros vacíos, pero con 300 empleados es poco.

## Cuándo cambiaría

Si el reporte por rango de fechas se pidiera todos los días o sobre muchos datos, usaría un árbol balanceado, que da el rango en O(log n + k) porque guarda las claves en orden.