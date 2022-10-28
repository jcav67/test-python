"""
  4) Mostrar de los terceros que se tienen en el archivo data.py 
  los cuales no poseen ni email o no tengan cellPhone.
"""
from data import  get_thirds

thirds = get_thirds()

for third in thirds:
  if not third['email'] or not third['cellPhone']:
    print(third)