from django.shortcuts import render, redirect
from .forms import AtivoForm
from .models import Edificio, Veiculo  # Importe todos os modelos necessários
from datetime import datetime

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
                    data_aquisicao=datetime(year=form.cleaned_data['data_aquisicao'], month=1, day=1)
                )
                novo_ativo.save()
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
            return redirect('alguma-url-de-sucesso')
    else:
        form = AtivoForm()
    return render(request, 'adicionar_ativo.html', {'form': form})