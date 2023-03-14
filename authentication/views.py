from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import MyTokenObtainPairSerializer, RegistrationSerializer
from authentication.utils import get_tokens_for_user
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated


class RegistrationAPIView(generics.GenericAPIView):
	# serializer_class = RegistrationSerializer

	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			username = serializer.data['username']
			user = User.objects.get(username=username)
			tokens = get_tokens_for_user(user)
			return Response({"user": serializer.data, "auth": tokens}, status=status.HTTP_201_CREATED)
		return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


registration_view = RegistrationAPIView.as_view()


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


login_view = MyTokenObtainPairView.as_view()

# change password view


class ChangePasswordView(generics.UpdateAPIView):

	serializer_class = ChangePasswordSerializer
	model = User
	permission_classes = (IsAuthenticated,)

	def get_object(self, queryset=None):
		obj = self.request.user
		return obj

	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			# Check old password
			if not self.object.check_password(serializer.data.get("old_password")):
				return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
			
			# set_password also hashes the password that the user will get
			self.object.set_password(serializer.data.get("new_password"))
			self.object.save()
			response = {
				'status': 'success',
				'message': 'Password updated successfully',
				'data': []
			}

			return Response(response, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

change_password_api_view = ChangePasswordView.as_view()