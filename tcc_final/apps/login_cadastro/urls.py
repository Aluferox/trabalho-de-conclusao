from django.urls import path
from apps.login_cadastro import views as login_cadastro_views

urlpatterns = [
    path('registrar/',login_cadastro_views.CreateUserView.as_view() , name='registrar'),
]