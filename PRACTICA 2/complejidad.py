import time
import tracemalloc
import random
import sys

def ejecutar_todas_las_pruebas_python():
    """
    Funcion principal para ejecutar todas las pruebas de algoritmos en Python.
    """
    # Aumentar el limite de recursion para Merge Sort con n=10^5
    # Es necesario para evitar un RecursionError con arreglos grandes.
    sys.setrecursionlimit(2000)

    # --- 1. Implementacion de Busqueda Lineal ---
    def busqueda_lineal(arreglo, objetivo):
        for indice in range(len(arreglo)):
            if arreglo[indice] == objetivo:
                return indice
        return -1

    # --- 2. Implementacion de Busqueda Binaria ---
    def busqueda_binaria(arreglo, objetivo):
        bajo, alto = 0, len(arreglo) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            if arreglo[medio] == objetivo:
                return medio
            elif arreglo[medio] < objetivo:
                bajo = medio + 1
            else:
                alto = medio - 1
        return -1

    # --- 3. Implementacion de Ordenamiento Burbuja ---
    def ordenamiento_burbuja(arreglo):
        n = len(arreglo)
        for i in range(n):
            intercambio = False
            for j in range(0, n-i-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                    intercambio = True
            if not intercambio:
                break
        return arreglo

    # --- 4. Implementacion de Ordenamiento por Mezcla ---
    def ordenamiento_mezcla(arreglo):
        if len(arreglo) > 1:
            medio = len(arreglo) // 2
            izquierda = arreglo[:medio]
            derecha = arreglo[medio:]
            
            ordenamiento_mezcla(izquierda)
            ordenamiento_mezcla(derecha)
            
            i = j = k = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    arreglo[k] = izquierda[i]; i += 1
                else:
                    arreglo[k] = derecha[j]; j += 1
                k += 1
            
            while i < len(izquierda):
                arreglo[k] = izquierda[i]; i += 1; k += 1
            
            while j < len(derecha):
                arreglo[k] = derecha[j]; j += 1; k += 1
        return arreglo

    # --- 5. Implementacion de Fibonacci Recursivo ---
    def fibonacci_recursivo(n):
        if n <= 1:
            return n
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


    # Pruebas de Busqueda Lineal
    print("\n--- 1. Busqueda Lineal ---")
    print(f"{'Tamano (n)':<15} | {'Tiempo (ms)':<15} | {'Pico Memoria (KiB)':<20}")
    print("-" * 55)
    for n in [10**3, 10**4, 10**5]:
        arreglo = list(range(n)); objetivo = n - 1 
        inicio_tiempo = time.perf_counter()
        busqueda_lineal(arreglo, objetivo)
        fin_tiempo = time.perf_counter()
        tiempo_transcurrido = (fin_tiempo - inicio_tiempo) * 1000
        tracemalloc.start()
        busqueda_lineal(arreglo, objetivo)
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{n:<15,} | {tiempo_transcurrido:<15.4f} | {pico / 1024:<20.4f}")
    
    # Pruebas de Busqueda Binaria
    print("\n--- 2. Busqueda Binaria ---")
    print(f"{'Tamano (n)':<15} | {'Tiempo (ms)':<15} | {'Pico Memoria (KiB)':<20}")
    print("-" * 55)
    for n in [10**3, 10**4, 10**5]:
        arreglo = list(range(n)); objetivo = n - 1
        inicio_tiempo = time.perf_counter()
        busqueda_binaria(arreglo, objetivo)
        fin_tiempo = time.perf_counter()
        tiempo_transcurrido = (fin_tiempo - inicio_tiempo) * 1000
        tracemalloc.start()
        busqueda_binaria(arreglo, objetivo)
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{n:<15,} | {tiempo_transcurrido:<15.4f} | {pico / 1024:<20.4f}")

    # Pruebas de Ordenamiento Burbuja
    print("\n--- 3. Ordenamiento por Burbuja ---")
    print(f"{'Tamano (n)':<15} | {'Tiempo (ms)':<15} | {'Pico Memoria (KiB)':<20}")
    print("-" * 55)
    for n in [10**3, 10**4]: # 10^5 es demasiado lento
        arreglo = list(range(n, 0, -1))
        inicio_tiempo = time.perf_counter()
        ordenamiento_burbuja(arreglo.copy())
        fin_tiempo = time.perf_counter()
        tiempo_transcurrido = (fin_tiempo - inicio_tiempo) * 1000
        tracemalloc.start()
        ordenamiento_burbuja(arreglo.copy())
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{n:<15,} | {tiempo_transcurrido:<15.4f} | {pico / 1024:<20.4f}")

    # Pruebas de Ordenamiento por Mezcla
    print("\n--- 4. Ordenamiento por Mezcla ---")
    print(f"{'Tamano (n)':<15} | {'Tiempo (ms)':<15} | {'Pico Memoria (KiB)':<20}")
    print("-" * 55)
    for n in [10**3, 10**4, 10**5]:
        arreglo = [random.randint(0, n) for _ in range(n)]
        inicio_tiempo = time.perf_counter()
        ordenamiento_mezcla(arreglo.copy())
        fin_tiempo = time.perf_counter()
        tiempo_transcurrido = (fin_tiempo - inicio_tiempo) * 1000
        tracemalloc.start()
        ordenamiento_mezcla(arreglo.copy())
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{n:<15,} | {tiempo_transcurrido:<15.4f} | {pico / 1024:<20.4f}")

    # Pruebas de Fibonacci Recursivo
    print("\n--- 5. Fibonacci Recursivo ---")
    print(f"{'Valor (n)':<15} | {'Tiempo (ms)':<15} | {'Pico Memoria (KiB)':<20}")
    print("-" * 55)
    for n in range(1, 21):
        inicio_tiempo = time.perf_counter()
        fibonacci_recursivo(n)
        fin_tiempo = time.perf_counter()
        tiempo_transcurrido = (fin_tiempo - inicio_tiempo) * 1000
        tracemalloc.start()
        fibonacci_recursivo(n)
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Imprimir solo una muestra para no saturar la salida
        if n <= 5 or n % 5 == 0:
            print(f"{n:<15} | {tiempo_transcurrido:<15.4f} | {pico / 1024:<20.4f}")

# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    ejecutar_todas_las_pruebas_python()