from django.core.management.base import BaseCommand
from meu_app.views import create_user
from django.http import HttpRequest

class Command(BaseCommand):
	help = 'Cria um usuário admin se ele não existir'

	def handle(self, *args, **kwargs):
		# Simula uma requisição HttpRequest
		request = HttpRequest()
		# Chama a função create_user
		response = create_user(request)
		# Imprime a resposta no console
		self.stdout.write(self.style.SUCCESS(response.content.decode()))