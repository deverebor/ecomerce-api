import requests

"""
Helper to force 404 error
"""

fake_product_id = 99999

endpoint = f"http://localhost:8000/api/v1/products/{fake_product_id}/"

get_response = requests.get(endpoint)
print(get_response.json())