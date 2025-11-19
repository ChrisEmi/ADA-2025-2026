#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<math.h>
#include <time.h>

struct Evento {
    int inicio;
    int fin;
    int duracion;
};

void random_evento(struct Evento* evento, int max_inicio, int max_duracion) {
    srand(time(NULL) + rand());
    evento->inicio = rand() % max_inicio;
    evento->duracion = (rand() % max_duracion) + 1; 
    evento->fin = evento->inicio + evento->duracion;
}

int maximo_eventos(struct Evento eventos[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (eventos[j].fin > eventos[j + 1].fin) {
                struct Evento temp = eventos[j];
                eventos[j] = eventos[j + 1];
                eventos[j + 1] = temp;
            }
        }
    }
    int contador = 0;
    int ultimo_fin = -1;

    for (int i = 0; i < n; i++) {
        if (eventos[i].inicio >= ultimo_fin) {
            contador++;
            ultimo_fin = eventos[i].fin;
        }
    }
    return contador;
}

int main(int argc, char *argv[]) {
    int n_eventos = 10;
    struct Evento eventos[n_eventos];

    for (int i = 0; i < n_eventos; i++) {
        random_evento(&eventos[i], 12, 6);
        printf("Evento %d: Inicio: %d, Fin: %d, Duracion: %d\n", i + 1, eventos[i].inicio, eventos[i].fin, eventos[i].duracion);
    }

    int max_eventos = maximo_eventos(eventos, n_eventos);
    printf("Numero maximo de eventos: %d\n", max_eventos);

    system("pause");
    return 0;
    
}