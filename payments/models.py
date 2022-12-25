from django.db import models
from restaurant.models import Orders

class Payments(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	amount = models.IntegerField()
	payment_method = models.CharField(max_length=255, choices=[("cash", "Cash"), ("card", "Card"), ("mobile money", "Mobile Money")])

	def __str__(self):
		return f"Payment ID: {self.id} | Order ID: {self.order_id} | Amount: {self.amount} | Payment Method: {self.payment_method}"