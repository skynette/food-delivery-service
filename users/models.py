from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

class User(AbstractUser):
	pkid = models.BigAutoField(_("primary key id"), primary_key=True, editable=False)
	id = models.UUIDField(_("Id"), default=uuid.uuid4, editable=False, unique=True)
	email = models.EmailField(_('email address'), unique=True)
	username = models.CharField(_('username'), max_length=50, blank=True, null=True, unique=True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	objects = CustomUserManager()

	class Meta:
		verbose_name = _('User')
		verbose_name_plural = _('Users')

	def __str__(self):
		return f"{self.username}"

	@property
	def get_full_name(self) -> str:
		return f"{self.first_name.title()} {self.last_name.title()}"
	
	def get_short_name(self) -> str:
		return f"{self.username}"


"""
imlement proxy models for 3 user types
"""
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=255)
	address = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"