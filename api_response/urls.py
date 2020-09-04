from django.contrib import admin
from django.urls import path
import api_response.views as api_views

urlpatterns = [

    # path('config/<slug:username>:<slug:pw>/', apiViews.test_api),
    


    path('', api_views.default_api_response),
    path('users/', api_views.api_users),
    path('test/', api_views.test),
    path('users/<slug:userid>/', api_views.api_user_data),
]