from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import User_APIView,Pet_APIView

urlpatterns = [
    path('users/',User_APIView.as_view(), name='user-crud'),
    path('users/login/', User_APIView.login, name='user-login'),
    path('pet/',Pet_APIView.as_view(), name='pet-crud'),
    path('pet/<int:id>/',Pet_APIView.getByUser, name='pet-by-user'),
]