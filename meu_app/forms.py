from django import forms
from .models import Edificio, Veiculo, Maquina, Equipamento

class AtivoForm(forms.Form):
    TIPO_ATIVO_CHOICES = [
        ('Edificio', 'Edifício'),
        ('Veiculo', 'Veículo'),
        ('Maquina', 'Máquina'),
        ('Equipamento', 'Equipamento'),
         
        # Adicione mais opções conforme necessário
    ]
    codigo = forms.IntegerField(label='Código')
    nome = forms.CharField(label='Nome', max_length=100)
    tipo = forms.ChoiceField(label='Tipo', choices=TIPO_ATIVO_CHOICES)
    loc = forms.CharField(label='Localização', max_length=100)
    custo_aquisicao = forms.FloatField(label='Custo de Aquisição')
    data_aquisicao = forms.DateField(
        label='Data de Aquisição',
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        input_formats=['%d/%m/%Y'],
        help_text='Formato: DD/MM/AAAA'
    )

class AtivoFormBase(forms.ModelForm):
    class Meta:
        fields = ['codigo', 'nome', 'loc', 'custo_aquisicao', 'data_aquisicao']
        labels = {
            'codigo': 'Código',
            'nome': 'Nome',
            'loc': 'Localização',
            'custo_aquisicao': 'Custo de Aquisição',
            'data_aquisicao': 'Data de Aquisição',
        }
        widgets = {
            'data_aquisicao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class EdificioForm(AtivoFormBase):
    class Meta(AtivoFormBase.Meta):
        model = Edificio

class VeiculoForm(AtivoFormBase):
    class Meta(AtivoFormBase.Meta):
        model = Veiculo

class MaquinaForm(AtivoFormBase):
    class Meta(AtivoFormBase.Meta):
        model = Maquina

class EquipamentoForm(AtivoFormBase):
    class Meta(AtivoFormBase.Meta):
        model = Equipamento