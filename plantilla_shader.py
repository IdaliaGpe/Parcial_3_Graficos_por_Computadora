import OpenGL.GL as gl
import glfw
import numpy as np

from pyexpat import model
from re import M
from Shader import *
from Modelo import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

modelo = None

# """ - Todo lo que este adentro va a ser un string y nos va a respetar saltos de linea, etc.
# La primera linea siempre tiene que ser la versión.
# layout - es como una plantilla a la que se le pasa un identificador (location = 0)
# in - atributos de entradas (el valor se le asigna desde el CPU)
# vec3 es el tipo de dato (x, y, z) y position es el nombre de la variable.
# out - salida

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def dibujar():

    global modelo

    modelo.dibujar()

def main():
    global modelo

    glfw.init()

    # Trabaja con la versión 3
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")

    modelo = Modelo(shader, posicion_id)

    # Draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.3,0.3,0.3,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Dibujar
        dibujar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar Memoria
    modelo.borrar()
    shader.borrar()
    
    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)

if __name__ == '__main__':
    main()