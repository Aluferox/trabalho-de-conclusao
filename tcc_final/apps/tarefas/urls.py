from django.urls import path
from apps.tarefas import views

urlpatterns = [
    path('token/', views.entrega_token, name='token'),
    path('consultar-sequencia/', views.consultar_sequencia, name='consulta_seq'),
]