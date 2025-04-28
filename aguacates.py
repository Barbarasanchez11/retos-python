import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

aguacates = [500, 520, 510, 530, 580, 590, 640, 620, 600, 580, 575, 550]

media = np.mean(aguacates)
mediana = np.median(aguacates)
moda = stats.mode(aguacates)
desviacion = np.std(aguacates)
coeficiente = (desviacion / media) * 100



mas_pesado = max(aguacates)
mas_ligero = min(aguacates)

rango_bajo = 400
rango_alto = 600

aguacates_en_rango = [peso for peso in aguacates if rango_bajo <= peso <= rango_alto]
cantidad_en_rango = len(aguacates_en_rango)

print(f"Media del peso: {media:.2f} gramos")
print(f"Mediana del peso: {mediana:.2f} gramos")
print(f"Moda del peso: {moda} gramos")
print(f"Desviación estándar: {desviacion:.2f} gramos")
print(f"Coeficiente de variación: {coeficiente:.2f}%")
print(f"Aguacate más pesado: {mas_pesado} gramos")
print(f"Aguacate más ligero: {mas_ligero} gramos")
print(f"Cantidad de aguacates en el rango ideal ({rango_bajo}-{rango_alto}g): {cantidad_en_rango}")

plt.hist(aguacates, bins=10, color='blue', alpha=0.7)
plt.title("Distribución de pesos de los aguacates")
plt.xlabel("Peso (gramos)")
plt.ylabel("Frecuencia")
plt.show()


plt.boxplot(aguacates, vert=False)
plt.title("Gráfico de caja de los aguacates")
plt.xlabel("Peso (gramos)")
plt.show()