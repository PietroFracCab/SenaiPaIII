import os
import django
from django.test import TestCase
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_paIII.settings')
django.setup()

from models import Veiculo

# Supondo que marea seja uma instância da classe Veiculo
marea = Veiculo()
marea.custo_aquisicao = 3000
marea.depreciacao_anual = 20.0  # Garantir que a depreciação anual seja 20%
marea.data_aquisicao = date(2020, 1, 1)  # Ajustar para uma data anterior ao ano atual

# Agora, calcular o valor atual
valor_atual = marea.calcular_valor_atual()
print(valor_atual)  # Isso deve mostrar um valor depreciado, não 3000