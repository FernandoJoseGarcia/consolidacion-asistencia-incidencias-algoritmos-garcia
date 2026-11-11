import math

datos = [3, 8, 12, 19, 25, 31, 40, 47]  # 8 numeros, ordenados


def busqueda_binaria(lista, buscado):
    inicio = 0
    fin = len(lista) - 1
    pasos = 0

    while inicio <= fin:
        medio = (inicio + fin) // 2
        pasos += 1
        print(f"  Paso {pasos}: inicio={inicio}, fin={fin}, medio={medio} -> miro {lista[medio]}")

        if lista[medio] == buscado:
            print(f"  Encontrado en el indice {medio}")
            return pasos
        if lista[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    print("  No esta: inicio > fin, me doy cuenta aca")
    return pasos


# Punto 1: buscar el 31
print("Buscando el 31:")
pasos_31 = busqueda_binaria(datos, 31)
print(f"Total: {pasos_31} pasos\n")

# Punto 2: buscar el 5 (no esta)
print("Buscando el 5:")
pasos_5 = busqueda_binaria(datos, 5)
print(f"Total: {pasos_5} pasos\n")

# Punto 3: maximo de pasos para 1.000 y 1.000.000 de datos
# Maximo de pasos = parte entera de log2(n) + 1
for n in [8, 1_000, 1_000_000]:
    maximo = int(math.log2(n)) + 1
    print(f"Con {n:,} datos: como maximo {maximo} pasos")