import re

regex = r'^(?![._])(?!.*[._]{2})[a-zA-Z0-9._]+(?<![._])@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'


while True:
    email = input('Introduce tu email: ')

    if re.match(regex, email):
     print('El correo es correcto')
     break
    else:
        print('El correo es inválido')    
    