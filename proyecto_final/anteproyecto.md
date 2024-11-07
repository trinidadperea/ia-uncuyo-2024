**Algoritmo de Hill Climbing para jugar Tetris** 

**Código del proyecto:** TETRIS  
**Integrantes:** Valerio Perla, Perea Trinidad

**Descripción:**

El proyecto consistirá en desarrollar un agente que juegue al Tetris utilizando técnicas de búsqueda local, específicamente el algoritmo de Hill Climbing, para determinar la mejor posición para cada pieza, con el objetivo de maximizar la puntuación obtenida. Tetris es un videojuego clásico en el que el jugador debe colocar piezas geométricas que caen, conocidas como tetrominós, en un espacio de juego con el fin de completar filas. Cuando una fila se completa, desaparece y se acumulan puntos. La dificultad radica en ubicar las piezas de manera eficiente para evitar que el espacio de juego se llene antes de completar una línea, lo que termina la partida.

El objetivo principal del proyecto será implementar un agente que, dada la secuencia de piezas que caen, utilice el algoritmo de Hill Climbing para determinar la mejor posición para colocar cada pieza y maximizar la puntuación de acuerdo con las reglas del juego. Para ello, se evaluarán varias métricas, tales como el puntaje obtenido, el número de filas eliminadas y el tiempo de juego. El alcance del proyecto estará limitado a la implementación de un algoritmo que evalúe diversas posiciones posibles y seleccione la mejor opción para cada pieza, con el fin de optimizar la jugabilidad.

El juego de Tetris sobre el cual se realizarán las pruebas lo desarrollaremos usando la biblioteca pygame, la cual es una librería para el desarrollo de juegos en 2D con lenguaje de programación python. A continuación se especifica cómo se puntúan los movimientos y objetivos cumplidos:

- Se obtienen más puntos en el juego cuando se completan varias líneas a la vez (el mínimo es 1 línea y el máximo es 4\)

- A lo largo del juego, al aumentar la velocidad también aumenta el puntaje que se obtiene al completar líneas

* Puntos Base:

  - 1 línea: 100 puntos.   
  - 2 líneas: 200 puntos.   
  - 3 líneas: 400 puntos.   
  - 4 líneas: 800 puntos

Baseline: Como base para la evaluación del rendimiento del agente que implementa el algoritmo de hill climbing implementaremos un agente aleatorio que coloca las piezas en posiciones al azar, el cual nos servirá como punto de referencia mínima.

**Justificación:**  
Implementar un agente que juegue al Tetris utilizando el algoritmo de Hill Climbing es interesante por varias razones. La primera es que Tetris es un juego que no requiere habilidades cognitivas complejas, pero sí de una estrategia para organizar y adaptar las piezas a las configuraciones posibles del tablero. Con el uso de Hill Climbing, el agente puede explorar las posiciones óptimas para cada pieza y maximizar su rendimiento en términos de puntuación. Además, Hill Climbing permite una toma de decisiones eficiente en tiempo real, adaptándose a las condiciones cambiantes del juego sin necesidad de planificar a largo plazo. El enfoque de este proyecto es utilizar un algoritmo que no dependa de una predicción global del juego, sino que trabaje con decisiones inmediatas, ajustándose dinámicamente a las configuraciones del tablero en cada turno.

**Listado de actividades a realizar:**

1. **Lectura y comprensión del algoritmo de Hill climbing, técnicas de optimización y métodos de evaluación** (2 días)  
2. **Revisión de la documentación y desarrollo del juego Tetris** (3 días)  
3. **Desarrollo del algoritmo de Hill climbing** (5 días)  
   * Implementación del algoritmo  para determinar las mejores posiciones para colocar cada pieza. 

3.1. **Definición de la función de evaluación que calcule la puntuación basada en**   
**la ubicación de las pieza** (2 días)  
3.2. **Optimización del agente utilizando búsqueda local** (3 días)

4. **Pruebas y comparación de soluciones** (2 días)  
5. **Recopilación y análisis de métricas** (2 días)  
6. **Elaboración de gráficos y visualización de resultados** (2 días)  
7. **Elaboración del informe final** (6 días)  
8. **Elaboración de la presentación del proyecto** (2 días)

**Referencias:**

[https://nlp.fi.muni.cz/aiproject/ui/kuna\_karol2016/tetris-documentation.pdf](https://nlp.fi.muni.cz/aiproject/ui/kuna_karol2016/tetris-documentation.pdf)

[https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/](https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/)

[https://cs229.stanford.edu/proj2012/BodoiaPuranik-ApplyingReinforcementLearningToCompetitiveTetris.pdf](https://cs229.stanford.edu/proj2012/BodoiaPuranik-ApplyingReinforcementLearningToCompetitiveTetris.pdf)

[https://www.pygame.org/news](https://www.pygame.org/news)

[https://noob.fandom.com/es/wiki/Tetris\#:\~:text=El%20Tetris%3A%20Se%20obtiene%20m%C3%A1s,m%C3%A1s%20l%C3%ADneas%20acumuladas%2C%20mejor%20puntaje](https://noob.fandom.com/es/wiki/Tetris#:~:text=El%20Tetris%3A%20Se%20obtiene%20m%C3%A1s,m%C3%A1s%20l%C3%ADneas%20acumuladas%2C%20mejor%20puntaje).