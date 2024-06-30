from django import forms
from .models import Edificio, Veiculo  # Importe todos os modelos necessários

class AtivoForm(forms.Form):
    TIPO_ATIVO_CHOICES = [
        ('Edificio', 'Edifício'),
        ('Veiculo', 'Veículo'),
        # Adicione mais opções conforme necessário
    ]
    codigo = forms.IntegerField(label='Código')
    nome = forms.CharField(label='Nome', max_length=100)
    tipo = forms.ChoiceField(label='Tipo', choices=TIPO_ATIVO_CHOICES)
    loc = forms.CharField(label='Localização', max_length=100)
    custo_aquisicao = forms.FloatField(label='Custo de Aquisição')
    data_aquisicao = forms.IntegerField(label='Data de Aquisição')
    