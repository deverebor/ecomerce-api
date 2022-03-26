import requests
from helpers.variables import Variables

"""
Helper to update an product information
"""

endpoint = input("Endpoint: ")

try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if endpoint:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/1/update/"

  get_response = requests.put(endpoint_url, json=Variables.data)
  print(get_response.json())