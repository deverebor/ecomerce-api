import requests
from variables import Variables

"""
Helper to create an products
"""

endpoint = input("Endpoint: ")

try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if endpoint:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/"

  get_response = requests.post(endpoint_url, json=Variables.data)
  print(get_response.json())