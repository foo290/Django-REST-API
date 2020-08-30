from django.contrib import admin
from django.urls import path
from loginsys import views as loginviews

urlpatterns = [

    path('login/', loginviews.login_page, name = 'Log-In'),
    path('signup/', loginviews.register_user, name = 'Sign-Up'),
]