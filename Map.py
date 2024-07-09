import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
# Asegúrate de que el archivo está en el mismo directorio o proporciona la ruta completa
df = pd.read_csv('democracy-eiu.csv')

# Ver las primeras filas del dataset
print(df.head())

# Estadísticas descriptivas
print(df.describe())

# Histograma del índice de democracia
plt.hist(df['democracy_eiu'], bins=20, edgecolor='black')
plt.title('Distribución del Índice de Democracia')
plt.xlabel('Índice de Democracia')
plt.ylabel('Frecuencia')
plt.show()

# Mapa del índice de democracia (suponiendo que el dataset tiene columnas 'country' y 'democracy_index')
import geopandas as gpd

# Cargar un shapefile del mundo
world = gpd.read_file('ne_110m_admin_0_countries.shp')

# Unir el shapefile con el dataframe del índice de democracia
world = world.merge(df, how='left', left_on='NAME', right_on='Entity')

# Crear el mapa
world.plot(column='democracy_eiu', legend=True,
           legend_kwds={'label': "Índice de Democracia",
                        'orientation': "horizontal"})
plt.title('Índice de Democracia por País')
plt.show()