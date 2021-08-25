from django.db import models

# Create your models here.


class Empresas(models.Model):
    nome = models.CharField(max_length=250)
    servicos = models.CharField(max_length=500)
    cnpj = models.IntegerField()
