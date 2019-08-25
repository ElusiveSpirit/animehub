import logging

from .base import *

DEBUG = False
SECRET_KEY = "zV5D42vLIMsfGZtEEzkKzz4mUXWyBxXyHg7f2tDVeyzavQsLPapEt9S6xxwN23Ep"
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": ""
    }
}

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.test.sqlite3'
    }
}

if os.environ.get('TESTS_WITHOUT_MIGRATIONS', False):
    MIGRATION_MODULES = {app.split('.')[-1]: None for app in INSTALLED_APPS}

# CELERY
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = 'redis'
CELERY_BROKER_URL = 'redis://'

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa F405

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# AMOCRM_SYNC_ENABLED = env.bool('AMOCRM_SYNC_ENABLED')

logging.disable(logging.CRITICAL)

try:
    from .local import *
except ImportError:
    pass
