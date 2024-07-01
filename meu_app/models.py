
from django.db import models
from datetime import datetime, date


class Maquina(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField(default=15.0)
    expectativa_vida_util = models.IntegerField(default=10.0)
    data_aquisicao = models.DateField()

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField(default=20.0)
    expectativa_vida_util = models.IntegerField(default=10.0)
    data_aquisicao = models.DateField()

    def __str__(self):
        return self.nome
    
class Edificio(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField(default=4.0)
    expectativa_vida_util = models.IntegerField(default=25.0)
    data_aquisicao = models.DateField()

    def __str__(self):
        return self.nome
    
    def calcular_valor_atual(self):
        anos_uso = datetime.now().year - self.data_aquisicao
        valor_atual = self.custo_aquisicao * ((1 - self.depreciacao_anual/100) ** anos_uso)
        return valor_atual
    
class Veiculo(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField(default=20.0)
    expectativa_vida_util = models.IntegerField(default=5.0)
    data_aquisicao = models.DateField()

    def __str__(self):
        return self.nome
   
    def calcular_valor_atual(self):
        # Calcula a idade do veículo em anos
        ano_atual = date.today().year
        mes_atual = date.today().month
        dia_atual = date.today().day
        idade_veiculo = ano_atual - self.data_aquisicao.year

        # Ajusta a idade do veículo se ainda não chegou ao aniversário de compra no ano atual
        if mes_atual < self.data_aquisicao.month or (mes_atual == self.data_aquisicao.month and dia_atual < self.data_aquisicao.day):
            idade_veiculo -= 1

        # Aplica a depreciação anual ao custo de aquisição
        valor_atual = self.custo_aquisicao * ((1 - self.depreciacao_anual / 100) ** idade_veiculo)
        
        # Garante que o valor não seja negativo
        return max(valor_atual, 0)
    
    def calcular_vida_util_restante(self):
        ano_atual = datetime.now().year
        anos_uso = ano_atual - self.data_aquisicao.year
        vida_util_restante = self.expectativa_vida_util - anos_uso
        return vida_util_restante

