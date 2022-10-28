"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import  get_thirds

thirds = get_thirds()
sorted_names=[]

for third in thirds:
  if(third['firstname']):
    sorted_names.append("".join([third['firstname']," ",third['lastname']," ",third['maidenname']]))
  else:
    sorted_names.append(third['tradename'])
sorted_names.sort()
print(sorted_names)