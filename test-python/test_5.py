"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""
from data import  get_thirds,get_companies

companies = get_companies()
thirds = get_thirds()
thids_sorted_by_name=[]

for third in thirds:
  if(third['firstname']):
    thids_sorted_by_name.append({
      'name':" ".join([third['firstname']," ",third['lastname']," ",third['maidenname']]),
      'id':third['companyid']
      })
  else:
    thids_sorted_by_name.append({
      'name': third['tradename'],
      'id':third['companyid']
      })
sorted_list = sorted(thids_sorted_by_name, key=lambda x: x['name'])
complete_list=[]

for elem in sorted_list:
  for company in companies:
    if elem['id'] == company['id']:
      elem['companyname'] = company['name']
    else:
      elem['companyname'] = ""
  complete_list.append(elem)
print(complete_list)