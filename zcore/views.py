import json
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class Home(APIView):
	"""
	Home details
	"""
	def get(self, request, *args, **kwargs):
		"""
		Returns biodata information
		"""
		data = {
			"message": "Hello, world",
		}
		return Response(data, status=status.HTTP_200_OK)

home = Home.as_view()


class UserDetails(APIView):
	"""
	User details
	"""
	permission_classes = [IsAuthenticated]
	def get(self, request, *args, **kwargs):
		user = User.objects.get(id=request.user.id)
		data = {
			"username": user.username,
		}
		return Response(data, status=200)

get_user_details = UserDetails.as_view()