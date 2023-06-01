from os import environ

from split_settings.tools import include

ENV = environ.get("DJANGO_ENV") or "local"
ENV = "local" if ENV == "development" else ENV

base_settings = [
    f"{ENV}.py",
]

include(*base_settings)