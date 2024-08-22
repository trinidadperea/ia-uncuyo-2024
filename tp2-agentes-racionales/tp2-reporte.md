## Introduccion
El problema abordado en este proyecto es la optimización de un agente reflexivo simple en un entorno de aspiradora, donde el agente debe limpiar un entorno con suciedad distribuida aleatoriamente. El objetivo principal es evaluar el desempeño del agente en diferentes configuraciones del entorno y diferentes porcentajes de suciedad, y determinar la efectividad del agente en términos de la cantidad de suciedad limpiada.
## Marco Teorico
En cuanto al entorno, este consiste en una cuadricula, que le fuimos dando varios tamaños, en la cual cada celda puede estar limpia o sucia, representadas por 0 y 1 respectivamente. En cuanto al agente, este puede moverse en 4 direcciones y realiar dos acciones, o limpiar, o nada, si es el agente refelxivo simple, si cae en una celda sucia la debe limpiar, y si es el agente reflexivo aleatorio, solo limpia cuando le toca la accion limpiar.
## Diseño Experimental
Medimos el entorno con 7 tamaños diferentes, 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128, y la suciedad con 4 porcentajes diferentes, 0.1, 0.2, 0.4 y 0.8, y tambien medimos la cantidad de veces que el agente limpio, para luego sacar un porcentaje. 
## Analisis y discusion de resultados
Primero realizamos una tabla, en la cual cargamos todos los resultados obtenidos con los diferentes tamaños y suciedades, que luego pasamos a un grafico para poder visualizarlo. Como conclusion, vemos que el entorno puede afectar al rendimiento del agente, y mas si el agente es aleatorio. 
