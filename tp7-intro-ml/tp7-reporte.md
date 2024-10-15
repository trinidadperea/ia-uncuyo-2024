# Respuestas a ISLRv2

## Ejercicio 1

For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

### a. The sample size n is extremely large, and the number of predictors p is small.

En este caso, donde el tamaño de la muestra n es extremadamente grande y el número de predictores p es pequeño, generalmente esperaríamos que un método flexible tenga un rendimiento mejor que un método inflexible. Ya que tienen la capacidad de capturar relaciones complejas en los datos, especialmente cuando el conjunto de datos es lo suficientemente grande como para proporcionar suficiente información para estimar con precisión dichas relaciones. Con un tamaño de muestra n grande, el modelo tiene muchos datos para evitar el sobreajuste, lo que suele ser un riesgo en modelos flexibles cuando el tamaño de la muestra es pequeño.

### b. The number of predictors p is extremely large, and the number of observations n is small.

En este caso, donde el número de predictores p es extremadamente grande y el número de observaciones n es pequeño, generalmente esperaríamos que un método inflexible tenga un rendimiento mejor que un método flexible. Ya que cuando hay pocos datos en comparación con el número de predictores, se reduce el riesgo de sobreajuste y el modelo se vuelve más estable.

### c. The relationship between the predictors and response is highly non-linear.

En este caso, donde la relación entre los predictores y la respuesta es altamente no lineal, generalmente esperaríamos que un método flexible tenga un rendimiento mejor que un método inflexible. Al no imponer suposiciones estrictas sobre la forma de la relación entre los predictores y la respuesta, estos métodos pueden adaptarse mejor a patrones no lineales, lo que permite capturar con mayor precisión la estructura subyacente de los datos.

### d. The variance of the error terms, i.e. $\sigma^2 = Var(\epsilon)$, is extremely high.

En este caso, donde la varianza de los términos de error es extremadamente alta, generalmente esperaríamos que un método inflexible tenga un rendimiento mejor que un método flexible. Los datos pueden ser muy dificiles de modelar debido a la alta variabilidad del error. Por lo tanto lo mejor sera una metodo inflexible, ya que al imponer mas restricciones y no permitir una gran adaptabilidad a los datos, tienden a ser mas resistentes. 

## Ejercicio 2

Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

### a. We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

> n = 500 
> p = 3 
> regresion
> inferencia

### b. We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

> n = 20 
> p = 13
> clasificacion
> prediccion

### c. We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

> n = 52 
> p = 3
> regresion 
> prediccion

## Ejercicio 5

What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

Un enfoque flexible puede ajustarse a relaciones no lineales o complejas entre los predictores y la variable de respuesta. Esto es útil cuando los datos tienen estructuras complejas que un enfoque menos flexible no podría modelar correctamente. Cuando el número de observaciones n es grande, un enfoque flexible puede aprovechar los datos adicionales para ajustar el modelo sin sobreajustar, lo que da como resultado un mejor rendimiento en términos de precisión. Los enfoques flexibles tienen un menor sesgo en el modelo, ya que hacen menos suposiciones sobre la forma de la relación entre las variables. Los enfoques menos flexibles son más sencillos de interpretar, ya que suelen tener coeficientes claros que describen las relaciones entre los predictores y la variable de respuesta. Si se sabe que las relaciones entre los predictores y la variable de respuesta son no lineales, un enfoque flexible será más adecuado para capturar dichas relaciones.

## Ejercicio 6

Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)?What are its disadvantages?

Un modelo parametrico utiliza parametros. Estos modelos suelen ser mas interpretables, ya que existe un modelo detras de como son generados los datos. Sin embargo, la desventaja es que el modelo podria no relfejar la realidad. Si el modelo esta muy lejos de la verdad, las estimaciones seran deficientes y los modelos mas flexibles pueden adaptarse a muchos modelos diferentes. Los enfoques que no son parametricos, no estiman un numero pequeño de parametros, por lo que para grandes numeros se neceistan observaciones mas precisas. 

## Ejercicio 7

> The table below provides a training data set containing six observations,
> three predictors, and one qualitative response variable.
> 
> | Obs. | $X_1$ | $X_2$ | $X_3$ | $Y$   |
> |------|-------|-------|-------|-------|
> | 1    | 0     | 3     | 0     | Red   |
> | 2    | 2     | 0     | 0     | Red   |
> | 3    | 0     | 1     | 3     | Red   |
> | 4    | 0     | 1     | 2     | Green |
> | 5    | -1    | 0     | 1     | Green |
> | 6    | 1     | 1     | 1     | Red   |
> 
> Suppose we wish to use this data set to make a prediction for $Y$ when 
> $X_1 = X_2 = X_3 = 0$ using $K$-nearest neighbors.
>
### a. Compute the Euclidean distance between each observation and the test point, $X_1 = X_2 = X_3 = 0$.

    - 1. √9 = 3

    - 2. √4 = 2

    - 3. √10 = 3.16

    - 4. √5 = 2.24

    - 5. √2 = 1.41

    - 6. √3 = 1.73

### b. What is our prediction with $K = 1$? Why?

El verde basado en el punto de datos 5.

### c. What is our prediction with $K = 3$? Why?

El rojo basado en el punto de dato 2, 5, 6.

### d. If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for $K$ to be large or small? Why?

Mas chico, ya que un k alto conduce a limites lineales debido al promedio.

