from rest_framework import serializers

from .models import Seller


class SellersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seller
    fields = [
      'product',
      'name',
      'company_name',
      'company_product_type',
      'email',
      'password',
      'company_picture',
      'country',
      'city',
      'join_date',
    ]