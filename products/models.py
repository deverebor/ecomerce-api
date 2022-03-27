from django.db import models
from uuid import uuid4

def upload_image_book(instance, filename):
  return f"{instance.id_product}-{filename}"

class Product(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    validate_day = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_book, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=00.00)