from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# models.py


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Chef(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
