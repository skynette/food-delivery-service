from rest_framework import serializers
from .models import Restaurant, MenuItem, Orders, OrderItems, Review

class RestaurantSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        # fields = ['id', 'name', 'email', 'phone', 'delivery_fee', 'average_delivery_time', 'minimum_order_value', 'location', 'rating']
        fields = ['id', 'name', 'email', 'phone', 'delivery_fee', 'average_delivery_time', 'minimum_order_value', 'rating']

    def get_rating(self, obj):
        # Get all the reviews for this restaurant
        reviews = Review.objects.filter(restaurant=obj)
        # Calculate the average rating
        if reviews.count() > 0:
            rating = sum([r.rating for r in reviews]) / reviews.count()
        else:
            rating = 0
        return rating

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
