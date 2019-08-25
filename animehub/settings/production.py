import random
import string

import django_cache_url
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = os.getenv('DJANGO_DEBUG', 'off') == 'on'

if 'DJANGO_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    # Use if/else rather than a default value to avoid calculating this if we don't need it
    print(
        "WARNING: DJANGO_SECRET_KEY not found in os.environ. Generating ephemeral SECRET_KEY."
    )
    SECRET_KEY = ''.join(
        [random.SystemRandom().choice(string.printable) for i in range(50)])

# Make sure Django can detect a secure connection properly on Heroku:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Redirect all requests to HTTPS
SECURE_SSL_REDIRECT = os.getenv('DJANGO_SECURE_SSL_REDIRECT', 'off') == 'on'

# Accept all hostnames, since we don't know in advance which hostname will be used for any given Heroku instance.
# IMPORTANT: Set this to a real hostname when using this in production!
# See https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(';')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# AWS creds may be used for S3 and/or Elasticsearch
AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY', '')
AWS_REGION = os.getenv('DJANGO_AWS_REGION', '')

# configure CACHES from CACHE_URL environment variable (defaults to locmem if no CACHE_URL is set)
CACHES = {'default': django_cache_url.config()}

if 'DJANGO_AWS_STORAGE_BUCKET_NAME' in os.environ:
    AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_AUTO_CREATE_BUCKET = True

    # STATIC
    # ------------------------

    STATICFILES_STORAGE = 'animehub.settings.production.StaticRootS3BotoStorage'
    STATIC_URL = 'https://{}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME)

    # MEDIA
    # ------------------------------------------------------------------------------

    INSTALLED_APPS.append('storages')
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
    MEDIA_HOST = ''

    # region http://stackoverflow.com/questions/10390244/
    from storages.backends.s3boto3 import S3Boto3Storage  # noqa E402
    from storages.backends.s3boto3 import S3Boto3Storage  # noqa E402
    StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')  # noqa
    MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='media', file_overwrite=False)  # noqa
    # endregion
    DEFAULT_FILE_STORAGE = 'animehub.settings.production.MediaRootS3BotoStorage'

    # Collectfast
    # ------------------------------------------------------------------------------
    # https://github.com/antonagestam/collectfast#installation
    INSTALLED_APPS = ['collectfast'] + INSTALLED_APPS  # noqa F405
    AWS_PRELOAD_METADATA = True
    COLLECTFAST_THREADS = 20

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

if 'DJANGO_SENTRY_DSN' in os.environ:
    sentry_sdk.init(
        dsn=os.getenv('DJANGO_SENTRY_DSN'),
        integrations=[DjangoIntegration()]
    )

try:
    from .local import *
except ImportError:
    pass
