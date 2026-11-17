# Jose Fernando Garcia Sanchez

# Variante A:registro de carnets
import random
import time

N_BASE = 800
CORRIDAS = 3


# Solucion LENTA
def hay_repetidos_por_pares(carnets):
    for i in range(len(carnets)):
        for j in range(i + 1, len(carnets)):
            if carnets[i] == carnets[j]:
                return True
    return False


# Mi CURA
def hay_repetidos_curado(carnets):
    vistos = set()
    for c in carnets:
        if c in vistos:
            return True
        vistos.add(c)
    return False


# Peor caso:lista SIN repetidos, desordenada
def generar_sin_repetidos(n, semilla=42):
    datos = list(range(n))
    random.Random(semilla).shuffle(datos)
    return datos


# Los cinco casos de prueba
CASOS = [
    ([7, 3, 9, 3, 5], True, "repetiudo en el medio"),
    ([7, 3, 9, 4, 5], False, "sin repetidos"),
    ([], False, "lista vacia"),
    ([8], False, "un solo elemento"),
    ([4, 1, 2, 6, 4], True, "repetid en los extremos"),
]

for datos, esperado, que in CASOS:
    copia = datos[:]
    assert hay_repetidos_por_pares(datos) == esperado, f"lenta falla: {que}"
    assert hay_repetidos_curado(datos) == esperado, f"curada falla: {que}"
    assert datos == copia, f"la cura modifico la lista: {que}"
print("Casos de prueba OK (las dos pasan los cinco y no modifican la lista)\n")


# Medicion con protocolo
def medir(funcion, datos):
    funcion(datos)
    tiempos = []
    for _ in range(CORRIDAS):
        inicio = time.perf_counter()
        funcion(datos)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)
    return sum(tiempos) / len(tiempos)


tamanos = [N_BASE, 2 * N_BASE, 4 * N_BASE, 8 * N_BASE]
resultados = []
for n in tamanos:
    datos = generar_sin_repetidos(n)
    print(f"midiendo n = {n:,} ...", flush=True)
    resultados.append((medir(hay_repetidos_por_pares, datos), medir(hay_repetidos_curado, datos)))

# Tablaa
print("\nTiempo promedio (ms), peor caso (lista sin repetidos)\n")
print(f"| {'n':>6} | {'por pares':>10} | {'x anterior':>10} | {'curada':>8} | {'x anterior':>10} |")
print(f"|{'-' * 8}|{'-' * 12}|{'-' * 12}|{'-' * 10}|{'-' * 12}|")
for i, (n, (t_lenta, t_curada)) in enumerate(zip(tamanos, resultados)):
    if i == 0:
        r1 = r2 = "-"
    else:
        r1 = f"x{t_lenta / resultados[i - 1][0]:.2f}"
        r2 = f"x{t_curada / resultados[i - 1][1]:.2f}"
    print(f"| {n:>6,} | {t_lenta:>10.2f} | {r1:>10} | {t_curada:>8.3f} | {r2:>10} |")

peor = max((t, n) for n, (t, _) in zip(tamanos, resultados))
print(f"\nPeor tiempo medido: {peor[0]:.2f} ms con n = {peor[1]:,} (solucion por pares)")