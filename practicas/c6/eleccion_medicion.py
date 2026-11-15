import random
import time

# (cantidad de registros, que representa)
TAMANOS = [
    (300, "empleados"),
    (1_200, "un dia"),
    (6_000, "una semana"),
    (26_400, "un mes"),
    (37_200, "peor mes (simulado)"),   # 300 empleados x 4 marcaciones x 31 dias
]
CORRIDAS = 3


# ---------- Candidato A: insercion ----------
def insercion(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


# ---------- Candidato B: MergeSort ----------
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


# ---------- Candidato C: el sort de Python ----------
def sort_python(a):
    a.sort()


algoritmos = [
    ("insercion", insercion),
    ("mergesort", mergesort),
    ("sort Python", sort_python),
]


def crear_reporte(n):
    """Reporte de asistencia simulado, SIN ordenar.
    Cada registro es un numero: codigo (9001-9300), dia (1-31) y minuto del dia.
    Ordenar el numero equivale a ordenar por codigo, luego dia y luego hora."""
    registros = []
    for _ in range(n):
        codigo = random.randint(9001, 9300)
        dia = random.randint(1, 31)
        minuto = random.randint(0, 1439)
        registros.append(codigo * 100_000 + dia * 1_440 + minuto)
    return registros


def esta_ordenado(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def medir(funcion, base):
    funcion(base[:300])                    # calentamiento (no se cuenta)
    tiempos = []
    for _ in range(CORRIDAS):
        copia = base[:]                    # reporte desordenado nuevo
        inicio = time.perf_counter()
        funcion(copia)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)  # a milisegundos
    assert esta_ordenado(copia), "el arreglo NO quedo ordenado"
    return sum(tiempos) / len(tiempos)


# ---------- Verificar que ordenan, ANTES de medir ----------
random.seed(1)
prueba = crear_reporte(2_000)
for nombre, funcion in algoritmos:
    copia = prueba[:]
    funcion(copia)
    assert copia == sorted(prueba), f"{nombre} no ordena bien"
print("Verificacion OK: los 3 candidatos dejan el reporte ordenado\n")

# ---------- Medicion ----------
resultados = []
for n, que in TAMANOS:
    base = crear_reporte(n)
    fila = []
    for nombre, funcion in algoritmos:
        print(f"midiendo {nombre} con n = {n:,} ({que}) ...", flush=True)
        fila.append(medir(funcion, base))
    resultados.append(fila)

# ---------- Tabla ----------
print("\nTiempo promedio (ms) para ordenar el reporte\n")
print(f"| {'n':>7} | {'que representa':<20} | {'insercion':>11} | {'mergesort':>11} | {'sort Python':>11} | {'ins/merge':>9} | {'merge/py':>8} |")
print(f"|{'-' * 9}|{'-' * 22}|{'-' * 13}|{'-' * 13}|{'-' * 13}|{'-' * 11}|{'-' * 10}|")
for (n, que), (t_ins, t_mer, t_py) in zip(TAMANOS, resultados):
    c1 = f"x{t_ins / t_mer:.1f}"
    c2 = f"x{t_mer / t_py:.1f}"
    print(f"| {n:>7,} | {que:<20} | {t_ins:>11.2f} | {t_mer:>11.2f} | {t_py:>11.2f} | {c1:>9} | {c2:>8} |")