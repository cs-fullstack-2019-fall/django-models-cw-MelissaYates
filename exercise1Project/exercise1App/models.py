from django.db import models

# Create your models here.
from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class Account(models.Model):
    username = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField(default=0)
    balance = models.DecimalField(max_digits = 10, decimal_places = 3)
