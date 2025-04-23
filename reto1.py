from datetime import datetime

#nacimientoAño = 1990
actual = datetime.now().year


nombre = input("¿Cuál es tu nombre? ")

nacimiento = int(input(f"¿En qué año naciste?"))
edad = actual - nacimiento 
print(f'tienes {edad} años')

