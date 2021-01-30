from django.shortcuts import render, redirect
from .models import TasksResults
from leitura_arquivos import handling_tasks
from .forms import IdForm

def entrega_token(request, task_id):
    return render(request, 'tarefas/task_id.html', {'task_id':task_id})

def consultar_sequencia(request):
    if request.method == 'POST':
        form = IdForm(request.POST)
        if form.is_valid():
            task_id = form.cleaned_data['task_id']
            try:
                task_id = TasksResults.objects.get(id_task=task_id)

                if len(task_id.result) <= 132:
                    return redirect('ajuda')

                result, phases = handling_tasks(task_id.result)

            except TasksResults.DoesNotExist:
                message = 'Sua Sequência Ainda Não Está Alinhada.'
                return render(
                    request,
                    'tarefas/consulta_sequencia.html',
                    {'form':form,
                     'message_error':message,
                     'task_id':task_id
                     }
                )

            return render(
                request,
                'tarefas/resultado_db.html',
                {
                    'task_result': result,
                    'phase_one': phases[0],
                    'phase_two': phases[1],
                    'similarity': phases[2]
                }
            )
    else:
        form = IdForm()
    return render(request, 'tarefas/consulta_sequencia.html', {'form':form})
