from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid

class User(AbstractUser):
	class Role(models.TextChoices):
		ADMIN = "ADMIN", "Admin"
		OWNER = "OWNER", "Owner"
		STAFF = "STAFF", "Staff"
		CUSTOMER = "CUSTOMER", "Customer"

	base_role = Role.ADMIN

	pkid = models.BigAutoField(_("primary key id"), primary_key=True, editable=False)
	id = models.UUIDField(_("Id"), default=uuid.uuid4, editable=False, unique=True)
	email = models.EmailField(_('email address'), unique=True)
	username = models.CharField(_('username'), max_length=50, blank=True, null=True, unique=True)
	role = models.CharField(_("User role or type"),max_length=50, choices=Role.choices)
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

	def save(self, *args, **kwargs):
		if not self.pk:
			self.role = self.base_role
			return super().save(*args, **kwargs)


"""
implement proxy models for 4 user types
"""


class Customer(User):
	base_role = User.Role.CUSTOMER
		
	class Meta:
		proxy = True
		ordering = ('first_name',)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Owner(User):
	base_role = User.Role.OWNER
		
	class Meta:
		proxy = True
		ordering = ('first_name',)

	def __str__(self):
		return f"{self.first_name}"


class Staff(User):
	base_role = User.Role.STAFF
		
	class Meta:
		proxy = True
		ordering = ('username',)

	def __str__(self):
		return f"{self.first_name}"
