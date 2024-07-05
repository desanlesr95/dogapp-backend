from rest_framework import serializers
from .models import User,Pet,PetPhotos



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['create_at','update_at']

class PetPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPhotos
        fields = ['url_photo', 'update_at'] 


class PetSerializer(serializers.ModelSerializer):
    recent_profile_photo = serializers.SerializerMethodField()
    class Meta:
        model = Pet
        exclude = ['create_at','update_at']
    def get_recent_profile_photo(self, obj):
        recent_photo = PetPhotos.objects.filter(pet=obj, perfil=1).order_by('-update_at').first()
        if recent_photo:
            return PetPhotoSerializer(recent_photo).data
        return None


class PetPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPhotos
        fields = '__all__'