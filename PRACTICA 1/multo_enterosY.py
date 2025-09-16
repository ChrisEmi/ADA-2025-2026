def multiplicacion_primaria(a:str, b:str) -> tuple:
    n1 = [int(x) for x in a if x.isdigit()]
    n2 = [int(y) for y in b if y.isdigit()]

    conteo = {
        "multiplicaciones": 0,
        "sumas": 0,
    }
    
    if '0' in (a, b):
        return '0', conteo

    resultado = [0] * (len(n1) + len(n2))
    for i in range(len(n1) - 1, -1, -1):
        for j in range(len(n2) - 1, -1, -1):
            producto = n1[i] * n2[j]
            conteo["multiplicaciones"] += 1

            p1os = i + j
            p2os = i + j + 1

            if resultado[p2os] != 0 or producto != 0:
                conteo["sumas"] += 1
            
            suma = producto + resultado[p2os]
            
            acarreo = suma // 10

            if acarreo > 0:
                conteo["sumas"] += 1

            resultado[p1os] += acarreo
            resultado[p2os] = suma % 10


    resultado_final = ''.join(map(str, resultado)).lstrip('0') or '0'
    
    return resultado_final, conteo

if __name__ == "__main__":
    a = input("Introduce el primer número: ")
    b = input("Introduce el segundo número: ")
    
    resultado_calculado, total_operaciones = multiplicacion_primaria(a, b)
    
    print("Resultado:", resultado_calculado)
    print("Número de multiplicaciones:", total_operaciones["multiplicaciones"])
    print("Número de sumas:", total_operaciones["sumas"])