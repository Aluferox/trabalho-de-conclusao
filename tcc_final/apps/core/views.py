from django.shortcuts import render, redirect
from .forms import HomeForm
from msa_astar.celeryconfig import app
from apps.tarefas.models import TasksResults
from leitura_arquivos import handling_tasks
from django.http import HttpResponseRedirect
from django.urls import reverse
import time

def home(request):
    sequencia= []
    if request.user.is_authenticated:
        return redirect('view_logado')

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) == 1:
                sequence_file = request.FILES['file_data']

                for chunk in sequence_file.chunks():
                    sequencia.append(str(chunk, 'utf-8')[:-1])

            elif form.cleaned_data['manual_text']:
                    text_simple = form.cleaned_data['manual_text']
                    sequencia.append(text_simple.replace('\r',''))

            res = app.send_task('celery_django.tasks.alinhar_sequencias', args=[sequencia], queue='tarefas', kwargs={})

            time.sleep(2)
            request.path = None

            try:
                task_id = TasksResults.objects.get(id_task=res.id)

                if len(task_id.result) <= 132:
                    return redirect('ajuda')

                result, phases = handling_tasks(task_id.result[1:-1])
                return render(
                    request,
                    'core/resultado.html',
                    {
                        'task_result':result,
                        'phase_one':phases[0],
                        'phase_two':phases[1],
                        'similarity':phases[2]
                    }
                )
            except TasksResults.DoesNotExist:
                return HttpResponseRedirect(reverse('token', kwargs={'task_id':res.id}))

    else:
        form = HomeForm()
    return render(request, 'core/index.html', {'form': form})

def ajuda(request):
    return render(request, 'core/ajuda.html')
