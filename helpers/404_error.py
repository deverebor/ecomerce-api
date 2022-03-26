import requests

"""
Helper to force 404 error
"""

fake_id = 99999
endpoint = input("Endpoint: ")

try:
    endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')
  
if endpoint:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/{fake_id}/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())