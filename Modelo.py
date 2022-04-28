from operator import imod
import OpenGL.GL as gl
import numpy as np

from ctypes import c_void_p

class Modelo:

    def __init__(self, shader, posicion_id):

        self.shader = shader
        self.vertices = np.array(
            [
                -0.15, -0.5, 0.0, #Izquierda, Abajo
                0.0, 0.5, 0.0,    #Arriba
                0.5, -0.5, 0.0    #Derecha
            ], dtype = "float32"
        )
        
        #Generar vertex array object y vertex buffer object
        self.VAO = gl.glGenVertexArrays(1)
        self.VBO = gl.glGenBuffers(1)

        #Le decimos a OpenGL con cual VAO trabajar
        gl.glBindVertexArray(self.VAO)
        
        # Le decimos a OpenGL con cual Buffer trabajar
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.VBO)

        # Establecerle la información al buffer
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, gl.GL_STATIC_DRAW)

        # Definir como leer el VAO y activarlo
        # La estructura de un vertex puede cambiar mucho por eso definimos como leerlo.
        # GL_FLOAT tiene 32 bits
        # glVertexAttribPointer(indice, tamaño, tipo, boolean, stride, const void * pointer)
        gl.glVertexAttribPointer(posicion_id, 3, gl.GL_FLOAT, 
            gl.GL_FALSE, 0, c_void_p(0))
        gl.glEnableVertexAttribArray(posicion_id)

        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        gl.glBindVertexArray(0)

    def dibujar(self):

        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        # Mandar a dibujar el VAO
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def borrar(self):
        gl.glDeleteVertexArrays(1, self.VAO)
        gl.glDeleteBuffers(1, self.VBO)