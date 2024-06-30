from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AtivoForm
from .models import Edificio, Veiculo  # Importe todos os modelos necessários
from datetime import date

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
                    # Adicione a lógica para Veiculo e outros tipos conforme necessário
                )
                novo_ativo.save()
            # Redireciona após o POST
            return redirect('adicionar-ativo')  # Redireciona para a mesma página, limpando o formulário
    else:
        form = AtivoForm()
    return render(request, 'adicionar_ativo.html', {'form': form})