from django.contrib import admin
from .models import Viagem, Passageiro

# Registramos os modelos para que apareçam no painel de administração
admin.site.register(Viagem)
admin.site.register(Passageiro)