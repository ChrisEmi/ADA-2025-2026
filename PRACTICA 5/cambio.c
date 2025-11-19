#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<math.h>

void cambio(int dinero, int monto, int dar_cambio[]) {
    int monedas[] = {1, 5, 10, 25};
    int num_monedas = sizeof(monedas) / sizeof(monedas[0]), cambio = dinero - monto;

    for (int i = num_monedas - 1; i >= 0; i--) {
        int cantidad = floor(cambio / monedas[i]);
        if (cantidad > 0) {
            dar_cambio[i] = cantidad;
            cambio -= cantidad * monedas[i];
        } else {
            dar_cambio[i] = 0;
        }
    }
}

int main(int argc, char *argv[]) {
    int dinero, monto, n_dinero;

    printf("Ingrese la cantidad de valores a procesar: ");
    scanf("%d", &n_dinero);

    printf("Ingrese el monto a pagar: ");
    scanf("%d", &monto);

    int resultado[n_dinero][4];

    for (int i = 0; i < n_dinero; i++) {
        printf("Ingrese el dinero %d: ", i + 1);
        scanf("%d", &dinero);
        cambio(dinero, monto, resultado[i]);
        if (dinero < monto) {
            printf("El dinero no alcanza para el monto a pagar\n");
        } else {
            printf("Cambio para el monto %d:\n", monto);
            printf("Monedas de 25: %d\n", resultado[i][3]);
            printf("Monedas de 10: %d\n", resultado[i][2]);
            printf("Monedas de 5: %d\n", resultado[i][1]);
            printf("Monedas de 1: %d\n", resultado[i][0]);
        }
        
    }

    system("pause");
    return 0;
    
}