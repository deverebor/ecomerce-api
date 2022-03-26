import requests

"""
Helper to view an determinated detail product
"""

endpoint = input("Endpoint: ")

try:
  endpoint = str(endpoint)
except:
  endpoint = None
  print(f'{endpoint} enpoint incorrect, please try again')

if endpoint:
  endpoint_url = f"http://localhost:8000/api/v1/{endpoint}/1/"

  get_response = requests.get(endpoint_url)
  print(get_response.json())