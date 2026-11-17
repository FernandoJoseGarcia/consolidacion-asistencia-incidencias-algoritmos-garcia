# Jose Fernando Garcia Sanchez

# P1.1 — Analizar

## a) Fragmentos

**F1: O(n).** Un solo ciclo que da n vueltass

**F2: O(n²).** Dos ciclos anidados: hace unas n × n / 2 comparaciones

**F3: O(log n).** k se divide a la mitad en cada vuelta

**F4: O(n log n).** El ciclo de afuera da n vueltas y el de adentro (k se duplica) da log n

## b) Recurrencias

**(i) T(n) = 3T(n/2) + n**
- a = 3, b = 2, d = 1, b^d = 2
- Comparacion: a > b^d (3 > 2)
- Forma: **n^(log₂ 3) ≈ n^1,585**
- Dominan las hojas..

**(ii) T(n) = T(n/2) + n²**
- a = 1, b = 2, d = 2, b^d = 4
- Comparacion: a < b^d (1 < 4)
- Forma: **n²**
- Domina la raiz.