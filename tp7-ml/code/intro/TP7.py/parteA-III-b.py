import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("arbolado-mendoza-dataset-train.csv")

# Verificar las primeras filas para asegurarnos de que la columna 'circ_tronco_cm' existe
print(df.head())

# Asegurarse de que la columna 'circ_tronco_cm' está limpia (sin valores nulos o erróneos)
df = df.dropna(subset=['circ_tronco_cm'])  # Eliminar valores nulos
df['circ_tronco_cm'] = pd.to_numeric(df['circ_tronco_cm'], errors='coerce')  # Convertir a numérico, si es necesario

# Generar histogramas con diferentes números de bins
bins_values = [10, 20, 30, 50, 100]

plt.figure(figsize=(12, 8))  # Ajusta el tamaño de la figura

# Crear subgráficos para diferentes números de bins
for i, bins in enumerate(bins_values, start=1):
    plt.subplot(2, 3, i)  # 2 filas, 3 columnas de subgráficos
    plt.hist(df['circ_tronco_cm'], bins=bins, edgecolor='black', alpha=0.7)
    plt.title(f'Histograma con {bins} bins')
    plt.xlabel('Circunferencia del tronco (cm)')
    plt.ylabel('Frecuencia')

plt.tight_layout()  # Ajustar el diseño para que no se sobrepongan los gráficos
plt.show()
