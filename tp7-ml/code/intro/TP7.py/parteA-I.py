import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df = pd.read_csv("arbolado-mza-dataset.csv")

# Mezclar los datos de manera aleatoria
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Calcular el tamaño de la división (20% para validación y 80% para entrenamiento)
split_index = int(0.2 * len(df_shuffled))

# Crear subconjuntos
df_validation = df_shuffled[:split_index]
df_train = df_shuffled[split_index:]

# Guardar en archivos separados
df_validation.to_csv("arbolado-mendoza-dataset-validation.csv", index=False)
df_train.to_csv("arbolado-mendoza-dataset-train.csv", index=False)

print("Los archivos se han creado exitosamente.")

