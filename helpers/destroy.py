import requests

"""
Helper to destroy an product
"""

id_product = input("What product do you want to destroy? ")
endpoint = input("Endpoint: ")

try:
    id_product = int(id_product)
except:
    id_product = None
    print(f'{id_product} is not a valid product id')
    
try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if id_product or endpoint:
    endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{id_product}/destroy/"

    get_response = requests.delete(endpoint_url)
    print(get_response.status_code, get_response.status_code == 204)