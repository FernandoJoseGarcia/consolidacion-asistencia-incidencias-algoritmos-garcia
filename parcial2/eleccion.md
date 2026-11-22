# Josee Fernando Garcia Sanchez

# P2.1 Elegir

Caso: pedidos de una pasteleria
n = 120.000 por jornada

## Operaciones y estructura

**Registrar:** 120.000 veces. Heap. O(log n)

**PrepararSiguiente:** 120.000 veces. Heap. O(log n

**EstaPendiente:** 40.000 veces. Conjunto. O(1)

**Pendientes:** el mismo conjunto. O(1)

El heap saca primero el menor plazo (si empatan el que llego primeo) y el conjunto dice rapido si un pedido sigue pendiente

## Por que no la lista simple

La lista simple preparar son unos 120.000 por 120.000 entre 2 = 7.200 millones de pasos, y EstaPendiente hasta 40.000 por 120.000 = 4.800 millones

Total: unos 12.000 millones

Mi estructura log2 de 120.000 es cerca de 17(aprox), asi que registrar y preparar son unos 2 millones cada uno, mas 40.000 de EstaPendiente

Total: unos 4 millones

## Cuando cambiaria de opinion

Con pocos pedidos al dia, por ej 50, usaria la lista simple porque es mas facil. Tambien si hubiera que cancelar pedidos, porque sacar uno del medio del heap cuesta O(n).