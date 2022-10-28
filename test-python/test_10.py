"""
  10) realice una consulta al archivo data.py, muestre todos los terceros, reduzca la 
  información y solo muestre el nombre, la ciudad y la identificacion, 
  ordenelos por su identificación
"""
from data import  get_thirds

thirds= get_thirds()
reduce_thirds= []

for third in thirds:
  #print(third)
  reduce_thirds.append({
    "name":" ".join([third['firstname']," ",third['lastname']," ",third['maidenname']]),
    "cityName": third["cityName"],
    "identificationNumber":third["identificationNumber"],
    "tradename": third["tradename"]
  })

sorted_reduce_thirds = sorted(reduce_thirds, key=lambda x: x['identificationNumber'])
print(sorted_reduce_thirds)