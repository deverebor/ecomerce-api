from rest_framework import serializers

from .models import User


class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'product',
      'name',
      'last_name',
      'email',
      'password',
      'profile_picture',
      'country',
      'city',
      'join_date',
    ]