"""
Django settings for herring project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import json
import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(BASE_DIR), '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+fn9lj!kwzxqzpxihje!_+o0!y8ork#@+wc19w_mnf7^6gi4d$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'puzzles',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'herring.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'herring.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': env.db_url(
        default='postgres:///herringdb',
        engine='django.db.backends.postgresql_psycopg2')
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = []

REDIS_URL = env.get_value('REDIS_URL', default='redis://localhost:6379/0')

# Celery queue
CELERY_BROKER_URL = env.get_value('BROKER_URL', default=REDIS_URL)


# Previously in puzzles/tasks.py
HERRING_STATUS_CHANNEL = env.get_value('STATUS_CHANNEL', default='_dev_puzzle_status')
HERRING_HOST = env.get_value('HOST', default='http://localhost:5000')
HERRING_PUZZLE_ACTIVITY_LOG_URL = env.get_value('PUZZLE_ACTIVITY_LOG_URL', default=None)
HERRING_PUZZLE_SITE_SESSION_COOKIE = env.get_value('PUZZLE_SITE_SESSION_COOKIE', default=None)


# Previously in herring/secrets.py
HERRING_SECRETS = json.loads(env.get_value('SECRETS', default='{}'))
HERRING_FUCK_OAUTH = json.loads(env.get_value('FUCK_OAUTH', default='{}'))


# XXX: the following was an attempt to get more stuff logged in Heroku. It
# didm't appear to work and it's not clear that it does anything.
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
