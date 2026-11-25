# Jose Fernando Garcia Sanchez

# I3 Medir

## Estado de la medicion

No alcance a terminar el codigo de la medicion a tiempo, asi que no tengo la tabla de tiempos ni la medicion con 1.000 paquetes. Entregue las dos clases (ingenua y mejorada) y los casos de prueba

Lo que pensaba medir era 1 corrida de calentamiento, 3 corridas medidas y promedio, en cuatro tamanos n, n+2, n+4 y n+6, comprobando que las dos den la misma ganancia

## Lo que esperaba

La ingenua es O(n * 2^n), asi que cada 2 paquetes mas deberia tardar cerca de x4. La mejorada es O(n*W), y como W crece poco con n, deberia crecer muy poco

Habria que tomar en cuenta el ruido de la laptop, porque la mejorada tarda menos de 1 ms

## 1.000 paquetes y capacidad 10.000

No lo medi

Son 1.000*10.000 = 10.000.000 de pasoss la ingenua no se puede ejecutar con 1.000 paquetes porque serian 2^1000 combinaciones.

## Y si la capacidad fuera 1.000.000.000 kg

Mi solucion cuesta O(n*W), y W seria enorme

- Pasos: 1.000*1.000.000.000=1.000.000.000.000, un billon de pasos,, A unos 10 millones de pasos por segundo en Python serian 100.000 segundos, unas 28 horas (estimacion)ç

- Memoria: la lista de ganancias tendria 1.000.000.000 de casillas (unos 8 GB) y la marca de decisiones 1.000*1.000.000.000=1 TB. No es soprotado

Entonces con esa capacidad mi solucion no sirve. Si la suma de todos los kg es menor que la capacidad, se puede bajar W a esa suma y llevar todo. Y si hay pocos paquetes, la fuerza bruta (n* 2^n) puede ser mejor que n*W.