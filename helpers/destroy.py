import requests

"""
Helper to destroy an product
"""

id_product = input("What product do you want to destroy? ")
try:
    id_product = int(id_product)
except:
    id_product = None
    print(f'{id_product} is not a valid product id')

if id_product:
    endpoint = f"http://localhost:8000/api/v1/products/{id_product}/destroy/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)