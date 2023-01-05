from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order-items/', views.OrderItemListView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailView.as_view(), name='order-item-detail'),
]
