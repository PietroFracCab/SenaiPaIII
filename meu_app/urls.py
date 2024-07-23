from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MyLoginView, adicionar_ativo, EdificioListView, EdificioUpdateView, EdificioDeleteView, EquipamentoListView, VeiculoListView, MaquinaListView, MaquinaUpdateView, MaquinaDeleteView, EquipamentoUpdateView, EquipamentoDeleteView, VeiculoUpdateView, VeiculoDeleteView

urlpatterns = [
    path('', login_required(adicionar_ativo), name='adicionar-ativo'),
    path('edificios/', EdificioListView.as_view(), name='edificio-list'),
    path('edificio/update/<int:pk>/', EdificioUpdateView.as_view(), name='edificio-update'),
    path('edificio/delete/<int:pk>/', EdificioDeleteView.as_view(), name='edificio-delete'),
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento-list'),
    path('equipamentos/update/<int:pk>/', EquipamentoUpdateView.as_view(), name='equipamento-update'),
    path('equipamentos/delete/<int:pk>/', EquipamentoDeleteView.as_view(), name='equipamento-delete'),
    path('veiculos/', VeiculoListView.as_view(), name='veiculo-list'),
    path('veiculos/update/<int:pk>/', VeiculoUpdateView.as_view(), name='veiculo-update'),
    path('veiculos/delete/<int:pk>/', VeiculoDeleteView.as_view(), name='veiculo-delete'),
    path('maquinas/', MaquinaListView.as_view(), name='maquina-list'),
    path('maquinas/update/<int:pk>/', MaquinaUpdateView.as_view(), name='maquina-update'),
    path('maquinas/delete/<int:pk>/', MaquinaDeleteView.as_view(), name='maquina-delete'),
    #path('', MyLoginView.as_view(), name='login'),
    path('login/', MyLoginView.as_view(), name='login'),
    
]
