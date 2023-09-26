from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Pet(models.Model):
    name = models.CharField(max_length=50)
    pet_type = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)