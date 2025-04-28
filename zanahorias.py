#Un grupo de agricultores está participando en un concurso para ver quién tiene las zanahorias más grandes. Han medido el peso (en gramos) de 12 zanahorias y necesitan analizar los datos para ver qué tan uniformes son sus cultivos.


#📌 Tu misión
#📊 Escribe un programa en Python que haga lo siguiente:
#Calcule la media (promedio) del peso de las zanahorias.
#Encuentre la mediana del peso.
#Determine la moda (peso más común).Calcule la desviación estándar para ver qué tanto varían los pesos.
#zanahorias = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]
#📊 Extra 1: Agrega una visualización con Matplotlib 📉 para mostrar la distribución de los pesos.
#🤖 Extra 2: Modifica el código para que el usuario pueda ingresar los pesos de nuevas zanahorias.

import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

nuevoPeso = input("Ingresa los pesos de las zanahorias  ")
zanahorias = list(map(int, nuevoPeso.split()))

print(zanahorias[1])

#zanahorias = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]

media = np.mean(zanahorias)
mediana = np.median(zanahorias)
moda= stats.mode(zanahorias)
desviacion= np.std(zanahorias)

print(f'media, {media}')
print(f'mediana, {mediana}')
print(f'moda, {moda}')
print(f'desviacion, {desviacion:.2f}')

plt.hist(zanahorias)
plt.title("Distribución de las zanahorias")
plt.xlabel("Peso (gr)")
plt.ylabel("Frecuencia")
plt.show()


