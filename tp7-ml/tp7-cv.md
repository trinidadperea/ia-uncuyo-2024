# TP7 - Cross Validation

## Función `create_folds()`


```r 
create_folds <- function(data, num_folds) {
  # Obtener el número total de filas en el dataframe
  total_rows <- nrow(data)
  
  # Crear una secuencia de índices del dataframe
  indices <- 1:total_rows
  
  # Mezclar los índices aleatoriamente
  shuffled_indices <- sample(indices)
  
  # Dividir los índices en folds
  folds <- split(shuffled_indices, 1:num_folds)
  
  # Devolver la lista de folds
  return(folds)
}

```

## Funcion `cross_validation()`

```r 

cross_validation <- function(data, num_folds) {
  # Crear folds
  folds <- create_folds(data, num_folds)
  
  # Inicializar vectores para almacenar las métricas de cada fold
  accuracies <- vector("numeric", length = num_folds)
  precisions <- vector("numeric", length = num_folds)
  sensitivities <- vector("numeric", length = num_folds)
  specificities <- vector("numeric", length = num_folds)
  
  for (i in 1:num_folds) {
    # Separar el dataframe en entrenamiento y prueba según el fold actual
    test_indices <- folds[[i]]
    train_indices <- unlist(folds[-i])
    train_data <- data[train_indices, ]
    test_data <- data[test_indices, ]
    
    # Entrenar un modelo de árbol de decisión con rpart
    model <- rpart(inclinacion_peligrosa ~ circ_tronco_cm + altura + lat + long , data = train_data, method = "class")
    
    # Realizar predicciones en el conjunto de prueba
    predictions <- predict(model, test_data, type = "class")
    
    # Calcular métricas para el fold actual
    matriz_de_confusion <- data.frame(
      True_Positive = sum(predictions == 1 & test_data$inclinacion_peligrosa == 1),
      True_Negative = sum(predictions == 0 & test_data$inclinacion_peligrosa == 0),
      False_Positive = sum(predictions == 1 & test_data$inclinacion_peligrosa == 0),
      False_Negative = sum(predictions == 0 & test_data$inclinacion_peligrosa == 1)
    )
    
    accuracies[i] <- accuracy(matriz_de_confusion)
    precisions[i] <- precision(matriz_de_confusion)
    sensitivities[i] <- sensitivity(matriz_de_confusion)
    specificities[i] <- specificity(matriz_de_confusion)
  }
  
  # Calcular la media y desviación estándar de las métricas
  mean_accuracy <- mean(accuracies)
  mean_precision <- mean(precisions)
  mean_sensitivity <- mean(sensitivities)
  mean_specificity <- mean(specificities)
  
  sd_accuracy <- sd(accuracies)
  sd_precision <- sd(precisions)
  sd_sensitivity <- sd(sensitivities)
  sd_specificity <- sd(specificities)
  
  # Devolver las métricas promedio y desviación estándar
  results <- list(
    Mean_Accuracy = mean_accuracy,
    Mean_Precision = mean_precision,
    Mean_Sensitivity = mean_sensitivity,
    Mean_Specificity = mean_specificity,
    SD_Accuracy = sd_accuracy,
    SD_Precision = sd_precision,
    SD_Sensitivity = sd_sensitivity,
    SD_Specificity = sd_specificity
  )
  
  print(results)
  return(results)
}

```

## Tabla de resultados
| Métrica         | Media       | Desviación Estándar |
|--------------   |-------------|---------------------|
| **Accuracy**    | 0.886       | 0.013               |
| **Precision**   | NaN         | NaN                 |
| **Sensitivity** | 0.0         | 0.0                 |
| **Specificity** | 1.0         | 0.0                 |




