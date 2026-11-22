# Jose Fernando Garcia Sanchez

import heapq
import time

N_BASE = 2000
CORRIDAS = 3

#SOLUCION INGENUA
class ReceptorIngenuo:
    def __init__(self):
        self._lista = []
        self._llegadas = 0

    def registrar(self, pedido, plazo):
        self._lista.append((pedido, plazo, self._llegadas))
        self._llegadas += 1

    def preparar_siguiente(self):
        if len(self._lista) == 0:
            return None
        mejor = 0
        for i in range(1, len(self._lista)):
            p = self._lista[i]
            m = self._lista[mejor]
            if p[1] < m[1] or (p[1] == m[1] and p[2] < m[2]):
                mejor = i
        nombre = self._lista[mejor][0]
        self._lista.pop(mejor)
        return nombre

    def esta_pendiente(self, pedido):
        for p in self._lista:
            if p[0] == pedido:
                return True
        return False

    def pendientes(self):
        return len(self._lista)


#MI SOLUCION
class ReceptorMejorado:
    def __init__(self):
        self._heap = []
        self._pendientes = set()
        self._llegadas = 0

    def registrar(self, pedido, plazo):
        heapq.heappush(self._heap, (plazo, self._llegadas, pedido))
        self._pendientes.add(pedido)
        self._llegadas += 1

    def preparar_siguiente(self):
        if len(self._heap) == 0:
            return None
        plazo, llegada, nombre = heapq.heappop(self._heap)
        self._pendientes.remove(nombre)
        return nombre

    def esta_pendiente(self, pedido):
        return pedido in self._pendientes

    def pendientes(self):
        return len(self._pendientes)


#Prueba
GUION = [
    ("registrar", "Torta", 120, ""), ("registrar", "Galletas", 30, ""),
    ("registrar", "Pan", 120, ""), ("registrar", "Brazo", 60, ""),
    ("pendientes", "", 0, "4"),
    ("esta", "Galletas", 0, "True"), ("esta", "Flan", 0, "False"),
    ("preparar", "", 0, "Galletas"), ("esta", "Galletas", 0, "False"),
    ("preparar", "", 0, "Brazo"),
    ("registrar", "Alfajor", 30, ""),
    ("preparar", "", 0, "Alfajor"), ("preparar", "", 0, "Torta"), ("preparar", "", 0, "Pan"),
    ("preparar", "", 0, "(ninguno)"), ("pendientes", "", 0, "0"),
]


def ejecutar(r, op, arg, plazo):
    if op == "registrar":
        r.registrar(arg, plazo)
        return ""
    if op == "preparar":
        salio = r.preparar_siguiente()
        return "(ninguno)" if salio is None else salio
    if op == "esta":
        return str(r.esta_pendiente(arg))
    return str(r.pendientes())


def probar(titulo, r):
    bien = 0
    total = 0
    for op, arg, plazo, esperado in GUION:
        obtenido = ejecutar(r, op, arg, plazo)
        if op == "registrar":
            continue
        total += 1
        if obtenido == esperado:
            bien += 1
        else:
            print(f"   MAL en {op} {arg}: esperado {esperado}, obtuvo {obtenido}")
    print(f"{titulo}: {bien} de {total} pasos correctos")


probar("ReceptorIngenuo ", ReceptorIngenuo())
probar("ReceptorMejorado", ReceptorMejorado())


#La carga
def ejecutar_carga(r, n):
    for i in range(n):
        r.registrar("Q" + str(i), ((i * 6007) % 6 + 1) * 15)
    control = 0
    for i in range(n):
        control += len(r.preparar_siguiente())
    return control


def orden_de_salida(r, n):
    for i in range(n):
        r.registrar("Q" + str(i), ((i * 6007) % 6 + 1) * 15)
    return [r.preparar_siguiente() for _ in range(n)]


assert orden_de_salida(ReceptorIngenuo(), 1000) == orden_de_salida(ReceptorMejorado(), 1000), \
    "las doss deben dar el mismo orden"
print("Mismo orden de saliida en las dos (n = 1,000)\n")


#Medicion
def medir(fabrica, n):
    ejecutar_carga(fabrica(), n)
    tiempos = []
    for _ in range(CORRIDAS):
        r = fabrica()
        inicio = time.perf_counter()
        ejecutar_carga(r, n)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)
    return sum(tiempos) / len(tiempos)


tamanos = [N_BASE, 2 * N_BASE, 4 * N_BASE]
resultados = []
for n in tamanos:
    print(f"midienndo n = {n:,} ...", flush=True)
    resultados.append((medir(ReceptorIngenuo, n), medir(ReceptorMejorado, n)))

print("\nTiempo promedio (ms): n pedidos llegan y se preparn ls n\n")
print(f"| {'n':>6} | {'ingenuo':>10} | {'x anterior':>10} | {'mejorado':>9} | {'x anterior':>10} |")
print(f"|{'-' * 8}|{'-' * 12}|{'-' * 12}|{'-' * 11}|{'-' * 12}|")
for i, (n, (t_ing, t_mej)) in enumerate(zip(tamanos, resultados)):
    if i == 0:
        r1 = r2 = "-"
    else:
        r1 = f"x{t_ing / resultados[i - 1][0]:.2f}"
        r2 = f"x{t_mej / resultados[i - 1][1]:.2f}"
    print(f"| {n:>6,} | {t_ing:>10.2f} | {r1:>10} | {t_mej:>9.2f} | {r2:>10} |")

peor = max((t, n) for n, (t, _) in zip(tamanos, resultados))
print(f"\nPeor tiempo medidos: {peor[0]:.2f} ms con n = {peor[1]:,} (solucion ingenua)")