import random
import time

N = 1_000_000      # tamano del arreglo ordenado
CLAVES = 1_000     # claves a buscar (todas existen)
CORRIDAS = 3


def busqueda_lineal(lista, buscado):
    for x in lista:
        if x == buscado:
            return True
    return False


def busqueda_binaria(lista, buscado):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == buscado:
            return True
        if lista[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False


def medir(funcion, lista, claves):
    # calentamiento con pocas claves (no se cuenta)
    for k in claves[:10]:
        funcion(lista, k)

    tiempos = []
    for _ in range(CORRIDAS):
        inicio = time.perf_counter()
        for k in claves:
            funcion(lista, k)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)  # a milisegundos
    return sum(tiempos) / len(tiempos)


# ---------- Datos ----------
random.seed(1)
desordenada = random.sample(range(10_000_000), N)
ordenada = sorted(desordenada)                 # arreglo ordenado
claves = random.sample(ordenada, CLAVES)       # claves que SI existen

# ---------- Verificar antes de medir ----------
assert all(busqueda_binaria(ordenada, k) for k in claves), "binaria no encuentra todas"
assert all(busqueda_lineal(ordenada, k) for k in claves[:20]), "lineal no encuentra"
print("Verificacion OK: las claves existen y ambas busquedas las encuentran")
print(f"n = {N:,} | {CLAVES:,} claves | {CORRIDAS} corridas\n")

# ---------- Medicion ----------
print("midiendo busqueda lineal (puede tardar) ...", flush=True)
t_lineal = medir(busqueda_lineal, ordenada, claves)
print("midiendo busqueda binaria ...", flush=True)
t_binaria = medir(busqueda_binaria, ordenada, claves)
cociente = t_lineal / t_binaria

print(f"\n| {'algoritmo':<10} | {'tiempo promedio (ms)':>20} |")
print(f"|{'-' * 12}|{'-' * 22}|")
print(f"| {'lineal':<10} | {t_lineal:>20.2f} |")
print(f"| {'binaria':<10} | {t_binaria:>20.2f} |")
print(f"\ncociente lineal / binaria = x{cociente:,.0f}")

# ---------- Para las dos lineas: cuesta ordenar? ----------
tiempos_orden = []
for _ in range(CORRIDAS):
    copia = desordenada[:]
    inicio = time.perf_counter()
    copia.sort()
    fin = time.perf_counter()
    tiempos_orden.append((fin - inicio) * 1000)
t_ordenar = sum(tiempos_orden) / len(tiempos_orden)

ahorro_por_busqueda = (t_lineal - t_binaria) / CLAVES
print(f"\ncosto de ordenar el arreglo una vez: {t_ordenar:.2f} ms")
print(f"ahorro por busqueda (lineal - binaria): {ahorro_por_busqueda:.3f} ms")
print(f"ordenar se paga a partir de ~{t_ordenar / ahorro_por_busqueda:.1f} busquedas")