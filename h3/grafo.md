# ¿Mi caso se puede modelar como un grafo?

Caso: consolidación diaria de asistencia, permisos y vacaciones.

## Respuesta

**NO.**

## Por qué

Un grafo sirve cuando importan las conexiones entre las cosas: llegar de un nodo a otro, el camino con menos tramos, saber quiénes están conectados o qué depende de qué.

Mi proceso no hace ninguna de esas preguntas. Cada día busca el código de cada marcación en las tablas de empleados, permisos y vacaciones, y cuenta cuántas marcaciones tiene cada empleado. Son consultas por código, no recorridos por conexiones: ningún dato depende de otro ni hace falta un camino. Por eso se resuelve con tablas hash y no con un grafo.