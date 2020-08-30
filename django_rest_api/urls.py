"""django_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import api_response
import loginsys
from home import views as homeviews
from django.contrib.auth.views import LogoutView
import users

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', homeviews.home, name='Home'),
    path('api/domain/', include('api_response.urls')),
    path('domain/auth/', include('loginsys.urls')),
    path('logout/', LogoutView.as_view(template_name='loginsys/logout_page.html'), name = 'Log-Out'),
    path('user/', include('users.urls')),

]

handler404 = 'api_response.views.error404'
handler500 = 'api_response.views.error500'
