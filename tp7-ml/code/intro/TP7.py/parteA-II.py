# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df = pd.read_csv('arbolado-mendoza-dataset-train.csv')

# Mostrar las primeras filas del DataFrame para explorar los datos
print(df.head())

# Paso 1: Distribución de la clase inclinacion_grave
# Contar la frecuencia de cada clase en la columna 'inclinacion_peligrosa'
inclinacion_counts = df['inclinacion_peligrosa'].value_counts()

# Crear un gráfico de barras para la distribución de 'inclinacion_peligrosa'
plt.figure(figsize=(8, 6))
sns.countplot(x='inclinacion_peligrosa', data=df, palette='viridis')
plt.title('Distribución de la Clase Inclinación Peligrosa')
plt.xlabel('Inclinación Peligrosa (0: No, 1: Sí)')
plt.ylabel('Frecuencia')
plt.show()

# Paso 2: ¿Se puede considerar alguna sección más peligrosa que otra?
# Agrupar por 'seccion' y calcular el porcentaje de inclinación peligrosa en cada sección
secciones_inclinacion = df.groupby('seccion')['inclinacion_peligrosa'].mean() * 100

# Crear un gráfico de barras para el porcentaje de inclinación peligrosa por sección
plt.figure(figsize=(12, 6))
secciones_inclinacion.sort_values(ascending=False).plot(kind='bar', color='salmon')
plt.title('Porcentaje de Árboles con Inclinación Grave por Sección')
plt.xlabel('Sección Administrativa')
plt.ylabel('Porcentaje de Inclinación Grave (%)')
plt.show()

# Paso 3: ¿Se puede considerar alguna especie más peligrosa que otra?
# Agrupar por 'especie' y calcular el porcentaje de inclinación peligrosa para cada especie
especies_inclinacion = df.groupby('especie')['inclinacion_peligrosa'].mean() * 100

# Crear un gráfico de barras para el porcentaje de inclinación peligrosa por especie
plt.figure(figsize=(12, 6))
especies_inclinacion.sort_values(ascending=False).plot(kind='bar', color='lightblue')
plt.title('Porcentaje de Árboles con Inclinación Peligrosa por Especie')
plt.xlabel('Especie del Árbol')
plt.ylabel('Porcentaje de Inclinación Peligrosa (%)')
plt.show()
