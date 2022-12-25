from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Customer

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	location = models.CharField(max_length=255)

class MenuItem(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.IntegerField()

class Orders(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	status = models.CharField(max_length=255, choices=[("pending", "Pending"), ("in progress", "In Progress"), ("completed", "Completed")])
	delivery_address = models.CharField(max_length=255)
	total_price = models.IntegerField()

class OrderItems(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	quantity = models.IntegerField()

class Payments(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	amount = models.IntegerField()
	payment_method = models.CharField(max_length=255, choices=[("cash", "Cash"), ("card", "Card"), ("mobile money", "Mobile Money")])

class Review(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	review = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = [('customer_id', 'restaurant_id')]