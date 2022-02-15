from .base import *
from ..settings.secret_key import secret_key


DEBUG = False
SECRET_KEY = secret_key
ALLOWED_HOSTS = ['localhost', '*'] 
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True
STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": '',
        "USER": '',
        "PASSWORD": '',
        "HOST": 'localhost',
        "PORT": "",
    }
}


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://972917c839474187b8ba284c51739ebd@o1144789.ingest.sentry.io/6209500",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


try:
    from .local import *
except ImportError:
    pass
