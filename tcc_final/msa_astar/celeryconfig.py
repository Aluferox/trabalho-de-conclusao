import os
from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msa_astar.settings')

app = Celery('msa_astar')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_default_queue = 'resultados'
app.conf.task_queues = (
     Queue('resultados', routing_key='default'),
)

if __name__ == '__main__':
    app.start()
