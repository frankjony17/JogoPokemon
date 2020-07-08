from django.db import models


class Tipo(models.Model):
    name = models.CharField(
        max_length=45, blank=False, unique=False)
    slot = models.IntegerField(blank=False, default=0)
    url = models.CharField(max_length=128, blank=False, default='')


class Pokemon(models.Model):
    name = models.CharField(max_length=45, blank=False, unique=True)
    tamanho = models.IntegerField(blank=False, default=0)
    ordem = models.CharField(max_length=45, blank=False, default='')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

