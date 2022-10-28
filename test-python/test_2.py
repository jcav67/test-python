"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""

from data import  get_companies,get_branches

def branches_info():
  companies= get_companies();
  branches= get_branches();
  temp_arr=[]
  result = {}

  for company in companies:
    temp_arr = []
    for branch_per_company in company['branches']:
      for branch in branches:
        if(branch['id'] == branch_per_company):
          temp_arr.append(branch['name'])
    company['sucursales']=temp_arr
    result[company['id']] = company

  return result

branches = branches_info()
print(branches)