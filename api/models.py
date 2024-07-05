from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, mail, password=None, **extra_fields):
        if not mail:
            raise ValueError('The Email field must be set')
        mail = self.normalize_email(mail)
        user = self.model(mail=mail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mail, password, **extra_fields)
        

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=150)
    mail = models.CharField(max_length=150,unique=True)
    phone = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=60)
    objects = UserManager()

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['name', 'lastname']


    def __str__(self):
        return self.mail



class Pet(models.Model):
    name = models.CharField(max_length=50)
    pet_type = models.IntegerField(default=None, null=True) ## 1 Dog , 2 Cat 
    gender = models.BooleanField(default=None, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=40)
    gender = models.IntegerField(null=True)


class PetPhotos(models.Model):
    url_photo = models.ImageField(upload_to='images/',null = True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    perfil = models.IntegerField()
    portada = models.IntegerField()
    pet = models.ForeignKey(Pet,on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f"Photo {self.id} of pet {self.pet_id}"


class PetShare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet,on_delete = models.CASCADE)
    status = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Vet(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ubication = models.CharField(max_length=255)

class Veterinarian(models.Model):
    name = models.CharField(max_length=100) 
    identification = models.CharField(max_length=50)
    work_in = models.ForeignKey(Vet, on_delete=models.SET_NULL,null=True)
    years_experience = models.IntegerField()



