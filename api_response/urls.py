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

def make_patterns(app, model):
    for model in models_list:
        if model not in API_URLS:
            urlpatterns.append(path(f'{app}/{model}/', api_views.respond_to_call, {
                'app_name': app,
                'model_name': model
            }))
        else:
            for pattern in API_URLS[model]:
                if pattern != URL_PATTERN_BLOCKER:
                    urlpatterns.append(path(f'{pattern}', api_views.respond_to_call,
                                            {
                                                'app_name': app,
                                                'model_name': model
                                            }))
                else:
                    print(f'API_URLS blocked for  --> "{model}", by URL_PATTERN_BLOCKER : "{pattern}"')

    
# Trying to make a list if single model is given else pass as it is
for app, models_list in API_ENABLED_APPS.items():
    try:
        models_list = models_list.split()
        make_patterns(app, models_list)
    except AttributeError:
        make_patterns(app, models_list)

    
# Fixed URL patterns for user model
urlpatterns += [
    path('users/<slug:userid>/', api_views.api_user_data),
    path('', api_views.default_api_response),
    path('users/', api_views.user_api_endpoint),
]

print(f'API_URL_patterns --> {urlpatterns}')

