from django.db import models
from uuid import uuid4

from products.models import Product

def upload_profile_picture(instance, filename):
  return f"{instance.id_seller}-{filename}"

class Seller(models.Model):
    id_seller = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    company_product_type = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    company_picture = models.ImageField(upload_to=upload_profile_picture, blank=True, null=True)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    join_date = models.DateTimeField(auto_now_add=True)