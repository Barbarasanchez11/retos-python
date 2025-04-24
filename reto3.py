import random

jugadores = ['Alcaraz', 'Djokovic', 'Zverez', 'Medvedev', 'Tsisipas', 'Rune', 'Rublev', 'Fritz']

def partido(j1,j2):
    ganador = random.choice([j1,j2])
    print(f'{j1} vs {j2} Ganador:{ganador}')
    return ganador

partido('Alcaraz','Djokovic')