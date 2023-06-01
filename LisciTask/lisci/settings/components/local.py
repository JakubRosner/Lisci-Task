import os

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "NAME": "lisci",
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "USER": "lisci",
        "PASSWORD": "lisci",
        "DISABLE_SERVER_SIDE_CURSORS": True,
        "OPTIONS": {"application_name": os.getenv("HOSTNAME", "unknown")},
    },
}
