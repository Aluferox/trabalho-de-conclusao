from celery import shared_task
from apps.tarefas.models import TasksResults

@shared_task(name='save_database')
def save_database(result_seq):
        salvar = TasksResults(id_task=result_seq['task_id'],result=result_seq['result'])
        salvar.save()
