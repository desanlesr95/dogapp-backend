from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.conf import settings

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=150)
    mail = models.CharField(max_length=150,unique=True)
    phone = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=60)
    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['name','password']



class Pet(models.Model):
    name = models.CharField(max_length=50)
    pet_type = models.BooleanField(default=None, null=True)
    gender = models.BooleanField(default=None, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=40)
