from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('profile/', views.profile, name = 'User-Profile'),
    path('register/', views.register_user, name = 'Sign-Up'),
]