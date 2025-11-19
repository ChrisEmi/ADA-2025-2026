import random

MOCHILA_ARTICULOS = 300

def generar_articulos(n):
    pesos = []
    costos = []

    for _ in range(n):
        peso = random.randint(1, 100)
        valor = random.randint(10, 500)
        pesos.append(peso)
        costos.append(valor)
    return pesos, costos

def mochila(pesos, costos, capacidad):
    objeto = []

    for i in range(len(pesos)):
        ratio = costos[i] / pesos[i]
        objeto.append((ratio, pesos[i], costos[i]))

    objeto.sort(reverse=True)
    total_valor = 0

    for ratio, peso, valor in objeto:
        if capacidad >= peso:
            capacidad -= peso
            total_valor += valor
        else:
            fraccion = capacidad / peso
            total_valor += valor * fraccion
            break

    return total_valor

capacidad = MOCHILA_ARTICULOS
n = int(input("Ingrese la cantidad de artículos: "))

pesos, costos = generar_articulos(n)
print("Pesos de los artículos:", pesos)
print("Costos de los artículos:", costos)

valor_total = mochila(pesos, costos, capacidad)

print("Capacidad de la mochila:", capacidad)
print("Valor total en la mochila:", valor_total)