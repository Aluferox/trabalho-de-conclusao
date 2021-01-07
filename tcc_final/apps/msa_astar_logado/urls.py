from django.urls import path
from .views import view_logado


urlpatterns = [
    path('star/', view_logado, name='view_logado')
]