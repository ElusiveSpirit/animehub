from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES['default']['HOST'] = 'localhost'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2(k#=3t$95lu7gwssm@$z6q4=xr&_x+a)q@-%u6#+=ngy#rx7='

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BASE_URL = 'http://127.0.0.1:8000'
INTERNAL_IPS = ['127.0.0.1']

try:
    from .local import *
except ImportError:
    pass
