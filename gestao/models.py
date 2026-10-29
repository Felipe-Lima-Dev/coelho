from django.db import models

# Create your models here.
from django.db import models

class Viagem(models.Model):
    # Campos do 'novaviagem.html'
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    cidade_inicio = models.CharField(max_length=100)
    cidade_termino = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    horario_saida = models.TimeField()
    horario_chegada = models.TimeField()

    def __str__(self):
        return self.nome


class Passageiro(models.Model):
    # Campos do 'novopassageiro.html'
    nome = models.CharField(max_length=150)
    documento = models.CharField(max_length=20)
    nacionalidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    nome_emergencia = models.CharField(max_length=150)
    telefone_emergencia = models.CharField(max_length=20)
    
    # Campo para o Status/Presença
    presente = models.CharField(default='off')

    # Relação Pai-Filho com PROTECT
    viagem = models.ForeignKey(Viagem, on_delete=models.PROTECT, related_name='passageiros')

    def __str__(self):
        return self.nome
    