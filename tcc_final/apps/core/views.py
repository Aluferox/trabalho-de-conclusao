from django.shortcuts import render
from .forms import HomeForm
from leitura_arquivos import handle_uploaded_file
from django.shortcuts import redirect


def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) == 1:
                result, infos = handle_uploaded_file(request.FILES['file_data'])
            elif form.cleaned_data['manual_text']:
                    text_simple = form.cleaned_data['manual_text']
                    result, infos = handle_uploaded_file(text_simple)

            request.path = None

            if result and infos:
                return render(request, 'core/resultado.html', {'result': result,
                                                           'phase_one': infos[0],
                                                           'phase_two': infos[1],
                                                           'similarity': infos[2],
                                                           },
                              )
            else:
                return redirect('ajuda')
    else:
        form = HomeForm()
    return render(request, 'core/index.html', {'form': form})

def ajuda(request):
    return render(request, 'core/ajuda.html')



