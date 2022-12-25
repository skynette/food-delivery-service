from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
