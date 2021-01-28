from django.shortcuts import render, redirect
from .forms import HomeForm
from msa_astar.celeryconfig import app
from apps.tarefas.models import TasksResults
from leitura_arquivos import handling_tasks
from django.contrib.auth.decorators import login_required
import time

@login_required
def view_logado(request):
    sequencia= []
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


            res = app.send_task('celeryworker.tasks.alinhar_sequencias', args=[sequencia], queue='tarefas', kwargs={})

            time.sleep(2)
            request.path = '/msa/star/'

            try:
                result_tasks = TasksResults.objects.get(id_task=res.id)
                result, phases = handling_tasks(result_tasks.result[1:-1])
                return render(
                    request,
                    'msa_astar_logado/resultado.html',
                    {
                        'task_result':result,
                        'phase_one':phases[0],
                        'phase_two':phases[1],
                        'similarity':phases[2]
                    }
                )
            except TasksResults.DoesNotExist:
                request.session['id'] = res.id
                return redirect('token')

    else:
        form = HomeForm()
    return render(request, 'msa_astar_logado/page_main.html', {'form': form})
