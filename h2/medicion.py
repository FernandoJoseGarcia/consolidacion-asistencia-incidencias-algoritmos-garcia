# H2 - Medicion: contar cuantas marcaciones tiene cada empleado
# Ingenua (lista, como CONTAR.SI.CONJUNTO) contra adecuada (tabla hash)

import random
import time

N_BASE = 1200      # un dia de marcaciones. Tamanos: n, 2n, 4n, 8n
CORRIDAS = 3


# ---------- INGENUA: con lista ----------
# Por cada marcacion recorro TODA la lista contando las que tienen el mismo codigo.
# Es lo que hace hoy CONTAR.SI.CONJUNTO en mi Excel: n marcaciones x n recorrido = O(n^2).
def contar_ingenua(marcaciones):
    resultado = []
    for m in marcaciones:
        cuenta = 0
        for otra in marcaciones:
            if otra == m:
                cuenta += 1
        resultado.append(cuenta)
    return resultado


# ---------- ADECUADA: con tabla hash (diccionario de Python) ----------
# Una sola pasada: guardo un contador por codigo y luego lo consulto.
# Cada acceso al diccionario cuesta O(1) en promedio: en total O(n).
def contar_hash(marcaciones):
    contador = {}
    for m in marcaciones:
        contador[m] = contador.get(m, 0) + 1
    return [contador[m] for m in marcaciones]


# ---------- Datos: reporte sin ordenar, codigos de empleado 9001 a 9300 ----------
def generar_marcaciones(n, semilla=42):
    azar = random.Random(semilla)
    return [azar.randint(9001, 9300) for _ in range(n)]


# ---------- Pruebas chicas: las dos deben dar lo mismo ----------
CASOS = [
    ([9001, 9002, 9001], [2, 1, 2], "un codigo repetido"),
    ([9001, 9002, 9003], [1, 1, 1], "todos distintos"),
    ([], [], "lista vacia"),
    ([9005], [1], "una sola marcacion"),
    ([9001, 9001, 9001, 9001], [4, 4, 4, 4], "las 4 marcaciones de un empleado"),
]

for datos, esperado, que in CASOS:
    assert contar_ingenua(datos) == esperado, f"ingenua falla: {que}"
    assert contar_hash(datos) == esperado, f"hash falla: {que}"
print("Casos de prueba OK (las dos dan lo mismo en los cinco casos)\n")


# ---------- Medicion con protocolo ----------
def medir(funcion, datos):
    funcion(datos)                              # 1 corrida de calentamiento (no se cuenta)
    tiempos = []
    for _ in range(CORRIDAS):
        inicio = time.perf_counter()
        funcion(datos)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)   # a milisegundos
    return sum(tiempos) / len(tiempos)


tamanos = [N_BASE, 2 * N_BASE, 4 * N_BASE, 8 * N_BASE]
resultados = []
for n in tamanos:
    datos = generar_marcaciones(n)
    assert contar_ingenua(datos) == contar_hash(datos), "las dos deben dar el mismo resultado"
    print(f"midiendo n = {n:,} ...", flush=True)
    resultados.append((medir(contar_ingenua, datos), medir(contar_hash, datos)))

# ---------- Tabla ----------
print("\nTiempo promedio (ms): contar marcaciones por empleado\n")
print(f"| {'n':>6} | {'ingenua':>10} | {'x anterior':>10} | {'hash':>8} | {'x anterior':>10} |")
print(f"|{'-' * 8}|{'-' * 12}|{'-' * 12}|{'-' * 10}|{'-' * 12}|")
for i, (n, (t_ing, t_hash)) in enumerate(zip(tamanos, resultados)):
    if i == 0:
        r1 = r2 = "-"
    else:
        r1 = f"x{t_ing / resultados[i - 1][0]:.2f}"
        r2 = f"x{t_hash / resultados[i - 1][1]:.2f}"
    print(f"| {n:>6,} | {t_ing:>10.2f} | {r1:>10} | {t_hash:>8.3f} | {r2:>10} |")

peor = max((t, n) for n, (t, _) in zip(tamanos, resultados))
print(f"\nPeor tiempo medido: {peor[0]:.2f} ms con n = {peor[1]:,} (solucion ingenua)")