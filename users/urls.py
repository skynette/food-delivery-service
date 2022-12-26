from django.urls import path
from . import views


urlpatterns = [
	path('details/<int:pk>/', views.get_user_details),
]