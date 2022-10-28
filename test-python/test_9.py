"""
9) realice una consulta al archivo data.py, muestre todos los items, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente,
  en caso de que esté lo tenga. 
  
  El resultado del ordenando debe ser así, en la parte inicial los items 
  que no tienen color y en la parte final los que si tienen color, todo dentro de
  un mismo objeto
"""
from data import  get_items,get_colors

items = get_items()
colors = get_colors()
full_items = []
sorted_items=[]

for item in items:
  if(int(item['code']) % 2 ==0):

    print(item)

  for color in colors:
    if(item['color'] and item['color']== color['colorCode']):

      item['colorName'] = color['colorName']

    else:
      item['colorName'] = ""
      
  full_items.append(item)
  
sorted_items = sorted(full_items, key=lambda x: x['colorName'],reverse = True)
print(sorted_items)