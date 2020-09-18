from django.contrib import admin
from django.urls import path
import api_response.views as api_views

urlpatterns = [

    # path('config/<slug:username>:<slug:pw>/', apiViews.test_api),
    
    path('users/<slug:userid>/', api_views.api_user_data),
]