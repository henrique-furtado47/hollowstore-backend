from django.db import models
from django.contrib.auth.models import User


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

class Pedido(models.Model):
    # Definindo as opções de Status
    STATUS_CHOICES = (
        ('C', 'Carrinho'),
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('E', 'Enviado'),
        ('F', 'Cancelado'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Pedido {self.id} - {self.user.username}"

    # Método opcional para calcular o total do pedido
    @property
    def total(self):
        return sum(item.preco_unitario * item.quantidade for item in self.itens.all())

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT) # PROTECT impede deletar produto se houver venda
    quantidade = models.PositiveIntegerField(default=1)
    # É importante salvar o preço aqui, caso o preço do produto mude no futuro
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

    # Sobrescreve o save para pegar o preço do produto automaticamente se não informado
    def save(self, *args, **kwargs):
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco
            self.imagem = self.produto.imagem
        super().save(*args, **kwargs)