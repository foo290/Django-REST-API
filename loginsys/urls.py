from django.contrib import admin
from django.urls import path
from loginsys import views as loginviews
from django.contrib.auth import views as authviews
from users import views as usersviews

urlpatterns = [
    
    # path('login/', loginviews.login_page, name = 'Log-In'),
    path('user-login/', authviews.LoginView.as_view(template_name='loginsys/login_page.html'), name = 'Log-In'),

    # path('signup/', loginviews.register_user, name = 'Sign-Up'),
]