from django.urls import path
from . import views

urlpatterns = [
    path('users',views.get, name='user-list'),
]