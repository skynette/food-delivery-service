from django.db import models
from restaurant.models import Orders


PAYMENT_CHOICES = [
	("cash", "Cash"), 
	("card", "Card"), 
	("mobile money", "Mobile Money")
]

class Payments(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	amount = models.IntegerField()
	payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES)

	def __str__(self):
		return f"Payment ID: {self.id} | Order ID: {self.order.id} | Amount: {self.amount} | Payment Method: {self.payment_method}"
		