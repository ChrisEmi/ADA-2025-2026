def multiplicacion_primaria(a:str, b:str) -> str:
    n1 = [int(x) for x in a if x.isdigit()]
    n2 = [int(y) for y in b if y.isdigit()]
    
    resultado = [0] * (len(n1) + len(n2))
    for i in range(len(n1) - 1, -1, -1):
        for j in range(len(n2) - 1, -1, -1):
            producto = n1[i] * n2[j]
            if producto >= 9:
                acarreos = producto // 10
                producto = producto % 10


            suma = producto + resultado[i + j + 1]
            resultado[i + j + 1] = suma % 10
            resultado[i + j] += suma // 10

