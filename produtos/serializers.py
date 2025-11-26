from rest_framework import serializers

from .models import Categoria, Produto, Tipo

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