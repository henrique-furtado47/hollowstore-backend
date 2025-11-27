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