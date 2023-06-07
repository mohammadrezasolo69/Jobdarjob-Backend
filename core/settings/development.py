from .base import *

LOCAL_APPS = [
    'silk',
]

INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE += 'silk.middleware.SilkyMiddleware',
