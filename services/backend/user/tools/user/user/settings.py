"""
Django settings for user project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from user.vault import VaultClient
import os

# Create a Vault link
vault = VaultClient()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@$a#6@+$t&8cn_qhyy0txl-8qvpxwdz^bt(!g=$fc#+e#2-x9g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'queueservice',
    'pokemapservice',
    'tokenservice',
    'userservice',
    'chatservice',
    'pongservice',
    'gameservice',
    '*',]

CSRF_COOKIE_SAMESITE = 'None'
CSRF_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['https://localhost:4430',
                        'https://127.0.0.1:4430',
                        'https://userservice:4430',
                        'https://chatservice:4430',
                        'https://tokenservice:4430',
                        'https://queueservice:4430',
                        'https://pokemapservice:4430',
                        'https://gameservice:4430',
                        'https://pongservice:4430',]


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'https://localhost:4430',
    'https://127.0.0.1:4430',
    'https://userservice:4430',
    'https://chatservice:4430',
    'https://tokenservice:4430',
    'https://queueservice:4430',
    'https://pokemapservice:4430',
    'https://gameservice:4430',
    'https://pongservice:4430', # Remplacez par les origines que vous voulez autoriser
]

# # Assurez-vous également d'utiliser HTTPS et de définir CSRF_COOKIE_SECURE et SESSION_COOKIE_SECURE sur True
# # Définition de l'attribut SameSite pour le cookie de session
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# Application definition
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'drf_spectacular',
    'profiles',
    'friends',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'user.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
        ],
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

WSGI_APPLICATION = 'user.wsgi.application'

ASGI_APPLICATION = 'user.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts":[("127.0.0.1", 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

db_info = vault.secret('user_db')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_info['db_name'],
        'USER': db_info['db_username'],
        'PASSWORD': db_info['db_password'],

    }
}

#Authentication user

AUTH_USER_MODEL = 'profiles.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
     BASE_DIR.joinpath('static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/home/'


# Configuration for Django REST Framework (DRF) to use DRF Spectacular for API documentation.
# Sets the default schema class to 'drf_spectacular.openapi.AutoSchema'.
# This class is responsible for generating the API schema for DRF Spectacular.
# For more information, refer to the DRF Spectacular documentation: https://drf-spectacular.readthedocs.io/
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

