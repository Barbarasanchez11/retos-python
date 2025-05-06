import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("/Users/barbarasanchezurbano/Downloads/ventas.csv")

# Mostrar las primeras filas
print(df.head())

# Calcular la columna 'total' (ingresos por fila)
df['total'] = df['precio'] * df['unidades']
print(df.head())

# Agrupar por producto y sumar los ingresos
ingresos_por_producto = df.groupby('producto')['total'].sum()

# Convertir la fecha a formato datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Extraer el mes
df['mes'] = df['fecha'].dt.month
print(df.head())

# Agrupar por mes y sumar los ingresos
print(df.groupby('mes')['total'].sum())

# Filtrar por unidades mayores a 3
print(df[df['unidades'] > 3])

# Gráfico de barras: Ingresos por producto
plt.figure(figsize=(10, 6))
ingresos_por_producto.plot(kind='bar', color='skyblue')
plt.title('Ingresos por Producto')
plt.xlabel('Producto')
plt.ylabel('Ingresos Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histograma: Frecuencia de ingresos por fila
plt.figure(figsize=(10, 6))
plt.hist(df['total'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Frecuencia de Ingresos por Fila')
plt.xlabel('Ingresos por Fila')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()