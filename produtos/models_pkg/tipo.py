from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.nome
