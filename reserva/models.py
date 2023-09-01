from django.db import models

# Create your models here.
class Reserva(models.Model):
    cnpj = models.CharField(max_length=18)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField()

    def __str__(self):
        return self.nome_empresa

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()
    empresa = models.OneToOneField(Reserva, on_delete=models.CASCADE)