library(ggplot2)
library(dplyr)
library(rpart)
library(readr)

train_data <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv")
validation_data <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-validation.csv")

#a)
agregar_columna_aleatoria <- function(data) {
  # Generar valores aleatorios entre 0 y 1
  valores_random <- runif(nrow(data), min = 0, max = 1)
  
  # Agregar la nueva columna al data.frame
  data$prediction_prob <- valores_random
  
  # Devolver el data.frame con la nueva columna
  return(data)
}

#b)
# Función para generar la columna prediction_class
random_classifier <- function(data) {
  # Aplicar el criterio y generar la nueva columna
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  
  # Devolver el data.frame con la nueva columna
  return(data)
}

train_data <- agregar_columna_aleatoria(train_data)
validation_data <- agregar_columna_aleatoria(validation_data)

# c)
validation_data <- random_classifier(validation_data)

head(validation_data)

#d.
calculate_confusion_matrix <- function(actual, predicted) {
  TP <- sum(actual == 1 & predicted == 1)
  TN <- sum(actual == 0 & predicted == 0)
  FP <- sum(actual == 0 & predicted == 1)
  FN <- sum(actual == 1 & predicted == 0)
  
  confusion_matrix <- data.frame(TP = TP, TN = TN, FP = FP, FN = FN)
  
  return(confusion_matrix)
}

# Utilizar la función para calcular la matriz de confusión
confusion_matrix <- calculate_confusion_matrix(validation_data$inclinacion_peligrosa, validation_data$prediction_class)

# Ver la matriz de confusión
View(confusion_matrix)


#5)

# Definir la función biggerclass_classifier
biggerclass_classifier <- function(data) {
  # Calcular la clase mayoritaria
  majority_class <- as.numeric(names(sort(table(data$inclinacion_peligrosa), decreasing = TRUE)[1]))
  
  # Crear la nueva columna prediction_class con la clase mayoritaria
  data$prediction_class <- majority_class
  
  # Devolver el dataframe con la nueva columna
  return(data)
}

validation_data <- biggerclass_classifier(validation_data)

confusion_matrix <- calculate_confusion_matrix(validation_data$inclinacion_peligrosa, validation_data$prediction_class)

View(confusion_matrix)

#6)

accuracy <- function(confusion_matrix) {
  TP <- confusion_matrix$True_Positive
  TN <- confusion_matrix$True_Negative
  FP <- confusion_matrix$False_Positive
  FN <- confusion_matrix$False_Negative
  return((TP + TN) / (TP + TN + FP + FN))
}

precision <- function(confusion_matrix) {
  TP <- confusion_matrix$True_Positive
  FP <- confusion_matrix$False_Positive
  return(TP / (TP + FP))
}

sensitivity <- function(confusion_matrix) {
  TP <- confusion_matrix$True_Positive
  FN <- confusion_matrix$False_Negative
  return(TP / (TP + FN))
}

specificity <- function(confusion_matrix) {
  TN <- confusion_matrix$True_Negative
  FP <- confusion_matrix$False_Positive
  return(TN / (TN + FP))
}

accuracy_value <- accuracy(confusion_matrix)
cat("Accuracy:", accuracy_value, "\n")
precision_value <- precision(confusion_matrix)
cat("Precision:", precision_value, "\n")
sensitivity_value <- sensitivity(confusion_matrix)
cat("Sensitivity:", sensitivity_value, "\n")
specificity_value <- specificity(confusion_matrix)
cat("Specificity:", specificity_value, "\n")

# 7)

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
resultados_arbol_decicion <- cross_validation(train_data, 10)

print(resultados_arbol_decicion)