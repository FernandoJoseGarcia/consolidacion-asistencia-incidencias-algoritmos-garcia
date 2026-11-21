# Inventario de operaciones de mi caso

Proceso: consolidación diaria de asistencia, permisos y vacaciones (H1).

## 1. Datos que guarda mi proceso

| Dato                              | Hoy                       | Peor mes                             |
|-----------------------------------|---------------------------|--------------------------------------|
| Empleados                         | 300                       | 300                                  |
| Marcaciones por empleado          | 4                         | 4                                    |
| Registros por día                 | 1.200                     | 1.200                                |
| Registros por semana              | 6.000                     | 6.000                                |
| Registros por mes                 | 26.400 (22 días)          | 37.200 (simulado: 300 × 4 × 31 días) |
| Historial de un año (26.400 × 12) | 316.800 al cierre del año | igual                                |

Son 4 tablas (asistencia, empleado, vacaciones y permisos) relacionadas por el código del empleado. El reporte de asistencia sale **sin ordenar** del reloj checador y el archivo va creciendo cada día (historial anual). Los permisos y vacaciones son pocos comparados con las marcaciones. Los números son los mismos de `c6`.

## 2. Operaciones y cuáles hago más veces

| Operación         | Qué hace en mi proceso                        | Veces por día      | Frecuencia |
|-------------------|-----------------------------------------------|--------------------|------------|
| Buscar por clave  | buscar el código de cada marcación            | 1.200              | Muchas     |
| Contar por clave  | contar marcaciones por empleado               | 1.200              | Muchas     |
| Insertar          | agregar las marcaciones del día               | 1.200              | Muchas     |
| Menor o siguiente | primera marcación del empleado y la siguiente | 600                | Medias     |
| Recorrer en orden | reporte por código, fecha y hora              | 1                  | Pocas      |
| Rango             | reporte por rango de fechas                   | 1 por semana o mes | Pocas      |
| Borrar            | quitar una marcación duplicada                | casi ninguna       | Pocas      |

Lo que más hago es **buscar y contar por código de empleado**: unas 2.400 operaciones por día (1.200 + 1.200). Las 1.200 búsquedas son las de `c4`: una por marcación, buscando el código en empleados, permisos y vacaciones. El conteo es lo que hoy hace CONTAR.SI.CONJUNTO, y el menor o el siguiente son 300 empleados × 2 (la primera marcación y la siguiente). Recorrer en orden (una vez por día), pedir un rango y borrar se hacen pocas veces.

## 3. Qué estructura la resuelve barato y cuál sufre

| Operación         | Arreglo         | Lista      | Tabla hash    | BST balanceado | Quién sufre           |
|-------------------|-----------------|------------|---------------|----------------|-----------------------|
| Buscar por clave  | O(n)            | O(n)       | O(1) promedio | O(log n)       | Arreglo y lista       |
| Contar por clave  | O(n)            | O(n)       | O(1) promedio | O(log n)       | Arreglo y lista       |
| Insertar          | O(1) amortizado | O(1)       | O(1) promedio | O(log n)       | Ninguna               |
| Borrar un valor   | O(n)            | O(n)       | O(1) promedio | O(log n)       | Arreglo y lista       |
| Menor o siguiente | O(n)            | O(n)       | O(n)          | O(log n)       | Hash (sin orden)      |
| Rango de valores  | O(n)            | O(n)       | O(n)          | O(log n + k)   | Hash (sin orden)      |
| Recorrer en orden | O(n log n)      | O(n log n) | O(n log n)    | O(n)           | Hash, arreglo y lista |

En la tabla hash y en el árbol la clave es el código de empleado. k es cuántos valores devuelve el rango. Recorrer en orden cuesta O(n log n) en las otras tres porque primero hay que ordenar, y O(n) en el árbol porque ya guarda las claves en orden. El árbol balanceado se agrega por la clase 9: se reacomoda solo para no degenerar.

## Ajuste con lo visto en clase: ¿necesito orden o rangos?

Casi no. Lo que más hago es buscar y contar por clave exacta (2.400 operaciones por día), y para eso el árbol cuesta O(log n) y la tabla hash O(1) en promedio. El orden aparece al recorrer el reporte en orden (una vez por día, y lo resuelvo con el sort de `c6`, que ordena un día de registros en menos de 1 ms), en el menor o el siguiente (sobre 4 marcaciones por empleado) y en el reporte por rango de fechas, que se pide una vez por semana o mes. Si ese reporte se pidiera todos los días o con muchos datos, ahí sí pensaría en el árbol balanceado, que da el rango en O(log n + k).

## 4. Mi conclusión

La estructura que más me conviene es la **tabla hash con el código de empleado como clave**, porque lo que más hago es buscar y contar por código.

Hoy, con BUSCARV y CONTAR.SI.CONJUNTO, cada búsqueda o conteo recorre toda la lista (O(n)), y como se repite por cada marcación el total es O(n²): solo contar son 1.200 × 1.200 = 1.440.000 comparaciones por día. Con la tabla hash cada operación cuesta O(1) en promedio, o sea unas 2.400 operaciones por día.

Lo que sufre la tabla hash es el **rango**, el **menor o el siguiente** y **recorrer en orden**, porque no guarda orden. Pero el rango se pide pocas veces (una vez por semana o mes), el menor o el siguiente se hace sobre solo 4 marcaciones por empleado y recorrer en orden pasa una vez por día, así que no pesan. Para que siga en O(1), usaría una función hash que reparta bien los códigos (con una mala, buscar vuelve a O(n)) y la tabla se agrandaría sola cuando se llena (rehash), porque el historial crece todos los días.

Esto se complementa con lo que elegí en otras tareas: en `c4`, ordenar una lista para buscar con binaria, y en `c6`, ordenar el reporte con el sort de Python para dejar las marcaciones de cada empleado juntas y en orden de fecha y hora (retardos y omisiones). La tabla hash se encarga de buscar y contar por código sin recorrer la lista.

## Resumen

```
Datos       : 300 empleados, 1.200 registros por día, 37.200 en el peor mes (simulado), reporte sin ordenar
Lo que más  : buscar y contar por código de empleado (2.400 operaciones por día)
Hoy         : BUSCARV + CONTAR.SI.CONJUNTO ... O(n²)
Estructura  : tabla hash (clave = código de empleado) ... O(1) promedio
Sufre       : rango, menor o siguiente y recorrer en orden (la tabla hash no guarda orden), pero se hacen pocas veces
Orden/rango : no son lo principal; si pesaran, árbol balanceado (O(log n + k))
```