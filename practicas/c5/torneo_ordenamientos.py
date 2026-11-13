import random
import time

TAMANOS = [10_000, 20_000, 40_000, 80_000]
CORRIDAS = 3


# ---------- Cuadratico: insercion ----------
def insercion(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


# ---------- n log n: MergeSort ----------
def mergesort(a):
    mergear(a, [0] * len(a), 0, len(a) - 1)


def mergear(a, tmp, ini, fin):
    if ini >= fin:
        return
    medio = (ini + fin) // 2
    mergear(a, tmp, ini, medio)
    mergear(a, tmp, medio + 1, fin)
    i, j, k = ini, medio + 1, ini
    while i <= medio and j <= fin:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i <= medio:
        tmp[k] = a[i]
        i += 1
        k += 1
    while j <= fin:
        tmp[k] = a[j]
        j += 1
        k += 1
    for k in range(ini, fin + 1):
        a[k] = tmp[k]


# ---------- n log n: QuickSort (pivote al medio) ----------
def quicksort(a):
    rapido(a, 0, len(a) - 1)


def rapido(a, ini, fin):
    if ini >= fin:
        return
    medio = (ini + fin) // 2
    a[medio], a[fin] = a[fin], a[medio]   # el pivote va al final
    pivote = a[fin]
    i = ini
    for j in range(ini, fin):
        if a[j] < pivote:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[fin] = a[fin], a[i]           # el pivote queda en su lugar
    rapido(a, ini, i - 1)
    rapido(a, i + 1, fin)


# ---------- Cuarto competidor: el sort de Python ----------
def sort_python(a):
    a.sort()


algoritmos = [
    ("insercion", insercion),
    ("mergesort", mergesort),
    ("quicksort", quicksort),
    ("sort Python", sort_python),
]


def esta_ordenado(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def medir(funcion, base):
    # calentamiento con una lista chica (no se cuenta)
    funcion(base[:1000])

    tiempos = []
    for _ in range(CORRIDAS):
        copia = base[:]                      # lista desordenada nueva
        inicio = time.perf_counter()
        funcion(copia)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)  # a milisegundos

    assert esta_ordenado(copia), "el arreglo NO quedo ordenado"
    return sum(tiempos) / len(tiempos)


# ---------- Verificar que ordenan, ANTES de medir ----------
random.seed(1)
prueba = random.sample(range(10_000), 2_000)
for nombre, funcion in algoritmos:
    copia = prueba[:]
    funcion(copia)
    assert copia == sorted(prueba), f"{nombre} no ordena bien"
print("Verificacion OK: los 4 algoritmos dejan el arreglo ordenado\n")

# ---------- Torneo ----------
resultados = {nombre: [] for nombre, _ in algoritmos}
for n in TAMANOS:
    base = random.sample(range(n * 10), n)
    for nombre, funcion in algoritmos:
        print(f"midiendo {nombre} con n = {n:,} ...", flush=True)
        resultados[nombre].append(medir(funcion, base))

# ---------- Tablas ----------
print("\nTiempo promedio (ms)\n")
encabezado = f"| {'n':>8} |" + "".join(f" {nombre:>12} |" for nombre, _ in algoritmos)
print(encabezado)
print("|" + "-" * 10 + "|" + ("-" * 14 + "|") * len(algoritmos))
for i, n in enumerate(TAMANOS):
    fila = f"| {n:>8,} |"
    for nombre, _ in algoritmos:
        fila += f" {resultados[nombre][i]:>12.1f} |"
    print(fila)

print("\nRatio vs el tamano anterior (al duplicar n)\n")
print(encabezado)
print("|" + "-" * 10 + "|" + ("-" * 14 + "|") * len(algoritmos))
for i, n in enumerate(TAMANOS):
    fila = f"| {n:>8,} |"
    for nombre, _ in algoritmos:
        if i == 0:
            ratio = "-"
        else:
            ratio = f"x{resultados[nombre][i] / resultados[nombre][i - 1]:.2f}"
        fila += f" {ratio:>12} |"
    print(fila)