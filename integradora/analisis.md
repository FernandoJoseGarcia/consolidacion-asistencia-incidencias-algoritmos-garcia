# Jose Fernando Garcia Sanchez

# I1 Analizar y elegir

## a) Costo de PlanificadorIngenuo.Elegir

El costo es O(n*2^n)

Cada paquete se lleva o no se lleva, o sea 2 opciones

Con n paquetes son 2*2* .. * 2 = 2^n combinaciones. Y en cada combinacion recorre los n paquetes para sumar peso y ganancia, entonces son 2^n*n pasos, entonces serian:

- n = 3 seria 8*3=24 paso
- n = 20 seroa 1.048.576*20=20.971.520 pasos, unos 21 millones
- n = 21 seria 2.097.152*21=44.040.192 pasos, mas del doble
- n = 30 seria 1.073.741.824*30=32.000 millones de pasos (aprox)

Cada paquete que se agrega duplica el trabajo, por eso se vuelve imposible mu rapido

## b) La recurrencia T(n) = 2 T(n-1) + 1

El teorema maestro sirve cuando el problema se divide entre b en cada llamada, como T(n/2). 
çAqui no se divide, solo se quita un paquete (n-1). Como no hay division, el teorema no se puede usar

Para saber cuanto cuesta calculamos  con T(0) = 1:

- T(1)=2*1+1=3
- T(2)=2*3+1=7
- T(3)=2*7+1=15

Los resultados son 2^2-1, 2^3-1 y 2^4-1, o sea que T(n)=2^(n+1)-1 

El costo es O(2^n), se duplica con cada paquete

## c) Voraz y estrategia

El voraz por ganancia por kg NO SIRVEE, lo estoy comprobando con el primer caso de las pruebas, con capacidad de 50 kg:

- P1 pesa 10 kg y gana 60 o sea 60/10=6 por kg
- P2 pesa 20 kg y gana 100 o sea 100/20=5 por kg
- P3 pesa 30 kg y gana 120 o sea 120/30=4 por kg

El voraz toma primero P1 y despues P2. Llevan 10+20=30 kg y ganan 60+100=160. 
P3 ya no entra, porque 30+30 = 60 y la capacidad es 50 (se pasa)

Lo mejor es llevar P2 y P3. Pesan 20+30=50 kg  justo lo que aguanta y ganan 100+120=220

Como 160 es menos que 220, el voraz se equivoca

**Estrategia que elijo es: programacion dinamica**

La idea es ir paquete por paquete y anotar cual es la mayor ganancia que puedo lograr con cada peso. Cada resultado se anota una sola vez y despues se reutiliza, en vez de calcularlo otra vez

Lo que se repite es la misma pregunta "con estos paquetes y este peso cual es la mayor ganancia" en la fuerza bruta se responde muchas veces, y asi se anota y se reutiliza.

Con el ejemplo de 50 kg:

- Con P1 con 10 kg o mas puedo ganar 60
- Con P1 y P2 con 20 kg gano 100 (solo P2) y con 30 kg gano 160 (P1 y P2)
- Con P3 para 50 kg tengo dos opciones. Si no llevo P3, gano 160. Si lo llevo, gano 120 mas lo mejor con los 20 kg que sobran, que es 100, o sea 220
- Me quedo con el mayor=220

El costo es O(n*W), con W la capacidad. Anoto una ganancia por cada paquete y por cada peso, y cada una cuesta 1 paso. Con 1.000 paquetes y capacidad 10.000 son 1.000*10.000=10.000.000 de pasos. La fuerza bruta seria 2^1000.

## d) Estructura para EstaEnElViaje

Usaria un conjunto (set) con los codigos de los paquetes elegidos. Buscar en un conjunto cuesta O(1), porque va directo al lugar sin recorrer

Recorrer la lista cuesta O(k), con k los paquetes elegidos, porque en el peor caso mira todos.

Si se consulta q veces, la lista hace q*k pasos y el conjunto solo q

Con 10.000 consultas y 500 paquetes elegidos serian:

- Lista: 10.000*500=5.000.000 de comparaciones
- Conjunto: 10.000*1=10.000 pasos

El conjunto es 5.000.000/10.000=500 veces mas rapido.