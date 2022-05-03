// """ - Todo lo que este adentro va a ser un string y nos va a respetar saltos de linea, etc.
// La primera linea siempre tiene que ser la versión.
// layout - es como una plantilla a la que se le pasa un identificador (location = 0)
// in - atributos de entradas (el valor se le asigna desde el CPU)
// vec3 es el tipo de dato (x, y, z) y position es el nombre de la variable.
// out - salida

#version 330 core
layout (location = 0) in vec4 position;
in vec4 color;
//Los out, van hacia el fragment shader
out vec4 fragmentColor;
//Hay que establecer posicion en la propiedad
//gl_Position que es del tipo vec4
void main() {
    gl_Position = position;
    fragmentColor = color;
}