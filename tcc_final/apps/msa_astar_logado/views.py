from django.shortcuts import render
from .forms import HomeForm
from leitura_arquivos import handle_uploaded_file
from django.contrib.auth.decorators import login_required


@login_required
def view_logado(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) == 1:
                result, infos = handle_uploaded_file(request.FILES['file_data'])
            else:
                text_simple = form.cleaned_data['manual_text']
                result, infos = handle_uploaded_file(text_simple)

            return render(request, 'msa_astar_logado/resultado.html', {'result': result,
                                                           'phase_one': infos[0],
                                                           'phase_two': infos[1],
                                                           'similarity': infos[2],
                                                           },
                              )

    else:
        form = HomeForm()
    return render(request, 'msa_astar_logado/page_main.html', {'form':form})




