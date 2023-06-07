from .base import *

# Config Sentry
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=env('SENTRY_DNS'),
    integrations=[
        DjangoIntegration(),
    ],

    traces_sample_rate=1.0,
    send_default_pii=True
)
