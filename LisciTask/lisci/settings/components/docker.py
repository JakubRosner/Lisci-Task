import os

DEBUG = True

ALLOWED_HOSTS = [".localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME", "nope"),
        "USER": os.environ.get("POSTGRES_USER", "nope"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "nope"),
        "HOST": "db",
        "PORT": 5432,
    }
}