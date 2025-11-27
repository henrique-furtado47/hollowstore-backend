from django.contrib.auth.models import User
from django.db import models


class Pedido(models.Model):
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

    @property
    def total(self):
        return sum(item.preco_unitario * item.quantidade for item in self.itens.all())
