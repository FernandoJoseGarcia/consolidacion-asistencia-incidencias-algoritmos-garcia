# Jose Fernando Garcia Sanchez

# P2.3 Medir

Uso EjecutarCarga (llegan n pedidos y despues se preparan los n)

Uso Python 3.9, en una laptop

Protocolo: 1 corrida de calentamiento, 3 corridas medidas y promedio

## Resultados

**n = 2,000:** ingenuo 819.57 ms, mejorado 3.77 ms

**n = 4,000:** ingenuo 2477.83 ms (x3.02), mejorado 8.60 ms (x2.28)

**n = 8,000:** ingenuo 10686.54 ms (x4.31), mejorado 19.57 ms (x2.27)

## Conclusion

El ingenuo se comporta como O(n2) al duplicar n tarda mas o menos x4 (dio x3.02 y x4.31)

El mejorado se comporta como O(n log n) al duplicar n tarda un poco mas de x2 (dio x2.28 y x2.27). Con 8,000 pedidos el ingenuo es mas lento

Hay ruido medi en mi laptop y el x3.02 salio mas bajo de lo esperado