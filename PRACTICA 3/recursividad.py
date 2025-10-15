import time
import tracemalloc
import sys

# Mostrar la pila de llamadas recursivas: guardaremos el camino actual en una lista
# y lo imprimiremos cuando entremos y salgamos de cada llamada.

def medir(func):
    """Decorator para medir tiempo y memoria de una funcion (solo para llamadas no recursivas)."""
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"\n== Resultado de {func.__name__} ==")
        print(f"Tiempo transcurrido: {(t1-t0)*1000:.6f} ms")
        print(f"Memoria pico: {peak/1024:.3f} KiB")
        return result
    return wrapper

# 1) Suma de digitos

# iterativa
@medir
def suma_digitos_iterativa(n):
    n = abs(int(n))
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

# recursiva con traza de pila
def suma_digitos_recursiva(n, pila=None):
    if pila is None:
        pila = []
    pila.append(n)
    print(f"Entrando: suma_digitos_recursiva({n}), pila: {pila}")
    n = abs(int(n))
    if n < 10:
        print(f"Saliendo: suma_digitos_recursiva({n}) = {n}, pila: {pila}")
        pila.pop()
        return n
    resultado = n % 10 + suma_digitos_recursiva(n // 10, pila)
    print(f"Saliendo: suma_digitos_recursiva({n}) = {resultado}, pila: {pila}")
    pila.pop()
    return resultado

# 2) Invertir cadena

@medir
def invertir_iterativa(s):
    return s[::-1]

def invertir_recursiva(s, pila=None):
    if pila is None:
        pila = []
    pila.append(s)
    print(f"Entrando: invertir_recursiva({s!r}), pila: {pila}")
    if s == "" or len(s) == 1:
        print(f"Saliendo: invertir_recursiva({s!r}) = {s!r}, pila: {pila}")
        pila.pop()
        return s
    resultado = invertir_recursiva(s[1:], pila) + s[0]
    print(f"Saliendo: invertir_recursiva({s!r}) = {resultado!r}, pila: {pila}")
    pila.pop()
    return resultado

# 3) Busqueda binaria (iterativa y recursiva)
@medir
def busqueda_binaria_iterativa(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

def busqueda_binaria_recursiva(arr, objetivo, bajo=0, alto=None, pila=None):
    if pila is None:
        pila = []
    if alto is None:
        alto = len(arr) - 1
    pila.append((bajo, alto))
    print(f"Entrando: busqueda_binaria_recursiva(bajo={bajo}, alto={alto}), pila: {pila}")
    if bajo > alto:
        print(f"Saliendo: busqueda_binaria_recursiva(bajo={bajo}, alto={alto}) = -1, pila: {pila}")
        pila.pop()
        return -1
    medio = (bajo + alto) // 2
    if arr[medio] == objetivo:
        print(f"Saliendo: busqueda_binaria_recursiva(bajo={bajo}, alto={alto}) = {medio}, pila: {pila}")
        pila.pop()
        return medio
    elif arr[medio] < objetivo:
        resultado = busqueda_binaria_recursiva(arr, objetivo, medio+1, alto, pila)
    else:
        resultado = busqueda_binaria_recursiva(arr, objetivo, bajo, medio-1, pila)
    print(f"Saliendo: busqueda_binaria_recursiva(bajo={bajo}, alto={alto}) = {resultado}, pila: {pila}")
    pila.pop()
    return resultado

# 4) Potenciacion (iterativa y recursiva) - manejando exponentes enteros no negativos
@medir
def potencia_iterativa(a, b):
    a = float(a)
    b = int(b)
    res = 1.0
    for _ in range(b):
        res *= a
    return res

def potencia_recursiva(a, b, pila=None):
    if pila is None:
        pila = []
    pila.append(b)
    print(f"Entrando: potencia_recursiva(a={a}, b={b}), pila: {pila}")
    a = float(a)
    b = int(b)
    if b == 0:
        print(f"Saliendo: potencia_recursiva(a={a}, b={b}) = 1.0, pila: {pila}")
        pila.pop()
        return 1.0
    if b == 1:
        print(f"Saliendo: potencia_recursiva(a={a}, b={b}) = {a}, pila: {pila}")
        pila.pop()
        return a
    mitad = potencia_recursiva(a, b//2, pila)
    if b % 2 == 0:
        resultado = mitad * mitad
    else:
        resultado = mitad * mitad * a
    print(f"Saliendo: potencia_recursiva(a={a}, b={b}) = {resultado}, pila: {pila}")
    pila.pop()
    return resultado


# Runner que ejecuta cada implementacion, mide y muestra resultados

def runner_demo():
    print("Ejecutando demostracion de funciones iterativas y recursivas\n")

    # 1) Suma de dígitos
    n = 123456789
    t0 = time.perf_counter()
    res_iter = suma_digitos_iterativa(n)
    t1 = time.perf_counter()
    tracemalloc.start()
    t0r = time.perf_counter()
    res_rec = suma_digitos_recursiva(n, pila=[])
    t1r = time.perf_counter()
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\n{:<30} | {:<15} | {:<15} | {:<15}".format('Funcion', 'Modo', 'Tiempo (ms)', 'Mem. pico (KiB)'))
    print('_'*70)
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('suma_digitos', 'iterativa', (t1-t0)*1000, 0.0))
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('suma_digitos', 'recursiva', (t1r-t0r)*1000, peak/1024))

    # 2) Invertir cadena
    s = 'hola mundo'
    t0 = time.perf_counter()
    res_iter = invertir_iterativa(s)
    t1 = time.perf_counter()
    t0r = time.perf_counter()
    res_rec = invertir_recursiva(s, pila=[])
    t1r = time.perf_counter()
    print("\n{:<30} | {:<15} | {:<15} | {:<15}".format('Funcion', 'Modo', 'Tiempo (ms)', 'Mem. pico (KiB)'))
    print('_'*70)
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('invertir_cadena', 'iterativa', (t1-t0)*1000, 0.0))
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('invertir_cadena', 'recursiva', (t1r-t0r)*1000, 0.0))

    # 3) Búsqueda binaria
    arr = list(range(0, 1000))
    objetivo = 777
    t0 = time.perf_counter()
    idx_iter = busqueda_binaria_iterativa(arr, objetivo)
    t1 = time.perf_counter()
    tracemalloc.start()
    t0r = time.perf_counter()
    idx_rec = busqueda_binaria_recursiva(arr, objetivo, pila=[])
    t1r = time.perf_counter()
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\n{:<30} | {:<15} | {:<15} | {:<15}".format('Funcion', 'Modo', 'Tiempo (ms)', 'Mem. pico (KiB)'))
    print('_'*70)
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('busqueda_binaria', 'iterativa', (t1-t0)*1000, 0.0))
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('busqueda_binaria', 'recursiva', (t1r-t0r)*1000, peak/1024))

    # 4) Potenciación
    a, b = 2, 20
    t0 = time.perf_counter()
    pot_iter = potencia_iterativa(a, b)
    t1 = time.perf_counter()
    tracemalloc.start()
    t0r = time.perf_counter()
    pot_rec = potencia_recursiva(a, b, pila=[])
    t1r = time.perf_counter()
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\n{:<30} | {:<15} | {:<15} | {:<15}".format('Funcion', 'Modo', 'Tiempo (ms)', 'Mem. pico (KiB)'))
    print('_'*70)
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('potenciacion', 'iterativa', (t1-t0)*1000, 0.0))
    print('{:<30} | {:<15} | {:<15.6f} | {:<15.3f}'.format('potenciacion', 'recursiva', (t1r-t0r)*1000, peak/1024))

    print('\nResultados concretos:')
    print(f"suma_digitos(n={n}): iter={res_iter}, rec={res_rec}")
    print(f"invertir_cadena(s='{s}'): iter={res_iter!r}, rec={res_rec!r}")
    print(f"busqueda_binaria(obj={objetivo}): iter={idx_iter}, rec={idx_rec}")
    print(f"potenciacion({a}^{b}): iter={pot_iter}, rec={pot_rec}")


if __name__ == "__main__":
    runner_demo()

