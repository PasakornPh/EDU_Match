
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'match_edu.settings')

app = Celery('match_edu')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()