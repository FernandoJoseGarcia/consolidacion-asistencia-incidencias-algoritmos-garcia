import time

N_BASE = 200_000
CORRIDAS = 5


def busqueda_lineal(lista, buscado):
    for x in lista:
        if x == buscado:
            return True
    return False


def medir(n):
    lista = list(range(n))
    buscado = -1

    busqueda_lineal(lista, buscado)

    tiempos = []
    for _ in range(CORRIDAS):
        inicio = time.perf_counter()
        busqueda_lineal(lista, buscado)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)

    return sum(tiempos) / len(tiempos)


tamanos = [N_BASE, 4 * N_BASE, 16 * N_BASE]
promedios = [medir(n) for n in tamanos]

lineas = []
lineas.append("| n | tiempo promedio (ms) | ratio vs anterior |")
lineas.append("|---|---|---|")
for i, (n, t) in enumerate(zip(tamanos, promedios)):
    ratio = "-" if i == 0 else f"x{t / promedios[i - 1]:.2f}"
    lineas.append(f"| {n:,} | {t:.2f} | {ratio} |")

tabla = "\n".join(lineas)
print(tabla)

with open("tabla_mediciones.md", "w", encoding="utf-8") as f:
    f.write(tabla + "\n")