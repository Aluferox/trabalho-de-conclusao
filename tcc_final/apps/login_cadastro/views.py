from django.shortcuts import render, redirect
from .forms import CreateUsers
from django.contrib import messages

def registro(request):

    if request.method =='POST':
        form = CreateUsers(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Você Foi Cadastrado com Sucesso.')
            return redirect('login')
    else:
        form = CreateUsers()

    return render(request, 'login_cadastro/registro.html', {'form':form})

