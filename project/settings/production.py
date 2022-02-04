from .base import *


DEBUG = False
SECRET_KEY = ''
ALLOWED_HOSTS = ['*'] 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
STATIC_ROOT = ''
STATIC_URL = '/static/'
MEDIA_ROOT = ''
MEDIA_URL = '/media/'


try:
    from .local import *
except ImportError:
    pass
