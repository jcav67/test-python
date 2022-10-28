"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a tener todos los terceros que pertenezcan a esa compañia
"""
from data import get_companies, get_thirds

companies= get_companies()
thirds = get_thirds()
company_thirds=[]
companies_complete=[]
sorted_companies = sorted(companies, key=lambda x: x['name'])

#print(sorted_companies)

for company in sorted_companies:
  for third in thirds:

    if(company['id'] == third['companyid']):
      company_thirds.append(third)

  company['third']=company_thirds
  companies_complete.append(company)

print(companies_complete)
