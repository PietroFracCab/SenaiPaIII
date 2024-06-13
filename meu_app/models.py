from django.db import models

class Maquina(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    custo_inicial = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    custo_inicial = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Edificio(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    custo_inicial = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    custo_inicial = models.FloatField()
    depreciacao_anual = models.FloatField()
    expectativa_vida_util = models.IntegerField()

    def __str__(self):
        return self.nome