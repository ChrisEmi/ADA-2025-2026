from datetime import datetime, timedelta

class Evento:
    def __init__(self, fecha_inicio, fecha_fin):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
    def duracion(self):
        return self.fecha_fin - self.fecha_inicio
    

def random_eventos(n, inicio, fin, duracion_min, duracion_max):
    import random
    eventos = []
    delta = fin - inicio
    for _ in range(n):
        inicio_evento = inicio + timedelta(hours=random.randint(0, int(delta.total_seconds() // 3600)))
        duracion_evento = timedelta(hours=random.randint(duracion_min, duracion_max))
        fin_evento = inicio_evento + duracion_evento
        eventos.append(Evento(inicio_evento, fin_evento))
    return eventos

def maximo_eventos(eventos):
    eventos_ordenados = sorted(eventos, key=lambda evento: evento.fecha_fin) 
    contador = 0
    ultimo_fin = datetime.min


    for evento in eventos_ordenados:
        if evento.fecha_inicio >= ultimo_fin:
            contador += 1
            ultimo_fin = evento.fecha_fin

    return contador


if __name__ == "__main__":
    inicio = datetime(2025, 11, 1)
    fin = datetime(2025, 11, 3)
    eventos = random_eventos(5, inicio, fin, 1, 6) 
    for i, evento in enumerate(eventos):
        print(f"Evento {i+1}: Inicio: {evento.fecha_inicio}, Fin: {evento.fecha_fin}, Duración: {evento.duracion()}")

    max_eventos = maximo_eventos(eventos)
    print(f"Número máximo de eventos que se pueden asistir: {max_eventos}")
