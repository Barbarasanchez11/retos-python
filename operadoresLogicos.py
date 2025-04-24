calor = True
negacion = not calor

print(f'inicial: {calor}')
print(f'negacion de la proposicion inicial: {negacion}')


#and deben ser las dos verdaderas si no da false
proposicion1 = True
proposicion2 = False

conjuncion = proposicion1 and proposicion2

print(f'proposicion1: {proposicion1}')
print(f'proposicion2: {proposicion2}')
print (f'{conjuncion}')



proposicion1 = True
proposicion2 = False

disyuncion = proposicion1 or proposicion2

print(f'proposicion1: {proposicion1}')
print(f'proposicion2: {proposicion2}')
print (f'{disyuncion}')

# Ejemplo 1: "Si llueve, entonces llevaré un paraguas"
llueve = True
llevar_paraguas = llueve  # Implicación: si llueve implica llevar paraguas
print(f"Si llueve {llueve}, entonces llevaré un paraguas: {llevar_paraguas}")
# Ejemplo 2: "Si estudio, entonces aprobaré el examen"
estudio = False
aprobar_examen = estudio or not estudio  # Implicación: si estudio implica aprobar o no estudiar equivale a aprobar
print(f"Si estudio {estudio}, entonces aprobaré el examen: {aprobar_examen}")
# Ejemplo 3: "Si como chocolate, entonces estaré feliz"
come_chocolate = True
feliz = come_chocolate  # Implicación: comer chocolate implica estar feliz
print(f"Si como chocolate {come_chocolate}, entonces estaré feliz: {feliz}")