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
        fields = ['produto', 'nome_produto', 'quantidade', 'preco_unitario',"imagem"]

class PedidoSerializer(serializers.ModelSerializer):
    # Removido o read_only=True para permitir escrita
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'status', 'data_criacao', 'total', 'itens']

    def create(self, validated_data):
        # 1. Separa os dados dos itens dos dados do pedido principal
        itens_data = validated_data.pop('itens')
        
        # 2. Cria o Pedido (o usuário já vem no validated_data ou via perform_create da view)
        pedido = Pedido.objects.create(**validated_data)
        
        # 3. Cria cada ItemPedido vinculado a esse novo pedido
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
            
        return pedido