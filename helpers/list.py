import requests

"""
Helper to list all products
"""

endpoint = "http://localhost:8000/api/v1/products/"

get_response = requests.get(endpoint)
print(get_response.json())