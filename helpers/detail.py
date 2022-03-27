import requests

"""
Helper to view an determinated detail product
"""

searched_id = input("What ID do you want to search: ")
endpoint = input("Endpoint: ")

try:
  searched_id = int(searched_id)
except:
  endpoint = None
  print(f'{searched_id} id incorrect, please try again')

try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if endpoint == 'products' and searched_id:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{searched_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())
  
elif endpoint == 'users' and searched_id:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{searched_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())
  
elif endpoint == 'sellers' and searched_id:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{searched_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())
  
else:
  print(f'{endpoint} enpoint incorrect, please try again')