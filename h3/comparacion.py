# H3 - Comparacion: fuerza bruta contra programacion dinamica
# CASO ANALOGICO (no es el proceso real del proyecto):
# RRHH tiene un tiempo limitado para revisar incidencias. Cada incidencia tarda unos
# minutos en revisarse y tiene una gravedad. Se quiere la mayor gravedad total revisada
# sin pasarse del tiempo disponible (problema de la mochila).

import random
import time

TAMANOS = [18, 20, 22, 24]      # cantidad de incidencias (cada +2 la fuerza bruta tarda ~x4)
CORRIDAS = 3


# ---------- VORAZ: elige primero la de mas gravedad por minuto (solo para el contraejemplo) ----------
def voraz(incidencias, tiempo):
    orden = sorted(incidencias, key=lambda x: x[1] / x[0], reverse=True)
    gravedad = 0
    for t, g in orden:
        if t <= tiempo:
            tiempo -= t
            gravedad += g
    return gravedad


# ---------- FUERZA BRUTA: prueba todas las combinaciones (2^n) ----------
# Para cada incidencia hay dos opciones: no revisarla o revisarla (si cabe).
def fuerza_bruta(incidencias, tiempo, i=0):
    if i == len(incidencias):
        return 0
    t, g = incidencias[i]
    sin = fuerza_bruta(incidencias, tiempo, i + 1)                  # no la reviso
    con = 0
    if t <= tiempo:
        con = g + fuerza_bruta(incidencias, tiempo - t, i + 1)      # la reviso
    return max(sin, con)


# ---------- DINAMICA: tabla (incidencias x minutos) ----------
# tabla[i][m] = mayor gravedad usando las primeras i incidencias con m minutos.
# Cada celda se calcula una sola vez usando celdas ya calculadas.
def dinamica(incidencias, tiempo):
    n = len(incidencias)
    tabla = [[0] * (tiempo + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, g = incidencias[i - 1]
        for m in range(tiempo + 1):
            tabla[i][m] = tabla[i - 1][m]                  # no la reviso
            if t <= m:
                con = g + tabla[i - 1][m - t]              # la reviso
                if con > tabla[i][m]:
                    tabla[i][m] = con
    return tabla[n][tiempo]


# ---------- Pruebas chicas ----------
# (tiempo, gravedad): A = (10, 60), B = (20, 100), C = (30, 120), con 50 minutos
EJEMPLO = [(10, 60), (20, 100), (30, 120)]
assert voraz(EJEMPLO, 50) == 160, "el voraz deberia dar 160"
assert fuerza_bruta(EJEMPLO, 50) == 220, "fuerza bruta deberia dar 220"
assert dinamica(EJEMPLO, 50) == 220, "dinamica deberia dar 220"
assert fuerza_bruta([], 50) == 0 and dinamica([], 50) == 0, "sin incidencias"
assert fuerza_bruta([(60, 90)], 50) == 0 and dinamica([(60, 90)], 50) == 0, "ninguna cabe"
print("Pruebas OK. Ejemplo A, B, C con 50 minutos:")
print(f"   voraz = {voraz(EJEMPLO, 50)}, fuerza bruta = {fuerza_bruta(EJEMPLO, 50)}, dinamica = {dinamica(EJEMPLO, 50)}")
print("   (el voraz se equivoca: toma A y B y ya no cabe C)\n")


# ---------- Datos: n incidencias con tiempo de 10 a 60 min y gravedad de 1 a 100 ----------
def generar(n, semilla=7):
    azar = random.Random(semilla)
    return [(azar.randint(10, 60), azar.randint(1, 100)) for _ in range(n)]


# El tiempo disponible es la mitad del tiempo que tomaria revisar todas las incidencias
def tiempo_disponible(incidencias):
    return sum(t for t, g in incidencias) // 2


# ---------- Medicion con protocolo ----------
def medir(funcion, incidencias, tiempo):
    funcion(incidencias, tiempo)                    # 1 corrida de calentamiento (no se cuenta)
    tiempos = []
    for _ in range(CORRIDAS):
        inicio = time.perf_counter()
        funcion(incidencias, tiempo)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)       # a milisegundos
    return sum(tiempos) / len(tiempos)


resultados = []
for n in TAMANOS:
    datos = generar(n)
    tiempo = tiempo_disponible(datos)
    mejor_fb = fuerza_bruta(datos, tiempo)
    mejor_din = dinamica(datos, tiempo)
    assert mejor_fb == mejor_din, "las dos deben dar el mismo resultado"
    print(f"midiendo n = {n} ...", flush=True)
    resultados.append((tiempo, mejor_din, medir(fuerza_bruta, datos, tiempo), medir(dinamica, datos, tiempo)))

print("\nTiempo promedio (ms). Minutos disponibles = mitad del tiempo total de las incidencias\n")
print(f"| {'n':>3} | {'minutos':>7} | {'gravedad':>8} | {'fuerza bruta':>12} | {'x anterior':>10} | {'dinamica':>8} | {'x anterior':>10} |")
print(f"|{'-' * 5}|{'-' * 9}|{'-' * 10}|{'-' * 14}|{'-' * 12}|{'-' * 10}|{'-' * 12}|")
for i, (n, (minutos, grav, t_fb, t_din)) in enumerate(zip(TAMANOS, resultados)):
    if i == 0:
        r1 = r2 = "-"
    else:
        r1 = f"x{t_fb / resultados[i - 1][2]:.2f}"
        r2 = f"x{t_din / resultados[i - 1][3]:.2f}"
    print(f"| {n:>3} | {minutos:>7} | {grav:>8} | {t_fb:>12.2f} | {r1:>10} | {t_din:>8.3f} | {r2:>10} |")

peor = max((r[2], n) for n, r in zip(TAMANOS, resultados))
print(f"\nPeor tiempo medido: {peor[0]:.2f} ms con n = {peor[1]} (fuerza bruta)")