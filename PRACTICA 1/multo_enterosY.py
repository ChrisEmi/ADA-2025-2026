from os import system  # Importa la función system del módulo os para ejecutar comandos del sistema operativo

def multiplicacion_primaria(a:str, b:str) -> tuple:
    n1 = [int(x) for x in a if x.isdigit()]  # Convierte los dígitos de 'a' en una lista de enteros
    n2 = [int(y) for y in b if y.isdigit()]  # Convierte los dígitos de 'b' en una lista de enteros

    conteo = {
        "multiplicaciones": 0,  # Inicializa el contador de multiplicaciones
        "sumas": 0,             # Inicializa el contador de sumas
    }
    
    if '0' in (a, b):  # Si alguno de los números es '0', retorna '0' y el conteo
        return '0', conteo

    resultado = [0] * (len(n1) + len(n2))  # Crea una lista para almacenar el resultado de la multiplicación
    for i in range(len(n1) - 1, -1, -1):  # Recorre los dígitos de n1 de derecha a izquierda
        for j in range(len(n2) - 1, -1, -1):  # Recorre los dígitos de n2 de derecha a izquierda
            producto = n1[i] * n2[j]  # Multiplica los dígitos actuales
            conteo["multiplicaciones"] += 1  # Incrementa el contador de multiplicaciones

            p1os = i + j          # Calcula la posición para el acarreo
            p2os = i + j + 1      # Calcula la posición para el dígito actual

            if resultado[p2os] != 0 or producto != 0:  # Si hay valor previo o producto no es cero
                conteo["sumas"] += 1  # Incrementa el contador de sumas
            
            suma = producto + resultado[p2os]  # Suma el producto al valor actual en resultado
            
            acarreo = suma // 10  # Calcula el acarreo (decenas)

            if acarreo > 0:  # Si hay acarreo
                conteo["sumas"] += 1  # Incrementa el contador de sumas

            resultado[p1os] += acarreo  # Suma el acarreo a la posición correspondiente
            resultado[p2os] = suma % 10  # Guarda la unidad en la posición actual

    resultado_final = ''.join(map(str, resultado)).lstrip('0') or '0'  # Convierte la lista resultado a string y elimina ceros a la izquierda
    
    return resultado_final, conteo  # Retorna el resultado y el conteo de operaciones

if __name__ == "__main__":  # Si el script se ejecuta directamente
    a = input("Introduce el primer número: ")  # Solicita el primer número al usuario
    b = input("Introduce el segundo número: ")  # Solicita el segundo número al usuario
    
    resultado_calculado, total_operaciones = multiplicacion_primaria(a, b)  # Llama a la función de multiplicación
    
    print("Resultado:", resultado_calculado)  # Imprime el resultado de la multiplicación
    print("Número de multiplicaciones:", total_operaciones["multiplicaciones"])  # Imprime el número de multiplicaciones realizadas
    print("Número de sumas:", total_operaciones["sumas"])  # Imprime el número de sumas realizadas
    system("pause")  # Pausa la consola (solo en Windows)
