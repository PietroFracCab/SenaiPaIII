from django.urls import path
from .views import adicionar_ativo

urlpatterns = [
    path('', adicionar_ativo, name='adicionar-ativo'), # '' vazio direciona para rota padrao http://localhost:8000/
]
