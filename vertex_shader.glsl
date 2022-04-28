#version 330 core
layout (location = 0) in vec3 position;
//hay que establecer posicion en la propiedad
//gl_Position que es del tipo vec4
void main() {
gl_Position = vec4(position.x, position.y,
    position.z, 1.0);
}