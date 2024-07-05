from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import User_APIView,Pet_APIView,PetPhotoUploadView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('users/',User_APIView.as_view(), name='user-crud'),
    path('users/login/', User_APIView.login, name='user-login'),
    path('pet/',Pet_APIView.as_view(), name='pet-crud'),
    path('pet/<int:id>/',Pet_APIView.getByUser, name='pet-by-user'),
    path('petMedia/', PetPhotoUploadView.as_view(), name='photo-upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)