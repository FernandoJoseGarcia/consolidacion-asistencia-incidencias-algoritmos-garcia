import math
from functools import lru_cache

# T(n) = a * T(n/b) + n^d
# (nombre, a, b, d)
recurrencias = [
    ("(a) 2T(n/2) + 1", 2, 2, 0),
    ("(b)  T(n/2) + n", 1, 2, 1),
    ("(c) 4T(n/2) + n", 4, 2, 1),
    ("(d) 2T(n/2) + n^2", 2, 2, 2),
    ("MergeSort (clase)", 2, 2, 1),   # ejemplo de la clase: a = b^d
]


def forma(a, b, d):
    """Teorema maestro de bolsillo: compara a con b^d."""
    bd = b ** d
    if a < bd:
        return "la raiz", ("n" if d == 1 else f"n^{d}")
    if a == bd:
        if d == 0:
            return "todos los pisos", "log n"
        if d == 1:
            return "todos los pisos", "n log n"
        return "todos los pisos", f"n^{d} log n"
    exp = math.log(a, b)
    return "las hojas", ("n" if abs(exp - 1) < 1e-9 else f"n^{exp:.3g}")


def comparacion(a, b, d):
    bd = b ** d
    if a < bd:
        return "a < b^d"
    if a == bd:
        return "a = b^d"
    return "a > b^d"


def evaluar(a, b, d, n):
    """Calcula T(n) con T(1) = 1, aplicando la recurrencia tal cual."""
    @lru_cache(maxsize=None)
    def T(m):
        if m <= 1:
            return 1
        return a * T(m / b) + m ** d
    return T(n)


# ---------- Tabla ----------
N = 1024   # se compara T(2N) con T(N), con N potencia de 2
print(f"| {'recurrencia':<18} | {'a':>1} | {'b':>1} | {'d':>1} | {'b^d':>3} | {'comparacion':<11} | {'domina':<15} | {'forma':<8} | {'T(2n)/T(n)':>10} |")
print(f"|{'-' * 20}|{'-' * 3}|{'-' * 3}|{'-' * 3}|{'-' * 5}|{'-' * 13}|{'-' * 17}|{'-' * 10}|{'-' * 12}|")
for nombre, a, b, d in recurrencias:
    domina, f = forma(a, b, d)
    ratio = evaluar(a, b, d, 2 * N) / evaluar(a, b, d, N)
    print(f"| {nombre:<18} | {a:>1} | {b:>1} | {d:>1} | {b ** d:>3} | {comparacion(a, b, d):<11} | {domina:<15} | {f:<8} | {'x' + format(ratio, '.2f'):>10} |")

print("\nComprobacion: si la forma es n el ratio da ~x2, si es n^2 da ~x4,")
print("y si es n log n da un poco mas de x2.")