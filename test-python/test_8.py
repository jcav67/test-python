"""
  8) realice una consulta al archivo data.py, muestre los items donde su codigo sea un número PAR,
  ordenelos por el precio de manera descendente y dentro de cada item 
  agregue el color correspondiente, si lo tiene.
"""
from numpy import int32
from data import  get_items,get_colors

items = get_items()
colors = get_colors()
full_items = []
sorted_items=[]

for item in items:
  if(int32(item['code']) % 2 ==0):

    print(item)

  for color in colors:
    if(item['color'] and item['color']== color['colorCode']):

      item['colorName'] = color['colorName']
    else:
      item['colorName'] = ""
  full_items.append(item)
  
sorted_items = sorted(full_items, key=lambda x: x['price'],reverse = True)
print(sorted_items)
    