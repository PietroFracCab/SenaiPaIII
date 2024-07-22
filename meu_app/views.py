from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AtivoForm, EdificioForm, VeiculoForm, MaquinaForm, EquipamentoForm
from .models import Edificio, Veiculo, Maquina, Equipamento  
from datetime import date
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def criar_ativo(form_data, AtivoClass): #função criada para refatorar condições IF de adicionar_ativo
    novo_ativo = AtivoClass(
        codigo=form_data['codigo'],
        nome=form_data['nome'],
        tipo=form_data['tipo'],
        loc=form_data['loc'],
        custo_aquisicao=form_data['custo_aquisicao'],
        data_aquisicao=date(year=form_data['data_aquisicao'].year, month=form_data['data_aquisicao'].month, day=form_data['data_aquisicao'].day)
    )
    novo_ativo.save()

def adicionar_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            ativo_classes = {
                'Edificio': Edificio,
                'Veiculo': Veiculo,
                'Maquina': Maquina,
                'Equipamento': Equipamento
            }
            if tipo in ativo_classes:
                criar_ativo(form.cleaned_data, ativo_classes[tipo])
                messages.success(request, 'Ativo adicionado com sucesso!')
                return redirect('adicionar-ativo')
    else:
        form = AtivoForm()
    return render(request, 'adicionar_ativo.html', {'form': form})

class EdificioListView(ListView):
    model = Edificio
    template_name = 'EdificioListView.html'
    context_object_name = 'Edificio_list'

class EdificioUpdateView(UpdateView):
    model = Edificio
    form_class = EdificioForm
    template_name = 'EdificioUpdateView.html'
    success_url = reverse_lazy('edificio-list')

class EdificioDeleteView(DeleteView):
    model = Edificio
    template_name = 'EdificioDeleteView.html'
    success_url = reverse_lazy('edificio-list')

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'VeiculoListView.html'
    context_object_name = 'Veiculo_list'

class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'VeiculoUpdateView.html'
    success_url = reverse_lazy('veiculo-list')

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'VeiculoDeleteView.html'
    success_url = reverse_lazy('veiculo-list')

class MaquinaListView(ListView):
    model = Maquina
    template_name = 'MaquinaListView.html'
    context_object_name = 'Maquina_list'

class MaquinaUpdateView(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name = 'MaquinaUpdateView.html'
    success_url = reverse_lazy('maquina-list')

class MaquinaDeleteView(DeleteView):
    model = Maquina
    template_name = 'MaquinaDeleteView.html'
    success_url = reverse_lazy('maquina-list')

class EquipamentoListView(ListView):
    model = Equipamento
    template_name = 'EquipamentoListView.html'
    context_object_name = 'Equipamento_list'

class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'EquipamentoUpdateView.html'
    success_url = reverse_lazy('equipamento-list')

class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = 'EquipamentoDeleteViewe.html'
    success_url = reverse_lazy('equipamento-list')