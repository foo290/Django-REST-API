from django.contrib import admin
from django.urls import path
import api_response.views as apiViews

urlpatterns = [

    path('config/<slug:username>:<slug:pw>/', apiViews.test_api),
    


    path('', apiViews.default_api_response),
    path('users/', apiViews.api_users),
    path('users/<slug:userid>/', apiViews.api_user_data),
]