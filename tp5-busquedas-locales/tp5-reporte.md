\<h1\>**INTRODUCCIÓN**\</h1\>

En este trabajo, exploramos tres algoritmos de búsqueda local: Simulated Annealing, Hill Climbing (en su versión canónica), y el Algoritmo Genético, aplicándolos al problema de las N-reinas. Este problema consiste en colocar N reinas en un tablero de ajedrez de NxN sin que se amenacen entre sí, lo cual presenta un desafío interesante para los algoritmos de optimización. El objetivo del trabajo es comparar la efectividad y eficiencia, de cada uno de los algoritmos antes mencionados, en la resolución del problema con el fin de analizar cuál de los tres es el más adecuado para encontrar una solución óptima. El estudio se enfoca en cómo las distintas características de cada algoritmo afectan su desempeño y capacidad de escape de óptimos locales, un desafío frecuente en la búsqueda local.

\<h1\>**MARCO TEÓRICO**\</h1\> 

**Hill Climbing**

Es una técnica de búsqueda local que se utiliza para resolver problemas de optimización. Su funcionamiento se basa en el siguiente enfoque: a partir de una solución inicial, el algoritmo explora el espacio de soluciones buscando mejoras incrementales en una función objetivo. Es un algoritmo voraz que solo acepta cambios que mejoran la solución actual, es decir, siempre "sube la colina" (de ahí su nombre).

Existen varias variantes de Hill Climbing, como el Simple Hill Climbing, que evalúa cada vecino y selecciona el primero que mejora la solución, o el Steepest Ascent Hill Climbing, que selecciona el vecino que proporciona la mayor mejora. Si bien es eficiente en algunos casos, Hill Climbing puede quedar atrapado en óptimos locales, que son puntos donde cualquier cambio no parece mejorar la solución, aunque no sea la mejor solución posible.

Una característica importante del algoritmo es su determinismo. Una vez que alcanza un óptimo local, no puede salir de él a menos que se empleen técnicas adicionales como el reinicio aleatorio.

**Simulated Annealing**

Es una variante más robusta de la búsqueda local que busca superar el principal problema de Hill Climbing: quedar atrapado en óptimos locales. Está inspirado en el proceso de recocido en la metalurgia, donde un material se calienta y luego se enfría lentamente para alcanzar un estado de mínima energía.

El algoritmo SA introduce una probabilidad de aceptar soluciones peores temporalmente, con el fin de explorar el espacio de soluciones más ampliamente y evitar quedar atrapado en óptimos locales. Esta probabilidad depende de un parámetro de temperatura que disminuye gradualmente a lo largo de la ejecución del algoritmo. Al inicio, cuando la temperatura es alta, es más probable que se acepten soluciones peores, permitiendo escapar de los óptimos locales. A medida que la temperatura disminuye, el algoritmo se vuelve más parecido a Hill Climbing, aceptando solo soluciones que mejoren la actual.

**Algoritmo Genético**

Son un tipo de algoritmo evolutivo basado en los principios de la selección natural de Darwin. Los GA son algoritmos de optimización inspirados en la biología, que buscan resolver problemas mediante la evolución de un conjunto de soluciones (llamadas población) a lo largo de varias generaciones.

En cada generación, se seleccionan individuos (soluciones) de la población actual para que procreen, creando nuevas soluciones mediante operadores de cruce (mezclando partes de dos soluciones) y mutación (alterando ligeramente una solución). A medida que las generaciones avanzan, las soluciones menos adecuadas se eliminan gradualmente y las más aptas se preservan, imitando el proceso de selección natural. La aptitud de cada solución se mide a través de una función de fitness, que indica qué tan buena es la solución en comparación con las demás.

El GA es especialmente adecuado para problemas donde el espacio de búsqueda es vasto y se necesita una exploración diversa del mismo. Debido a la naturaleza estocástica del algoritmo, el GA es muy efectivo para evitar óptimos locales, ya que mantiene y explora múltiples soluciones simultáneamente.

\<h1\>**DISEÑO EXPERIMENTAL**\</h1\>

Antes de iniciar con las pruebas se diseñaron los algoritmos de búsqueda local: hill climbing, simulated annealing y genetic, teniendo en cuenta las siguientes instrucciones:

- Cada algoritmo debe ser capaz de encontrar solamente una solución para tableros de diferentes tamaños.   
- Definir una función objetivo H(e) la cual contabiliza la cantidad de pares de reinas amenazadas para un tablero e.  
- Definir una variable que establezca el número máximo de estados que podrán ser evaluados  
- Devolver el tablero solución junto con la cantidad de estados que tuvo que recorrer el algoritmo para llegar a la misma, y el tiempo empleado. En caso de alcanzar el máximo de estados evaluados, devolver la mejor solución encontrada y el valor correspondiente de la función H.

Luego, se ejecutó 30 veces cada algoritmo para el caso de 4, 8 y 10 reinas.

\<h1\>**ANÁLISIS Y DISCUSIÓN DE RESULTADOS**\</h1\>

A continuación se muestran los resultados obtenidos usando diagrama de caja

- **Distribución de los tiempos de ejecución** 


\!\[\](https://github.com/Perlaval/ia-uncuyo-2024/blob/main/tp4-busquedas-locales/images/tiempo\_ejecucion\_boxplot.png)

- **Distribución de la cantidad de estados visitados**

\!\[\](https://github.com/Perlaval/ia-uncuyo-2024/blob/main/tp4-busquedas-locales/images/estados\_visitados\_boxplot.png)

**Datos obtenidos:**

Tiempo de ejecución promedio  3.5821420907974244  
Desviación estándar en tiempo de ejecucion  4.292314216103424  
Porcentaje de soluciones encontradas  2.1  
Desviación estándar en tiempo de ejecucion  4.292314216103424  
Porcentaje de soluciones encontradas  2.1

**Hill Climbing**: podemos observar que el diagrama de caja correspondiente a la distribución del tiempo de ejecución nos muestra que en general, este algoritmo, tiene un tiempo de ejecución consistente sin mucha variabilidad entre cada prueba, lo mismo podemos ver en el diagrama de caja correspondiente a la distribución de la cantidad de estados visitados pero también es importante tener en cuenta que este algoritmo es propenso a quedarse atrapado en óptimos locales, entonces esto influye en el hecho de que no esté explorando lo suficiente el espacio de soluciones, lo que lo limita a encontrar la solución más óptima.

**Simulated Annealing**: a diferencia del algoritmo anterior, este muestra un poco mas de variabilidad en la distribución de la cantidad de estados visitados lo que indica que pudo tener una mejor exploración del espacio de soluciones esto se debe a que dicho algoritmo trata de solucionar el problema de hill climbing (quedar atrapado en óptimos locales) al permitir la aceptación de soluciones peores en ciertas condiciones.

**Algoritmo Genético**: podemos observar que ambos gráficos de distribución (cantidad de estados visitados y tiempo de ejecución) son bastante más extensos en comparación con los dos anteriores esto se puede interpretar de la siguiente manera:

- Distribución de cantidad de estados visitados: vemos más variabilidad en la cantidad de estados visitados porque involucra muchas soluciones en cada generación lo que permite explorar más ampliamente el espacio de solución.  
- Distribución de tiempo de ejecución: pueden requerir más tiempo para realizar operaciones de selección y cruce, lo que puede resultar en tiempos de ejecución más largos.

**Variación de la función heurística a lo largo de las iteraciones**

- **Hill Climbing**


\!\[\](https://github.com/Perlaval/ia-uncuyo-2024/blob/main/tp4-busquedas-locales/images/heuristic\_variation\_HC.png)

La caída rápida inicial indica que el algoritmo **Hill Climbing** logra mejoras significativas en la función heurística desde el principio, luego podemos ver como hace una transición a una función constante después de las mejoras iniciales esto se puede deber a que el algoritmo encontró un punto donde ya no puede realizar más mejoras en la función heurística porque ha alcanzado un óptimo local.

- **Simulated Annealing**

\!\[\](https://github.com/Perlaval/ia-uncuyo-2024/blob/main/tp4-busquedas-locales/images/heuristic\_variation\_SA.png)

En este caso vemos como el algoritmo **Simulated Annealing** va explorando activamente el espacio de soluciones. El comportamiento que vemos en el gráfico es característico del proceso de “enfriamiento” del algoritmo donde al principio la temperatura es alta, lo que permite una mayor aceptación de cambios, incluso aquellos que no son los mejores.

- **Genético**

\!\[\](https://github.com/Perlaval/ia-uncuyo-2024/blob/main/tp4-busquedas-locales/images/heuristic\_variation\_GA.png)

En este gráfico podemos ver cómo el algoritmo **Genético** ha encontrado varios óptimos locales lo que vendrían siendo soluciones de calidad comparable 

\<h1\>**CONCLUSIONES**\</h1\>

Aunque el algoritmo Hill Climbing es más simple y rápido, pudimos ver en los resultados que tiene tendencia a quedar atrapado en los óptimos locales por lo que no termina de explorar correctamente el espacio de solución. En cambio, el algoritmo Simulated Annealing mostró mejor capacidad para explorar el espacio solución, especialmente en las primeras iteraciones, y vimos en la gráfica de la variación de la heurística como pudo evitar caer rápidamente en un óptimo local. Por su parte el último algoritmo, Genético, presentó un equilibrio entre exploración y explotación. La presencia de múltiples escalones en la gráfica de la heurística indica que encontró varias soluciones de calidad comparable a lo largo de las generaciones.

Para concluir, el Algoritmo Genético parece ser el más adecuado para resolver el problema de las N-reinas entre los tres algoritmos implementados. Su capacidad para explorar el espacio de soluciones de manera más amplia y su mantenimiento de la diversidad en la población lo hacen eficaz para encontrar soluciones óptimas en configuraciones complejas. Un mayor tiempo de ejecución garantiza la calidad de la solución.