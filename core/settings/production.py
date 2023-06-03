# Config Sentry
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

sentry_sdk.init(
    dsn=env('DNS'),
    integrations=[
        DjangoIntegration(),
    ],

    traces_sample_rate=1.0,
    send_default_pii=True
)
