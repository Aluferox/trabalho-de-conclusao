from django.urls import path, include
from  .views import registro

urlpatterns = [
    path('registrar/', registro, name='registrar'),
]