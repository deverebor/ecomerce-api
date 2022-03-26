import requests

"""
Helper to view an determinated detail product
"""

endpoint = "http://localhost:8000/api/v1/products/1/"

get_response = requests.get(endpoint)
print(get_response.json())