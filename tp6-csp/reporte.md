# Trabajo Práctico 6: Satisfacción de restricciones

1. Describir en detalle una formulación CSP para el Sudoku.
    - **Variables**: son las celdas individuales del tablero de Sudoku (Ti,j)
    - **Dominio**: es el conjunto de números posibles que pueden colocarse en una celda
        Di,j = {1,2,3,4,5,6,7,8,9}

        El dominio de las celdas que ya contienen un número al inicializar el sudoku, se limita al número presente.
    - **Restricciones**: condiciones que deben cumplirse para hacer asignaciones de valores válidas a las variables.
        - **Restricción de fila**: los números del 1 al 9 deben aparecer una sola vez
        - **Restricción de columna**: en cada columna se deben usar los números del 1 al 9 una sola vez.
        - **Restricción de subcuadrado**: en cada uno de los subcuadrados, los números del 1 al 9 deben aparecer una sola vez.

2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial WA=red, V=blue para el problema de colorear el mapa de Australia
(Figura 6.1 AIMA 3ra edición ).

![Texto alternativo](images\6.1_AIMA.png)


    - **Variables**: WA, NT, Q, NSW, SA, V, T
    - **Dominios**: 
        - WA = {red}
        - NT = {red, green, blue}
        - Q = {red, green, blue}
        - NSW = {red, green, blue}
        - SA = {red, green, blue}
        - v = {blue}
        - T = {red, green, blue}
    - **Restricciones**:
        - WA != NT, SA
        - NT != WA, SA, Q
        - Q != NT, SA, NSW
        - NSW != Q, SA, V
        - V != NSW, SA
    - **Arcos**:
        (WA,NT), (WA,SA), (NT,SA), (NT, Q), (Q,SA), (Q,NSW), (NSW,SA), (NSW,V), (V,SA).
    - **Aplicamos el algortimo:**
        Q = {(WA,NT), (WA,SA), (NT,SA), (NT, Q), (Q,SA), (Q,NSW), (NSW,SA), (NSW,V), (V,SA)}

        1. Verificamos (WA,NT)
            WA = {red}
            NT = {red, blue, green}
            modificamos el domino de NT: {blue, green}
        2. Verificamos (WA,SA)
            WA = {red}
            SA = {red,blue, green}
            modificamos el domino de SA: {blue,green}
        3. Verificamos (NT,SA)
            NT = {blue, green}
            SA = {blue, green}

        En este caso vemos que al hacer la modificación de los dominios, uno de los dos quedaría vacío,  por lo que estaríamos obteniendo una **inconsistencia**

3. ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP?
(i.e. cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas
por a lo sumo un camino).

La complejidad del algoritmo AC-3 en un problema de satisfacción de restricciones (CSP) cuya estructura es un árbol puede analizarse observando la **cantidad de arcos** que el algoritmo revisa y **cuántas veces puede hacer modificaciones en los dominios**.
    **Número de arcos en un árbol estructurado**: En un CSP donde las restricciones forman un árbol, si hay n variables, entonces hay exactamente n−1 arcos. Esto por la propiedad de que un árbol tiene n-1 aristas
    **Procesamiento de cada arco**: Por cada revisión de un arco, se comparan los valores de los dominios de las dos variables. Si el dominio de una variable tiene d valores, en el peor caso se realizarán d^2
    **Número de revisiones por arcos**: En el peor caso, un arco podría ser revisado varias veces durante el proceso de propagación, pero en un árbol estructurado CSP, una vez que un arco se vuelve consistente, ya no será revisado nuevamente. Esto se debe a que en los árboles, las dependencias son acíclicas, y por tanto, las modificaciones en los dominios no vuelven a afectar un arco ya revisado.
    **R:** La complejidad en el peor caso del algoritmo AC-3 en un CSP donde las restricciones forman un árbol es **O(n⋅d^2)** 

 4. AC-3 coloca de nuevo en la cola todo arco (Xk,Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk,Xi) se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk. Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n2d2).

Para cada valor en el dominio de Xk, llevamos un contador que indica cuántos valores en el dominio de Xi, son consistentes con ese valor de Xk. Si un valor de Xk no tiene ningún valor de Xi, que lo soporte, entonces se debe eliminar ese valor de Xk.

    1. Inicialización de contadores
    Para cada arco (Xk, Xi) y cada valor vk ∈ Dom(Xk), llevamos un contador support(vk,Xi) que indica cuantos valores en Dom(Xi) son consistentes con vk.
    Revisamos los pares (vk,vi), donde vk ∈ Dom(Xk) y vi ∈ Dom(Xi), verificamos si vk es consistente con vi y siempre que hallamos un par consistente, incrementamos el contador.

    2. Actualización de contadores
    Si se elimina un valor vi ∈ Dom(Xi), para cada valor vk ∈ Dom(Xk), si (vi,vk) era un par consistente, entonces decrementamos el contador de soporte support(vk,Xi).
    Si el contador de soporte de un valor vk llega a cero, entonces no hay ningún valor en Dom(Xi) que sea consistente con vk. En este caso, el valor vk debe ser eliminado del dominio de Xk, ya que no es posible encontrar una  asignación válida para ese valor bajo la restricción (Xk,Xi).

    3. Colocación de arcos en la cola
    Solo si eliminamos un valor vk de Dom(Xk) se tiene que volver a agregar el arco (Xk,Xi) para cualquier variable Xi que dependa de Xk. De esta manera se evita volver a agregar arcos a la cola si no hay cambios en los dominios.

    **Complejidad:** 
        - Para cada arco, necesitamos verificar la consistencia de cada par de valores, lo cual toma O(d^2) tiempo. d: tamaño máximo de un dominio.
        - Como hay O(n^2) arcos en el peor caso, la inicialización de los contadores toma O(n^2 x d^2).

5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 6.5, AIMA 3ra edición). Para ello, demostrar:

    - **Para un CSP cuyo grafo de restricciones es un árbol, la 2-consistencia (consistencia de arco) implica n−consistencia, siendo n el número total de variables.** 

        En un árbol, hay un solo camino entre cualquier par de variables, por lo que las dependencias entre variables están acotadas y no hay ciclos.
        Como el problema es 2-consistente, la estructura del árbol asegura que esta consistencia puede propagarse a todas la variables

        **Inducción sobre el número de variables:**
        1. **Base:** : para el caso de 1-consistencia (n=1), la asignación de una sola variable, es siempre posible ya que no hay restricciones

        2. **Paso Inductivo:** supongamos que para n-1 variables ya asignadas, hemos logrado una asignación consistente y queremos mostrar que podemos extender esta asignación al agregar una variable Xnuevo , de manera que sea consistente con las n-1 variables anteriores.

        Como estamos trabajando con un árbol, Xnuevo solo estará conectado a lo sumo a una de las variables asignadas (Xk), ya que no puede haber múltiples cambios entre las variables. Debido a la 2-consistencia, sabemos que para cualquier valor asignado a Xk, hay un valor consistente que podemos asignar a Xnuevo. Por lo que podemos asignar un valor a Xnuevo que sea consistente con todas las variables antes asignadas.

    - **Argumentar por qué lo demostrado en 5a es suficiente.**
        La demostración anterior es suficiente porque: 

        1. Los árboles no tienen ciclos, por lo que no habría manera de que se introduzca una inconsistencia en asignaciones previas, por lo que, una vez que se garantiza la consistencia de las asignaciones de pares de variables, se estaría asegurando que cualquier nueva variable puede ser asignada de manera consistente sin afectar las asignaciones previas.
        2. No hay caminos múltiples que puedan causar problemas de consistencia. La 2-consistencia, asegura la n-consistencia

        Resolver CSPs en árboles es mucho más eficiente, ya que al verificar la consistencia de pares asegura la consistencia en el conjunto completo de variables.

6. Implementar una solución al problema de las N-reinas utilizando una formulación CSP:
    + Implementar una solución utilizando backtracking.
    + Implementar una solución utilizando forward checking

7. Ejecutar 30 veces cada uno de los algoritmos implementados en el ejercicio 6, para el caso de 4,
8 y 10 reinas (opcional: 12 y 15 reinas). Para cada uno de los algoritmos:
    **Porcentaje de veces que se llega a un estado de solucion óptimo**
    Ambos algortimos siempre llegan a una solución óptima en cada ejecución por lo que el porcentaje de veces es 100%
    **Media y desviación estándar de tiempos**
    | algoritmo | n-reinas | media | desviacion estándar|
    |-----------|----------|-------|--------------------|
    | Backtracking | 4 | 1.3573331913600366e-05 | 2.263797253136027e-06 |
    | Forward Checking | 4 | 2.083666428613166e-05 | 1.0551922756351889e-05 |
    | Backtracking | 8 | 0.0005303666684388493 | 0.00016151011624929067 |
    | Forward Checking | 8 | 0.00026739333504034827 | 6.068958829428485e-05 |
    | Backtracking | 10 | 0.0006323233334114775 | 0.00012437401440250587 |
    | Forward Checking | 10 | 0.0002956733340397477 | 5.9639901374452104e-05 |
    **Media y desviación estándar de estados previos visitados**
    | algoritmo | n-reinas | media | desviacion estándar|
    |-----------|----------|-------|--------------------|
    | Backtracking | 4 | 10 | 0.0 |
    | Forward Checking | 4 | 5 | 0.0 |
    | Backtracking | 8 | 36 | 0.0 |
    | Forward Checking | 8 | 13 | 0.0 |
    | Backtracking | 10 | 55 | 0.0 |
    | Forward Checking | 10 | 15 | 0.0 |

**Realizar gráficos de caja y bigotes (boxplots) que muestren la distribución de los tiempos de
ejecución de cada algoritmo, y la distribución de la cantidad de estados previos visitados**

![Texto alternativo](images\Dist_estados.png)

![Texto alternativo](images\Dist_tiempos.png)

En los resultados obtenidos podemos ver que el algoritmo de Forward Checking (con formulación CSP) evalúa menos estados y completa su ejecución en un tiempo más corto que el algortimo de backtracking (con formulación CSP)

Al evaluar los resultados obtenidos en el TP5, pudimos observar que los algoritmos implementados en este trabajo prático son más eficinetes en términos de tiempo de ejecución y estados visitados que los algoritmos heurísticos (Hill Climbing, Simulated Annealing, Genetic), los cuales a menudo requieren más tiempo y exploración de estados ya que su enfoque se basa en la búsqueda local. Este enfoque, puede llevar a encontrar soluciones sub-optimas o en algunos casos no econtrar ninguna solucion, en cambio el backtracking (con CSP) y el forward Checking (con CSP) siempre son capaces de encontrar soluciones óptimas al explorar sistemáticamente el espacio de soluciones y retroceder al encontrar conflictos.























