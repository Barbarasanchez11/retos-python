from datetime import datetime

desayuno = 'café + tostadas'
comida = 'ensalada y sopa'
merienda = 'fruta + café'
cena = 'sandwich'
noEsHora = 'no es hora de comer'

hora = datetime.now().hour


if 8 <= hora < 10:
    toca = desayuno
    
elif 13 <= hora < 16:
    toca = comida  
    
elif 17 <= hora < 18:
    toca = merienda  
    
elif 20 <= hora < 23:
    toca = cena    
    
else:
   
    toca = noEsHora        
print(f'son las {hora} , es momento de {toca}')    
    
