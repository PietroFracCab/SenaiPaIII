from django.urls import path
from .views import adicionar_ativo, EdificioListView, EquipamentoListView, VeiculoListView, MaquinaListView

urlpatterns = [
    path('', adicionar_ativo, name='adicionar-ativo'),
    path('edificios/', EdificioListView.as_view(), name='edificio-list'),
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento-list'),
    path('veiculos/', VeiculoListView.as_view(), name='veiculo-list'),
    path('maquinas/', MaquinaListView.as_view(), name='maquina-list'),
]