from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import CreateUsers

from django.views.generic import CreateView


class CreateUserView(CreateView):
    model = User
    template_name = 'login_cadastro/registro.html'
    form_class = CreateUsers
    success_url = reverse_lazy('login')
