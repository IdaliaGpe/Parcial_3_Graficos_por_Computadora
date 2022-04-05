from curses import window
from sre_constants import SUCCESS
from tkinter.messagebox import NO
from turtle import Screen
import OpenGL.GL as gl
import glfw
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

vertex_shader_source = """#version 330 core
                          layout (location = 0) in vec3 position;
                          //hay que establecer posición en la propiedad
                          //gl_Position que es el tipo vec4
                          
                          void main() {
                              gl_Position = vec4(position.x, position.y, position.z, 1.0);
                          }
                        """

fragment_shader_sorce = """#version 330 core
                           out vec4 fragmentColor;

                          void main() {
                              fragmentColor = vec4(1.0f, 0.5f, 0.2f, 1.0);
                          }
                        """

def main():

    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    #Crear Ventana
    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Plantilla Shaders", None, None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana0")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    #vertex shader
    vertex_shader = gl.glCreateShader(gl.GL_VERTEX_SHADER)
    gl.glShaderSource(vertex_shader, vertex_shader_source)
    gl.glCompileShader(vertex_shader)

    success = gl.glGetShaderiv(vertex_shader, gl.GL_COMPILE_STATUS)
    if not success:
        info_log = gl.glGetShaderInfoLog(vertex_shader, 512, None)
        raise Exception(info_log)

    #fragment shader
    fragment_shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
    gl.glShaderSource(fragment_shader, fragment_shader_sorce)
    gl.glCompileShader(fragment_shader)

    success = gl.glGetShaderiv(fragment_shader, gl.GL_COMPILE_STATUS)
    if not success:
        info_log = gl.glGetShaderInfoLog(fragment_shader, 512, None)
        raise Exception(info_log)  

def framebuffer_size_callback(window, width, height):
    gl.glViewport(0, 0, width, height)