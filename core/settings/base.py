import os
from pathlib import Path

import environ

# ----------------------------------------------------------------------------------------------------------------------

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# ----------------------------------------------------------------------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']

# ----------------------------------------------------------------------------------------------------------------------

# Application definition
INTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework',
    'django_filters'
]

MY_APPS = [
    'job.apps.JobConfig',
]


INSTALLED_APPS = INTERNAL_APPS + THIRD_PARTY_APPS + MY_APPS

# ----------------------------------------------------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------------------------------------------------------------------------

ROOT_URLCONF = 'core.urls'

# ----------------------------------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------------------------------

WSGI_APPLICATION = 'core.wsgi.application'

# ----------------------------------------------------------------------------------------------------------------------

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent/ 'db.sqlite3',
    },

    'clickhouse': {
        'ENGINE': 'clickhouse_backend.backend',
        'NAME': env('CLICKHOUSE_NAME_DB'),
        'HOST': env("CLICKHOUSE_HOST_DB"),
        'PORT': env('CLICKHOUSE_PORT_DB'),
        'USER': env("CLICKHOUSE_USER_DB"),
        'PASSWORD': env("CLICKHOUSE_PASSWORD_DB"),
    }
}
DATABASE_ROUTERS = ['core.dbrouters.ClickHouseRouter']
# ----------------------------------------------------------------------------------------------------------------------

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# ----------------------------------------------------------------------------------------------------------------------

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_TZ = False

# ----------------------------------------------------------------------------------------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATIC_ROOT = os.path.join(BASE_DIR.parent, 'statics/')
MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'assets')
]

# ----------------------------------------------------------------------------------------------------------------------

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Config drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Jobdarjob',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR'
}

# Config DRF
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

