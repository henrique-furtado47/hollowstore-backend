from rest_framework import serializers

from .models import Categoria, Produto, Tipo, Pedido, ItemPedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'nome', 'descricao']

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    tipo = TipoSerializer()

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'preco', 'categoria', 'tipo', 'imagem',
            'dano', 'defesa', 'durabilidade', 'seda', 'alma', 'slot_custo', 'efeito',
        ]
        
class ItemPedidoSerializer(serializers.ModelSerializer):
    # Mostra o nome do produto ao invés de apenas o ID na leitura
    nome_produto = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = ItemPedido
        fields = ['produto', 'nome_produto', 'quantidade', 'preco_unitario']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'status', 'data_criacao', 'total', 'itens']