from django.db import models


class Escola(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=13)
    datanc = models.DateField()

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

    def __str__(self):
        return self.nome


