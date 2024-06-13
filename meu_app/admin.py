from django.contrib import admin
from .models import Maquina, Equipamento, Edificio, Veiculo

admin.site.register(Maquina, Equipamento, Edificio, Veiculo)

# Register your models here.
