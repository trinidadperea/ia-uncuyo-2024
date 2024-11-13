# Informe: Evaluación del Algoritmo ID3 sobre el dataset `tennis.csv`

## Resultados sobre la Evaluación sobre `tennis.csv`

Para evaluar el rendimiento del algoritmo de árbol de decisión implementado con el conjunto de datos `tennis.csv`, se realizó la construcción del árbol de decisión utilizando el algoritmo ID3 con las siguientes características:

- **Características de Entrada**: `outlook`, `temp`, `humidity`, `windy`
- **Clase a predecir**: `play`

### Árbol de Decisión Generado

El árbol de decisión generado por el algoritmo ID3 sobre el dataset es el siguiente:

{'outlook': {
    'sunny': {
        'humidity': {
            'high': 'no',
            'normal': 'yes'
        }
    },
    'overcast': 'yes',
    'rainy': {
        'windy': {
            'false': 'yes',
            'true': 'no'
        }
    }
}}


### Evaluación Empírica

Utilizando el conjunto de datos `tennis.csv`, la predicción se realizó para los siguientes ejemplos:

#### Ejemplo 1: `sunny, hot, high, false`
- **Predicción**: `no`
- **Valor Real**: `no`
- **Resultado**: Correcto

#### Ejemplo 2: `rainy, cool, normal, false`
- **Predicción**: `yes`
- **Valor Real**: `yes`
- **Resultado**: Correcto

#### Ejemplo 3: `overcast, hot, high, false`
- **Predicción**: `yes`
- **Valor Real**: `yes`
- **Resultado**: Correcto

#### Ejemplo 4: `rainy, mild, high, true`
- **Predicción**: `no`
- **Valor Real**: `no`
- **Resultado**: Correcto

En general, el modelo muestra un rendimiento correcto sobre este conjunto de datos pequeño. El árbol de decisión se construye con éxito y realiza predicciones precisas para los ejemplos seleccionados del conjunto de datos.

### Precisión del Modelo

Para evaluar la precisión del modelo de manera más robusta, se podría aplicar validación cruzada o dividir los datos en un conjunto de entrenamiento y un conjunto de prueba. Sin embargo, dado que el conjunto de datos proporcionado es relativamente pequeño y simple, la precisión es bastante alta en este caso.

## Estrategias para Datos de Tipo Real

El algoritmo ID3 originalmente está diseñado para trabajar con características discretas, como se observa en este ejercicio. Sin embargo, en muchos casos, los conjuntos de datos contienen variables numéricas o continuas (de tipo real). Existen varias estrategias para manejar este tipo de datos en árboles de decisión.

### 1. **Discretización de Variables Continuas**
Una estrategia común es convertir las variables continuas en variables discretas. Esto se puede hacer de las siguientes maneras:
- **Discretización basada en rangos**: Se pueden establecer intervalos específicos para las variables continuas (por ejemplo, "edad > 20 y <= 30", "edad > 30 y <= 40").
- **Discretización basada en percentiles**: Dividir los datos en intervalos que contengan un número similar de ejemplos.

### 2. **Creación de Umbrales de División**
Otra estrategia es encontrar un umbral adecuado para dividir las variables continuas. En lugar de asignar etiquetas discretas a los valores, se evalúa si una variable continua es mayor o menor que un umbral específico. Por ejemplo, si la variable es la **temperatura**, se puede dividir entre "temperatura > 30" y "temperatura <= 30".

- **Proceso de selección del umbral**: El umbral que maximice la ganancia de información (o reduzca la entropía) se seleccionaría en cada paso de la construcción del árbol de decisión.

### 3. **Modificación del Algoritmo ID3**
Se pueden modificar las versiones tradicionales de los algoritmos de árboles de decisión (como ID3 y C4.5) para que funcionen con datos continuos. Estos algoritmos pueden calcular la ganancia de información no solo sobre características discretas, sino también sobre rangos continuos. El árbol seleccionaría el valor de la variable continua que proporcione la mayor ganancia al dividir el conjunto de datos.

### 4. **Uso de Árboles de Decisión para Datos Continuos (CART)**
Una alternativa más avanzada para trabajar con datos continuos es utilizar el algoritmo CART (Classification and Regression Trees). En lugar de dividir solo en categorías discretas, CART crea divisiones basadas en umbrales numéricos para variables continuas. Este algoritmo es más flexible y puede manejar tanto variables continuas como discretas sin necesidad de discretización previa.

## Conclusión

El algoritmo ID3 ha sido implementado y evaluado con éxito sobre el conjunto de datos `tennis.csv`. Si bien el modelo mostró buenos resultados en este conjunto de datos simple y pequeño, en aplicaciones con variables continuas o más complejas se deben considerar las estrategias de discretización o la modificación del algoritmo para manejar datos continuos de manera más eficiente. La implementación de variantes como CART podría ofrecer mejores resultados en escenarios más complejos.

