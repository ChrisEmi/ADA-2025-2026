#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<math.h>
#include <time.h>
#define MOCHILA_ARTICULOS 300


struct articulo {
    int peso;
    int valor;
    double ratio;
};

void llenar_pesos(int n_articulos, int pesos[]) {
    for (int i = 0; i < n_articulos; i++) {
        pesos[i] = rand() % 100 + 1;
    }
}
void llenar_costos(int n_articulos, int costos[]) {
    for (int i = 0; i < n_articulos; i++) {
        costos[i] = rand() % (n_articulos * 10) + 1;
    }
}

void crear_articulos(struct articulo articulos[], int pesos[], int costos[], int n_articulos) {
    for (int i = 0; i < n_articulos; i++) {
        articulos[i].peso = pesos[i];
        articulos[i].valor = costos[i];
        articulos[i].ratio = (double)costos[i] / pesos[i];
    }
}

double mochila(int pesos[], int costos[], int n_articulos, int capacidad_mochila) {
    struct articulo articulos[n_articulos];
    crear_articulos(articulos, pesos, costos, n_articulos);
    for (int i = 0; i < n_articulos - 1; i++) {
        for (int j = 0; j < n_articulos - i - 1; j++) {
            if (articulos[j].ratio < articulos[j + 1].ratio) {
                struct articulo temp = articulos[j];
                articulos[j] = articulos[j + 1];
                articulos[j + 1] = temp;
            }
        }
    }
    double valor_total = 0.0;
    int peso_actual = 0;

    for(int i = 0; i < n_articulos; i++) {
        if (peso_actual + articulos[i].peso <= capacidad_mochila) {
            peso_actual += articulos[i].peso;
            valor_total += articulos[i].valor;
        } else {
            int espacio_restante = capacidad_mochila - peso_actual;
            valor_total += articulos[i].ratio * espacio_restante;
            break;
        }
    }
    return valor_total;
}

int main(int argc, char *argv[]) {
    int peso,costo,n_articulos,capacidad_mochila;

    printf("Ingrese la cantidad de valores la mochila: ");
    scanf("%d", &n_articulos);
    srand(time(NULL));

    int pesos[n_articulos];
    int costos[n_articulos];
    capacidad_mochila = MOCHILA_ARTICULOS;

    llenar_costos(n_articulos, costos);
    llenar_pesos(n_articulos, pesos);

    for (int i = 0; i < n_articulos; i++) {
        printf("Articulo %d - Peso: %d, Costo: %d\n", i + 1, pesos[i], costos[i]);
    }

    double valor_maximo = mochila(pesos, costos, n_articulos, capacidad_mochila);

    printf("\nCapacidad de la mochila: %d\n", capacidad_mochila);
    printf("El valor maximo que se puede obtener es: %.2f\n", valor_maximo);


    system("pause");
    return 0;
    
}