import pandas as pd

# Cargar el archivo CSV original
df = pd.read_csv("arbolado-mendoza-dataset-train.csv")

# Verificar las primeras filas
print(df.head())

# Asegurarse de que 'circ_tronco_cm' sea numérica y eliminar valores nulos
df['circ_tronco_cm'] = pd.to_numeric(df['circ_tronco_cm'], errors='coerce')
df = df.dropna(subset=['circ_tronco_cm'])

# Definir los puntos de corte para las categorías basadas en los resultados de los histogramas
# Aquí asumimos que los puntos de corte se determinan a partir de los percentiles, pero pueden ser ajustados según el histograma
cut_points = [0, 30, 60, 100, float('inf')]  # Ejemplo de puntos de corte (bajo, medio, alto, muy alto)
labels = ['bajo', 'medio', 'alto', 'muy alto']

# Crear la nueva columna categórica
df['circ_tronco_cm_cat'] = pd.cut(df['circ_tronco_cm'], bins=cut_points, labels=labels, right=False)

# Verificar el nuevo dataframe
print(df[['circ_tronco_cm', 'circ_tronco_cm_cat']].head())

# Guardar el nuevo dataframe en un archivo CSV
df.to_csv("arbolado-mendoza-dataset-circ_tronco_cm-train.csv", index=False)
