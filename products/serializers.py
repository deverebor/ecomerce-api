from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [
      'user',
      'seller'
      'name',
      'description',
      'validate_day',
      'image',
      'price',
    ]