
from django.db import models
from datetime import datetime, date
import locale

# Define o locale para Português Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Ativo(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc = models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField()  # Será definido nas subclasses
    expectativa_vida_util = models.IntegerField()  # Será definido nas subclasses
    data_aquisicao = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

    def calcular_valor_atual(self):
        anos_uso = datetime.now().year - self.data_aquisicao.year
        valor_atual = self.custo_aquisicao * ((1 - self.depreciacao_anual / 100) ** anos_uso)
        return locale.currency(valor_atual, grouping=True)

    def calcular_vida_util_restante(self):
        ano_atual = datetime.now().year
        anos_uso = ano_atual - self.data_aquisicao.year
        vida_util_restante = self.expectativa_vida_util - anos_uso
        return vida_util_restante

    def custo_aquisicao_formatado(self):
        return locale.currency(self.custo_aquisicao, grouping=True)

class Maquina(Ativo):
    depreciacao_anual = models.FloatField(default=15.0)
    expectativa_vida_util = models.IntegerField(default=10)

class Equipamento(Ativo):
    depreciacao_anual = models.FloatField(default=20.0)
    expectativa_vida_util = models.IntegerField(default=10)

class Edificio(Ativo):
    depreciacao_anual = models.FloatField(default=4.0)
    expectativa_vida_util = models.IntegerField(default=25)

class Veiculo(Ativo):
    depreciacao_anual = models.FloatField(default=20.0)
    expectativa_vida_util = models.IntegerField(default=5)