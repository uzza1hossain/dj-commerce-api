import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(result_backend="django-db")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
