from .base import *
from ...deploy.production.production import ( 
    secret_key, database, allowed_hosts, sentrysdk)


DEBUG = False
SECRET_KEY = secret_key
ALLOWED_HOSTS = allowed_hosts
DATABASES = database
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'

sentrysdk

try:
    from .local import *
except ImportError:
    pass
