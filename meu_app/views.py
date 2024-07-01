from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AtivoForm
from .models import Edificio, Veiculo, Maquina, Equipamento  # Importe todos os modelos necessários
from datetime import date
from django.views.generic.list import ListView

def adicionar_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            # Crie uma instância do modelo com base no tipo e salve no banco de dados
            if tipo == 'Edificio':
                novo_ativo = Edificio(
                    codigo=form.cleaned_data['codigo'],
                    nome=form.cleaned_data['nome'],
                    tipo=tipo,
                    loc=form.cleaned_data['loc'],
                    custo_aquisicao=form.cleaned_data['custo_aquisicao'],
                    data_aquisicao=date(year=form.cleaned_data['data_aquisicao'].year, month=form.cleaned_data['data_aquisicao'].month, day=form.cleaned_data['data_aquisicao'].day)
                )
                novo_ativo.save()
                messages.success(request, 'Ativo adicionado com sucesso!')
                return redirect('adicionar-ativo')  # Redireciona para a mesma página, limpando o formulário
            elif tipo == 'Veiculo':
                novo_ativo = Veiculo(
                    codigo=form.cleaned_data['codigo'],
                    nome=form.cleaned_data['nome'],
                    tipo=tipo,
                    loc=form.cleaned_data['loc'],
                    custo_aquisicao=form.cleaned_data['custo_aquisicao'],
                    data_aquisicao=date(year=form.cleaned_data['data_aquisicao'].year, month=form.cleaned_data['data_aquisicao'].month, day=form.cleaned_data['data_aquisicao'].day)
                    # Adicione a lógica para Veiculo e outros tipos conforme necessário
                )
                novo_ativo.save()
                messages.success(request, 'Ativo adicionado com sucesso!')
                return redirect('adicionar-ativo')  # Redireciona para a mesma página, limpando o formulário
            elif tipo == 'Maquina':
                novo_ativo = Maquina(
                    codigo=form.cleaned_data['codigo'],
                    nome=form.cleaned_data['nome'],
                    tipo=tipo,
                    loc=form.cleaned_data['loc'],
                    custo_aquisicao=form.cleaned_data['custo_aquisicao'],
                    data_aquisicao=date(year=form.cleaned_data['data_aquisicao'].year, month=form.cleaned_data['data_aquisicao'].month, day=form.cleaned_data['data_aquisicao'].day)
                )
                novo_ativo.save()
                messages.success(request, 'Ativo adicionado com sucesso!')
                return redirect('adicionar-ativo')
            elif tipo == 'Equipamento':
                novo_ativo = Equipamento(
                    codigo=form.cleaned_data['codigo'],
                    nome=form.cleaned_data['nome'],
                    tipo=tipo,
                    loc=form.cleaned_data['loc'],
                    custo_aquisicao=form.cleaned_data['custo_aquisicao'],
                    data_aquisicao=date(year=form.cleaned_data['data_aquisicao'].year, month=form.cleaned_data['data_aquisicao'].month, day=form.cleaned_data['data_aquisicao'].day)
                )
                novo_ativo.save()
                messages.success(request, 'Ativo adicionado com sucesso!')
            return redirect('adicionar-ativo')
    else:
        form = AtivoForm()
    return render(request, 'adicionar_ativo.html', {'form': form})

class EdificioListView(ListView):
    model = Edificio
    template_name = 'EdificioListView.html'
    context_object_name = 'Edificio_list'


class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'VeiculoListView.html'
    context_object_name = 'Veiculo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione os veículos ao contexto
        veiculos = Veiculo.objects.all()
        # Calcule o valor atual para cada veículo e armazene em um dicionário
        veiculos_valores_atuais = {veiculo.id: veiculo.calcular_valor_atual() for veiculo in veiculos}
        # Adicione o dicionário ao contexto
        context['veiculos_valores_atuais'] = veiculos_valores_atuais
        return context

class MaquinaListView(ListView):
    model = Maquina
    template_name = 'MaquinaListView.html'
    context_object_name = 'Maquina_list'

class EquipamentoListView(ListView):
    model = Equipamento
    template_name = 'EquipamentoListView.html'
    context_object_name = 'Equipamento_list'