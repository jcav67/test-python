""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""
from data import  get_companies,get_branches

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

print(result)