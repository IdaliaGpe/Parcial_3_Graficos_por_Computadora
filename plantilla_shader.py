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