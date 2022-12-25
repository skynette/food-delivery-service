from rest_framework import serializers
from .models import Restaurant, MenuItem, Orders, OrderItems, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'email', 'phone', 'password', 'location']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'name', 'description', 'price']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'customer', 'restaurant', 'status', 'delivery_address', 'total_price']

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id', 'order', 'menu_item', 'quantity']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer', 'restaurant', 'rating', 'review', 'date']
