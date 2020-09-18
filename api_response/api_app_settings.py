from django.conf import settings

INCLUDE_PROFILE = False

# APPS ATTR
try:
    INCLUDE_PROFILE = settings.INCLUDE_PROFILE
    PROFILE_MODEL = settings.PROFILE_MODEL
except:
    PROFILE_MODEL = None

