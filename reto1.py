from datetime import datetime

nacimientoAño = 1990
actual = datetime.now().year
edad = actual - nacimientoAño


nombre = input("¿Cuál es tu nombre? ")

nacimiento = int(input(f"¿En qué año naciste?"))
print(f'tienes {edad} años')

