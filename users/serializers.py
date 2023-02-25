from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'password']
