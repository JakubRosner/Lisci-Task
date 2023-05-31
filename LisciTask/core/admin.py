from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('core')
for model in app.models.values():
    admin.site.register(model)
