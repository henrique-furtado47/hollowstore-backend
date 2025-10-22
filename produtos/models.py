from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)    
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos'
    )
    tipo = models.ForeignKey(
        Tipo, on_delete=models.SET_NULL, null=True, related_name='produtos'
    )
    imagem = models.CharField(max_length=255, blank=True, null=True)
    # Campos opcionais
    dano = models.IntegerField(blank=True, null=True)
    defesa = models.FloatField(blank=True, null=True)
    durabilidade = models.IntegerField(blank=True, null=True)
    seda = models.FloatField(blank=True, null=True)
    alma = models.FloatField(blank=True, null=True)
    slot_custo = models.PositiveIntegerField(blank=True, null=True)
    efeito = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nome
