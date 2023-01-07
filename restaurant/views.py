from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from restaurant.permissions import IsOwner
from .serializers import MenuItemSerializer, OrdersSerializer, OrderItemsSerializer, RestaurantSerializer
from .models import MenuItem, Orders, OrderItems, Restaurant
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from django.core.exceptions import PermissionDenied


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["name", "location"]
    ordering_fields = ["name", "location"]
    search_fields = ["name", "location"]


class RestaurantDetailView(generics.RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'pk'


class OrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.filter(customer=self.request.user)


class CreateOrderView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class UpdateOrderView(generics.UpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # Check if the order status is being updated to "completed"
        if self.request.data.get('status') == 'completed':
            # Calculate the total price of the order
            total_price = 0
            for item in self.get_object().items.all():
                total_price += item.price
        serializer.save()

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'


class MenuItemCreateView(generics.CreateAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        restaurant = get_object_or_404(Restaurant, pk=self.kwargs.get('pk'))
        if self.request.user == restaurant.owner:
            serializer.save(restaurant=restaurant)
        else:
            raise PermissionDenied


# make sure only owner of restaurant is allowed to
# create a menu item
class MenuItemListView(generics.RetrieveAPIView):
    """
    Gets the menu items for a given restaurant
    """
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        restaurant = self.kwargs['restaurant_pk']
        return MenuItem.objects.filter(restaurant=restaurant)


# make sure only owner of restaurant is allowed to
# edit a menu item
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderItemListView(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
