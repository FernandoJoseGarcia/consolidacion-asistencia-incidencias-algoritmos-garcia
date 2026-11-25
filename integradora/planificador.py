# Jose Fernando Garcia Sanchez

import random
import time

CORRIDAS = 3


class PlanificadorIngenuo:
    def __init__(self):
        self._elegidos = []

    def elegir(self, paquetes, capacidad):
        n = len(paquetes)
        mejor = 0
        mejor_mascara = 0
        for mascara in range(1 << n):
            kg = 0
            ganancia = 0
            for i in range(n):
                if mascara & (1 << i):
                    kg += paquetes[i][1]
                    ganancia += paquetes[i][2]
            if kg <= capacidad and ganancia > mejor:
                mejor = ganancia
                mejor_mascara = mascara
        self._elegidos = [paquetes[i][0] for i in range(n) if mejor_mascara & (1 << i)]
        return mejor, list(self._elegidos)

    def esta_en_el_viaje(self, codigo):
        return codigo in self._elegidos


class PlanificadorMejorado:
    def __init__(self):
        self._elegidos = set()

    def elegir(self, paquetes, capacidad):
        n = len(paquetes)
        mejor = [0] * (capacidad + 1)
        llevo = []
        for i in range(n):
            codigo, kg, ganancia = paquetes[i]
            fila = bytearray(capacidad + 1)
            for m in range(capacidad, kg - 1, -1):
                con = ganancia + mejor[m - kg]
                if con > mejor[m]:
                    mejor[m] = con
                    fila[m] = 1
            llevo.append(fila)
        self._elegidos = set()
        m = capacidad
        for i in range(n - 1, -1, -1):
            if llevo[i][m]:
                self._elegidos.add(paquetes[i][0])
                m -= paquetes[i][1]
        return mejor[capacidad], list(self._elegidos)

    def esta_en_el_viaje(self, codigo):
        return codigo in self._elegidos


CASOS = [
    ("el voraz se equivoca", [("P1", 10, 60), ("P2", 20, 100), ("P3", 30, 120)], 50, 220, ["P2", "P3"]),
    ("cuatro paquetes", [("P1", 2, 3), ("P2", 3, 4), ("P3", 4, 5), ("P4", 5, 6)], 8, 10, ["P2", "P4"]),
    ("capacidad cero", [("P1", 5, 10), ("P2", 7, 12)], 0, 0, []),
    ("sin paquetes", [], 30, 0, []),
    ("nada cabe", [("P1", 40, 90), ("P2", 50, 100)], 30, 0, []),
    ("entran todos", [("P1", 5, 10), ("P2", 7, 12), ("P3", 3, 4)], 100, 26, ["P1", "P2", "P3"]),
]

