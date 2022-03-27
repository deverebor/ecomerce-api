import requests
from variables import ProductsVariables, UsersVariables, SellersVariables

"""
Helper to update an product information
"""

update_id = input("ID do you want to update: ")
endpoint = input("Endpoint: ")

try:
  update_id = int(update_id)
except:
  endpoint = None
  print(f'{update_id} id incorrect, please try again')

try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if endpoint == 'products' and update_id:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{update_id}/update/"

  get_response = requests.put(endpoint_url, json=ProductsVariables.data)
  print(get_response.json())
  
elif endpoint == 'users' and update_id:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{update_id}/update/"

  get_response = requests.put(endpoint_url, json=UsersVariables.data)
  print(get_response.json())
  
elif endpoint == 'sellers' and update_id:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{update_id}/update/"

  get_response = requests.put(endpoint_url, json=SellersVariables.data)
  print(get_response.json())
  
else:
  print(f'{endpoint} enpoint incorrect, please try again')