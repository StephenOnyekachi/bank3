
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Users(models.Model):
class Users(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    number = models.IntegerField(default=0, null=True)
    balance = models.IntegerField(default=0, null=True)
    block = models.BooleanField(default=False)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    account = models.IntegerField(default=1, null=True)
    type = models.TextField(null=True)
    fund = models.IntegerField(default=1111, null=True)

    def __str__(self):
        return self.username
