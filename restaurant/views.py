from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from restaurant.permissions import IsOwner
from .serializers import MenuItemSerializer, OrdersSerializer, OrderItemsSerializer, RestaurantSerializer
from .models import MenuItem, Orders, OrderItems, Restaurant

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


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


# make sure only owner of restaurant is allowed to
# create a menu item
class MenuListView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# make sure only owner of restaurant is allowed to
# edit a menu item
class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderItemListView(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
