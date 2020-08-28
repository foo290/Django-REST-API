from django.contrib import admin
from django.urls import path
from api_response.views import UsersViews

urlpatterns = [

    # path('config/<slug:username>:<slug:pw>/', apiViews.test_api),
    


    path('', UsersViews().default_api_response),
    path('users/', UsersViews().api_users),
    path('users/<slug:userid>/', UsersViews().api_user_data),
]