from celery import Celery

app = Celery('news')

app.config_from_object('django.conf:settings', namespace='CELERY')
