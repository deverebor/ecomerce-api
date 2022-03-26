import requests
from variables import Variables

"""
Helper to create an products
"""

endpoint = "http://localhost:8000/api/v1/products/"

get_response = requests.post(endpoint, json=Variables.data)
print(get_response.json())