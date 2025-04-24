import random


jugadores = ['Alcaraz', 'Djokovic', 'Zverev', 'Medvedev', 'Tsitsipas', 'Rune', 'Rublev', 'Fritz']


def partido(j1, j2):
    ganador = random.choice([j1, j2])
    print(f'{j1} vs {j2} , Ganador: {ganador}')
    return ganador


print('Cuartos de final:')
semi_finalistas = []
for i in range(0, len(jugadores), 2):
    ganador = partido(jugadores[i], jugadores[i+1])
    semi_finalistas.append(ganador)


print('Semifinales:')
finalistas = []
for i in range(0, len(semi_finalistas), 2):
    ganador = partido(semi_finalistas[i], semi_finalistas[i+1])
    finalistas.append(ganador)


print('Final:')
campeon = partido(finalistas[0], finalistas[1])


print(f'El campeón del torneo es: {campeon.upper()}!')

      