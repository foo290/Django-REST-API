from django.contrib import admin
from django.urls import path
import api_response.views as api_views
from .api_app_settings import (
    API_ENABLED_APPS,
    URL_PATTERN_BLOCKER,
    API_URLS,
)

urlpatterns = []

# Making URL patterns based on user specified models and pattern
for app in API_ENABLED_APPS:
    if app not in API_URLS:
        urlpatterns.append(path(f'{app}/', api_views.respond_to_call, {
            'app_name': app,
            'model_name': API_ENABLED_APPS[app]
        }))
    else:
        for pattern in API_URLS[app]:
            if pattern != URL_PATTERN_BLOCKER:
                urlpatterns.append(path(f'{pattern}', api_views.respond_to_call,
                                        {
                                            'app_name': app,
                                            'model_name': API_ENABLED_APPS[app]
                                        }))
            else:
                print(f'API_URLS blocked for  --> "{app}", by URL_PATTERN_BLOCKER : "{pattern}"')

# Fixed URL patterns for user model
urlpatterns += [
    path('users/<slug:userid>/', api_views.api_user_data),
    path('', api_views.default_api_response),
    path('users/', api_views.user_api_endpoint),
    path('testapi/<slug:user>/<slug:operator>/<slug:id>', api_views.test_api)
]

print(f'API_URL_patterns --> {urlpatterns}')

