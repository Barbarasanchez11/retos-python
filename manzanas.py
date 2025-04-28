import numpy as np
import statistics as stats

manzanas = [150,180,200,170,150,190,200,210,150,180]

media = np.mean(manzanas)
mediana = np.median(manzanas)
moda = stats.mode(manzanas)
desviacion = np.std(manzanas)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print(f"Desviación estándar: {desviacion:.2f}")
