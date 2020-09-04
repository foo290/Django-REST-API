from django.contrib import admin
from django.urls import path
import webhooks.views as webhook_views

urlpatterns = [
    path('reverse-api-request/callback-point/github/', webhook_views.github_webhook_point),
]