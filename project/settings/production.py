from .base import *

ENV_NAME = 'production'
DEBUG = False

# Whitenoise
# http://whitenoise.evans.io/en/stable/django.html

MIDDLEWARE = [MIDDLEWARE[0]] + ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE[1:]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


try:
    from .local import *
except ImportError:
    pass
