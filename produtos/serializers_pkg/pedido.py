from rest_framework import serializers

from ..models import Pedido
from .item_pedido import ItemPedidoSerializer


class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'status', 'data_criacao', 'total', 'itens']
