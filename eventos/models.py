from django.db import models

# Create your models here.

class Eventos(models.Model):
    nome_evento = models.CharField(max_length=200)
    tipo = models.TextField()
    data_inicio = models.DateField()
    data_final = models.DateField()
    descricao = models.CharField(max_length=400)
    gratuito = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    local = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    quantidade_vagas = models.CharField(max_length=10)

    def __str__(self):
        return self.nome_evento