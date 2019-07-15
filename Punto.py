class Punto():
    def __init__(self):
        self.puntuacion = 100
        self.cambio_puntuacion = 20

    def cambiar_puntuacion(self, cambio_puntuacion):
        self.puntuacion += cambio_puntuacion

    def puntuacion_actual(self):
        return self.puntuacion
