import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)

# create either customer profile or restaurant owner profile
# might also have restaurant staff profile

# @receiver(post_save, sender=User)
# def create_customer_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Customer.objects.create(user=instance)
# 		logger.info("User Profile created")
