
def cambio(dinero, monto):
    cambio = monto - dinero
    if cambio < 0:
        return {}
    monedas = [1, 5, 10, 25]
    dar_cambio = {}
    
    for valor in monedas[::-1]:
        cantidad = cambio // valor
        if cantidad > 0:
            dar_cambio[valor] = cantidad
            cambio -= valor * cantidad
            
    return dar_cambio


n = int(input("Ingrese la cantidad de valores a procesar: "))
dinero = int(input("Ingrese el dinero entregado: "))

for i in range(n):
    monto = int(input(f"Ingrese el monto {i+1}: "))
    resultado = cambio(dinero, monto)
    if not resultado:
        print("No hay resultado")
    else:
        print("El cambio a entregar es:")
        for valor, cantidad in resultado.items():
            print(f"{cantidad} moneda(s) de {valor}")
    print()