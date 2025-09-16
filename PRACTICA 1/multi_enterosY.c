#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int caracterToMatriz(char* c, int arr[]);

int main() {
    char a[100], b[100];
    int x[100], y[100], multiplicacion, acarreo = 0, suma, sumas = 0, multiplicaciones = 0, pA, pB;

    printf("Ingrese el primer numero: ");
    scanf("%s", a);
    printf("Ingrese el segundo numero: ");
    scanf("%s", b);

    int aLongitud = caracterToMatriz(a, x);
    int bLongitud = caracterToMatriz(b, y);

    int resultado[aLongitud + bLongitud];

    for(int i = 0; i < aLongitud + bLongitud; i++) {
        resultado[i] = 0;
    } // Inicializar el arreglo resultado a 0


    for(int i = 0; i < aLongitud; i++) {
        for(int j = 0; j < bLongitud; j++) {
            multiplicacion = x[i] * y[j]; // Realizar la multiplicacion
            multiplicaciones++; // Contar la multiplicaciones

            pA = i + j;
            pB = i + j + 1;
            suma = resultado[pB] + multiplicacion; // Sumar el resultado previo con la nueva multiplicacion
            if (resultado[pB] != 0 || multiplicacion != 0) { // Contar la suma solo si alguno de los dos es no cero
                sumas++;
            }

            resultado[pB] = suma % 10; // Guardar el dígito en la posición correcta
            acarreo = suma / 10; // Calcular el acarreo
            if (acarreo > 0) { // Si hay acarreo, sumarlo a la posición anterior
                resultado[pA] += acarreo;
                sumas++; 
                acarreo = 0;
            }
        }
    }

    printf("Resultado de la multiplicacion:\n");

    int primerIndex = 0; // Encontrar el primer índice no cero
    while (primerIndex < aLongitud + bLongitud - 1 && resultado[primerIndex] == 0) primerIndex++;
    for (int i = primerIndex; i < aLongitud + bLongitud; i++) { // Imprimir desde el primer índice no cero
        printf("%d", resultado[i]);
    }

    printf("\nCantidad de sumas: %d\n", sumas);
    printf("Cantidad de multiplicaciones: %d\n", multiplicaciones);

    system("pause");

    return 0;
}

int caracterToMatriz(char* c, int arr[]) {
    int i = 0;
    while (c[i] != '\0') {
        arr[i] = c[i] - '0';
        i++;
    }
    return i;
}