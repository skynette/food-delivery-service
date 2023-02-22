from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemListView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-detail'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('orders/create', views.CreateOrderView.as_view(), name='order-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order-items/', views.OrderItemListView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailView.as_view(), name='order-item-detail'),

    #restaurant creation
    path('create/', views.RestaurantCreateView.as_view(), name='create-restaurant'),
    path('list/', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    
]
