
from django.db import models
from datetime import datetime


class Maquina(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()
    data_aquisicao = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()
    data_aquisicao = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return self.nome
    
class Edificio(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    loc =  models.CharField(max_length=100, default="Não especificado")
    custo_aquisicao = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()
    data_aquisicao = models.IntegerField(default=datetime.now().year)

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
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()
    data_aquisicao = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return self.nome
    def __str__(self):
        return self.nome

