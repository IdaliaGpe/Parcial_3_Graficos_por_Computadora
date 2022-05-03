from Modelo import *

class Triangulo(Modelo):

    def __init__(self, shader, posicion_id, color_id):

        self.vertices = np.array(
            [
                -0.15, -0.5, 0.0,1.0 ,  1.0, 0.0, 0.0, 1.0,  # Izquierda, abajo
                0.0, 0.5, 0.0,1.0    ,  1.0, 0.0, 0.0, 1.0,  # Arriba
                0.5, -0.5, 0.0,1.0 ,    1.0, 0.0, 0.0, 1.0   # Derecha
            ], dtype = "float32"
        )
        super().__init__(shader, posicion_id, color_id)