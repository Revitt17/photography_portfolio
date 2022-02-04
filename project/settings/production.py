from .base import *
from ..settings.secret_key import secret_key


DEBUG = False
SECRET_KEY = secret_key
ALLOWED_HOSTS = ['*'] 


try:
    from .local import *
except ImportError:
    pass
