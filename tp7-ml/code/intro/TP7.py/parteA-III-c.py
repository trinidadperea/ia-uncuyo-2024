import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("arbolado-mendoza-dataset-train.csv")

# Verificar las primeras filas para asegurarnos de que la columna 'circ_tronco_cm' y 'inclinacion_peligrosa' existen
print(df.head())

# Asegurarse de que las columnas necesarias están limpias
df = df.dropna(subset=['circ_tronco_cm', 'inclinacion_peligrosa'])  # Eliminar filas con valores nulos
df['circ_tronco_cm'] = pd.to_numeric(df['circ_tronco_cm'], errors='coerce')  # Convertir 'circ_tronco_cm' a numérico

# Asegurarse de que la variable 'inclinacion_peligrosa' sea una categoría
df['inclinacion_peligrosa'] = df['inclinacion_peligrosa'].astype(str)

# Generar histogramas con diferentes números de bins, separados por la variable 'inclinacion_peligrosa'
bins_values = [10, 20, 30, 50, 100]

# Crear subgráficos para diferentes números de bins y para cada clase de 'inclinacion_peligrosa'
plt.figure(figsize=(14, 10))

# Loop sobre las clases de la variable 'inclinacion_peligrosa'
for i, (inclinacion_class, group) in enumerate(df.groupby('inclinacion_peligrosa'), start=1):
    plt.subplot(len(df['inclinacion_peligrosa'].unique()), len(bins_values), i)  # Subgráficos
    for bins in bins_values:
        plt.hist(group['circ_tronco_cm'], bins=bins, edgecolor='black', alpha=0.7)
        plt.title(f'{inclinacion_class} - {bins} bins')
        plt.xlabel('Circunferencia del tronco (cm)')
        plt.ylabel('Frecuencia')

plt.tight_layout()  # Ajustar el diseño
plt.show()
