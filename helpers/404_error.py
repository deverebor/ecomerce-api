import requests

"""
Helper to force 404 error
"""

fake_id = 999999
endpoint = input("Endpoint: ")

try:
    endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')
  
if endpoint == 'products':
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{fake_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())
  
elif endpoint == 'users':
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{fake_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())
  
elif endpoint == 'sellers':
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{fake_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())
  
else:
  print(f'{endpoint} enpoint incorrect, please try again')