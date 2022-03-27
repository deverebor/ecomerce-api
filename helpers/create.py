import requests
from variables import ProductsVariables, UsersVariables, SellersVariables

"""
Helper to create an products
"""

endpoint = input("Endpoint: ")

try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if endpoint == 'products':
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/"

  get_response = requests.post(endpoint_url, json=ProductsVariables.data)
  print(get_response.json())
  
elif endpoint == 'users':
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/"

  get_response = requests.post(endpoint_url, json=UsersVariables.data)
  print(get_response.json())
  
elif endpoint == 'sellers':
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/"

  get_response = requests.post(endpoint_url, json=SellersVariables.data)
  print(get_response.json())
  
else:
  print(f'{endpoint} enpoint incorrect, please try again')
