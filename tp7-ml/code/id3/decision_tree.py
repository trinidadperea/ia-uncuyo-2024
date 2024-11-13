import pandas as pd
import math

# Cálculo de la Entropía de un conjunto de datos
def entropy(data):
    # Calcular la distribución de las clases
    class_counts = data.iloc[:, -1].value_counts()
    total = len(data)
    
    # Calcular la entropía
    ent = 0
    for count in class_counts:
        p = count / total
        ent -= p * math.log2(p)
    return ent

# Cálculo de la ganancia de información
def information_gain(data, feature_index):
    total_entropy = entropy(data)
    
    # Obtener los valores únicos de la característica
    feature_values = data.iloc[:, feature_index].unique()
    
    # Calcular la entropía ponderada de los subconjuntos después de dividir
    weighted_entropy = 0
    for value in feature_values:
        subset = data[data.iloc[:, feature_index] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    
    # Ganancia de información
    return total_entropy - weighted_entropy

# Algoritmo ID3 para crear el árbol de decisión
def id3(data, features, depth=0, max_depth=5):
    # Si todos los ejemplos tienen la misma clase, devolver un nodo hoja
    if len(data.iloc[:, -1].unique()) == 1:
        return data.iloc[:, -1].iloc[0]
    
    # Si no hay más características o alcanzamos la profundidad máxima, devolver la clase más frecuente
    if len(features) == 0 or depth >= max_depth:
        return data.iloc[:, -1].mode()[0]
    
    # Calcular la ganancia de información para cada característica
    gains = [information_gain(data, feature) for feature in features]
    
    # Seleccionar la característica con la mayor ganancia de información
    best_feature = features[gains.index(max(gains))]
    
    # Crear el nodo del árbol
    tree = {best_feature: {}}
    
    # Dividir los datos en subconjuntos según los valores de la característica seleccionada
    feature_values = data[best_feature].unique()
    
    # Crear subárboles recursivamente
    for value in feature_values:
        subset = data[data[best_feature] == value]
        remaining_features = [f for f in features if f != best_feature]
        tree[best_feature][value] = id3(subset, remaining_features, depth + 1, max_depth)
    
    return tree

# Función para predecir usando el árbol de decisión
def predict(tree, example):
    if isinstance(tree, dict):
        feature = list(tree.keys())[0]
        value = example[feature]
        subtree = tree[feature].get(value, None)
        if subtree is not None:
            return predict(subtree, example)
        else:
            return None
    else:
        return tree

# Cargar el conjunto de datos 'tennis.csv' (asegurarse de que el archivo esté en el mismo directorio)
df = pd.read_csv('tennis.csv')

# Asumimos que la última columna es la clase a predecir
features = df.columns[:-1]

# Construir el árbol de decisión
tree = id3(df, features)

# Imprimir el árbol de decisión
print("Árbol de Decisión:")
print(tree)

# Ejemplo de predicción usando el árbol
example = df.iloc[0, :-1]  # Tomar un ejemplo del conjunto de datos
prediction = predict(tree, example)
print("Predicción para el primer ejemplo:", prediction)
