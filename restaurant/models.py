from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Customer

ORDER_CHOICES = [
	("pending", "Pending"), 
	("in progress", "In Progress"), 
	("completed", "Completed")
]

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=255)
	delivery_fee = models.IntegerField()
	average_delivery_time = models.FloatField()
	minimum_order_value = models.IntegerField()
	location = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class MenuItem(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.IntegerField()

	def __str__(self):
		return f"{self.name} at {self.restaurant}"

class Orders(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	status = models.CharField(max_length=255, choices=ORDER_CHOICES)
	delivery_address = models.CharField(max_length=255)
	total_price = models.IntegerField()

	def __str__(self):
		return f"Order #{self.pk} for {self.customer} at {self.restaurant}"

class OrderItems(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.quantity} of {self.menu_item} for Order #{self.order.pk}"

class Review(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	review = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.customer}'s review of {self.restaurant}"

	class Meta:
		unique_together = [('customer_id', 'restaurant_id')]