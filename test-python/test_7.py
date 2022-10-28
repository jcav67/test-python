"""
  7) realice una consulta al archivo data.py, muestre los items que tienen colores 
  y ordenelos por precio de manera ascendente
"""
from data import  get_items

items = get_items()
items_with_color = []
sorted_items=[]

for item in items:
  if(item['color']):
    print(item)
    items_with_color.append(item)

sorted_items = sorted(items_with_color, key=lambda x: x['price'])
print(sorted_items)