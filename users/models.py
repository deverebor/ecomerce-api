from django.db import models
from uuid import uuid4
from products.models import Product

def upload_profile_picture(instance, filename):
  return f"{instance.id_user}-{filename}"

class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, blank=True, null=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    profile_picture = models.ImageField(upload_to=upload_profile_picture, blank=True, null=True)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    join_date = models.DateTimeField(auto_now_add=True)