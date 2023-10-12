from rest_framework import serializers
from .models import User,Pet



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['create_at','update_at']



class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ['create_at','update_at']