#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

// --- 1. Implementacion de Busqueda Lineal ---
int busqueda_lineal(int arreglo[], int tam, int objetivo) {
    for (int i = 0; i < tam; i++) {
        if (arreglo[i] == objetivo) return i;
    }
    return -1;
}

// --- 2. Implementacion de Busqueda Binaria ---
int busqueda_binaria(int arreglo[], int tam, int objetivo) {
    int bajo = 0, alto = tam - 1;
    while (bajo <= alto) {
        int medio = bajo + (alto - bajo) / 2;
        if (arreglo[medio] == objetivo) return medio;
        if (arreglo[medio] < objetivo) bajo = medio + 1;
        else alto = medio - 1;
    }
    return -1;
}

// --- 3. Implementacion de Ordenamiento Burbuja ---
void intercambiar(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void ordenamiento_burbuja(int arreglo[], int tam) {
    for (int i = 0; i < tam - 1; i++) {
        int intercambio = 0;
        for (int j = 0; j < tam - i - 1; j++) {
            if (arreglo[j] > arreglo[j + 1]) {
                intercambiar(&arreglo[j], &arreglo[j + 1]);
                intercambio = 1;
            }
        }
        if (intercambio == 0) break;
    }
}

// --- 4. Implementacion de Ordenamiento por Mezcla ---
void mezcla(int arreglo[], int izq, int medio, int der) {
    int n1 = medio - izq + 1;
    int n2 = der - medio;
    int* I = (int*)malloc(n1 * sizeof(int));
    int* D = (int*)malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++) I[i] = arreglo[izq + i];
    for (int j = 0; j < n2; j++) D[j] = arreglo[medio + 1 + j];

    int i = 0, j = 0, k = izq;
    while (i < n1 && j < n2) {
        if (I[i] <= D[j]) arreglo[k++] = I[i++];
        else arreglo[k++] = D[j++];
    }
    while (i < n1) arreglo[k++] = I[i++];
    while (j < n2) arreglo[k++] = D[j++];
    free(I);
    free(D);
}

void ordenamiento_mezcla(int arreglo[], int izq, int der) {
    if (izq < der) {
        int medio = izq + (der - izq) / 2;
        ordenamiento_mezcla(arreglo, izq, medio);
        ordenamiento_mezcla(arreglo, medio + 1, der);
        mezcla(arreglo, izq, medio, der);
    }
}

// --- 5. Implementacion de Fibonacci Recursivo ---
long long fibonacci_recursivo(int n) {
    if (n <= 1) return n;
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2);
}


// --- Bloque Principal de Pruebas ---
int main() {
    setlocale(LC_ALL, "");
    srand(time(NULL)); // Semilla para números aleatorios

    // Pruebas Busqueda Lineal
    printf("\n--- 1. Busqueda Lineal ---\n");
    printf("| %-12s | %-15s | %-20s |\n", "Tamano (n)", "Tiempo (ms)", "Memoria Heap (KiB)");
    printf("|--------------|-----------------|----------------------|\n");
    int tamanos_busqueda[] = {1000, 10000, 100000};
    for (int i = 0; i < 3; i++) {
        int tam = tamanos_busqueda[i];
        int* arreglo = (int*)malloc(tam * sizeof(int));
        for (int j = 0; j < tam; j++) arreglo[j] = j;
        clock_t inicio = clock();
        busqueda_lineal(arreglo, tam, tam - 1);
        clock_t fin = clock();
        double tiempo_ms = ((double)(fin - inicio) / CLOCKS_PER_SEC) * 1000.0;
        printf("| %-12d | %-15.4f | %-20.4f |\n", tam, tiempo_ms, (double)(tam*sizeof(int))/1024.0);
        free(arreglo);
    }

    // Pruebas Busqueda Binaria
    printf("\n--- 2. Busqueda Binaria ---\n");
    printf("| %-12s | %-15s | %-20s |\n", "Tamano (n)", "Tiempo (ms)", "Memoria Heap (KiB)");
    printf("|--------------|-----------------|----------------------|\n");
    for (int i = 0; i < 3; i++) {
        int tam = tamanos_busqueda[i];
        int* arreglo = (int*)malloc(tam * sizeof(int));
        for (int j = 0; j < tam; j++) arreglo[j] = j;
        clock_t inicio = clock();
        busqueda_binaria(arreglo, tam, tam-1);
        clock_t fin = clock();
        double tiempo_ms = ((double)(fin - inicio) / CLOCKS_PER_SEC) * 1000.0;
        printf("| %-12d | %-15.4f | %-20.4f |\n", tam, tiempo_ms, (double)(tam*sizeof(int))/1024.0);
        free(arreglo);
    }
    
    // Pruebas Ordenamiento Burbuja
    printf("\n--- 3. Ordenamiento por Burbuja ---\n");
    printf("| %-12s | %-15s | %-20s |\n", "Tamano (n)", "Tiempo (ms)", "Memoria Heap (KiB)");
    printf("|--------------|-----------------|----------------------|\n");
    int tamanos_burbuja[] = {1000, 10000, 100000};
    for (int i = 0; i < 3; i++) {
        int tam = tamanos_burbuja[i];
        int* arreglo = (int*)malloc(tam * sizeof(int));
        for (int j = 0; j < tam; j++) arreglo[j] = tam - j; // Peor caso
        clock_t inicio = clock();
        ordenamiento_burbuja(arreglo, tam);
        clock_t fin = clock();
        double tiempo_ms = ((double)(fin - inicio) / CLOCKS_PER_SEC) * 1000.0;
        printf("| %-12d | %-15.4f | %-20.4f |\n", tam, tiempo_ms, (double)(tam*sizeof(int))/1024.0);
        free(arreglo);
    }

    // Pruebas Ordenamiento por Mezcla
    printf("\n--- 4. Ordenamiento por Mezcla ---\n");
    printf("| %-12s | %-15s | %-20s |\n", "Tamano (n)", "Tiempo (ms)", "Memoria Heap (KiB)");
    printf("|--------------|-----------------|----------------------|\n");
    for (int i = 0; i < 3; i++) {
        int tam = tamanos_busqueda[i];
        int* arreglo = (int*)malloc(tam * sizeof(int));
        for (int j = 0; j < tam; j++) arreglo[j] = rand() % tam;
        clock_t inicio = clock();
        ordenamiento_mezcla(arreglo, 0, tam - 1);
        clock_t fin = clock();
        double tiempo_ms = ((double)(fin - inicio) / CLOCKS_PER_SEC) * 1000.0;
        printf("| %-12d | %-15.4f | %-20.4f |\n", tam, tiempo_ms, (double)(tam*sizeof(int))/1024.0);
        free(arreglo);
    }

    // Pruebas Fibonacci
    printf("\n--- 5. Fibonacci Recursivo ---\n");
    printf("| %-10s | %-15s | %-25s |\n", "Valor (n)", "Tiempo (ms)", "Memoria Stack (Teorico)");
    printf("|------------|-----------------|---------------------------|\n");
    for (int n = 1; n <= 20; n++) {
        clock_t inicio = clock();
        fibonacci_recursivo(n);
        clock_t fin = clock();
        double tiempo_ms = ((double)(fin - inicio) / CLOCKS_PER_SEC) * 1000.0;
        if (n <= 5 || n % 5 == 0) {
             printf("| %-10d | %-15.4f | Crece linealmente con n |\n", n, tiempo_ms);
        }
    }

    return 0;
}