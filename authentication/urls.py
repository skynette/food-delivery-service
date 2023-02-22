from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from django.urls import include, path
from . import views


urlpatterns = [
    path('register/', views.registration_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('change-password/', views.change_password_api_view,  name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
