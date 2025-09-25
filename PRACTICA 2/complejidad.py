import time
import tracemalloc
import numpy as np
import random

import matplotlib.pyplot as plt

# Algoritmos a analizar

def busqueda_lineal(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

def busqueda_binaria(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def burbuja(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def fibonacci(n):
    if n == 0: return [0]
    elif n == 1: return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Función para medir tiempo y memoria
def medir_algoritmo(func, *args):
    tracemalloc.start()
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (end_time - start_time), peak / 1024  # tiempo en segundos, memoria en KB

# Tamaños de prueba
sizes = [100, 500, 1000, 2000, 4000, 8000]
resultados = {
    'Busqueda Lineal': {'tiempo': [], 'memoria': []},
    'Busqueda Binaria': {'tiempo': [], 'memoria': []},
    'Burbuja': {'tiempo': [], 'memoria': []},
    'Fibonacci': {'tiempo': [], 'memoria': []}
}

for n in sizes:
    arr = random.sample(range(n*10), n)
    arr_ordenado = sorted(arr)
    x = arr[random.randint(0, n-1)]

    # Busqueda Lineal
    t, m = medir_algoritmo(busqueda_lineal, arr, x)
    resultados['Busqueda Lineal']['tiempo'].append(t)
    resultados['Busqueda Lineal']['memoria'].append(m)

    # Busqueda Binaria (requiere arreglo ordenado)
    t, m = medir_algoritmo(busqueda_binaria, arr_ordenado, x)
    resultados['Busqueda Binaria']['tiempo'].append(t)
    resultados['Busqueda Binaria']['memoria'].append(m)

    # Burbuja
    t, m = medir_algoritmo(burbuja, arr)
    resultados['Burbuja']['tiempo'].append(t)
    resultados['Burbuja']['memoria'].append(m)

    # Fibonacci (n es el tamaño de la serie)
    t, m = medir_algoritmo(fibonacci, n)
    resultados['Fibonacci']['tiempo'].append(t)
    resultados['Fibonacci']['memoria'].append(m)

# Graficar resultados
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
for key in resultados:
    plt.plot(sizes, resultados[key]['tiempo'], marker='o', label=key)
plt.xlabel('Tamaño del arreglo / n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Comparación de tiempo de ejecución')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
for key in resultados:
    plt.plot(sizes, resultados[key]['memoria'], marker='o', label=key)
plt.xlabel('Tamaño del arreglo / n')
plt.ylabel('Memoria pico (KB)')
plt.title('Comparación de uso de memoria')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Imprimir resultados en consola
print("\nResultados de tiempo y memoria por algoritmo:")
for key in resultados:
    print(f"\nAlgoritmo: {key}")
    print("Tamaños:", sizes)
    print("Tiempos (s):", [f"{t:.6f}" for t in resultados[key]['tiempo']])
    print("Memoria pico (KB):", [f"{m:.2f}" for m in resultados[key]['memoria']])