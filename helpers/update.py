import requests
from helpers.variables import Variables

"""
Helper to update an product information
"""

endpoint = "http://localhost:8000/api/v1/products/1/update/"

get_response = requests.put(endpoint, json=Variables.data)
print(get_response.json())