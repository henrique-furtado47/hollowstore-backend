from rest_framework import serializers

from ..models import Produto
from .categoria import CategoriaSerializer
from .tipo import TipoSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    tipo = TipoSerializer()

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'preco', 'categoria', 'tipo', 'imagem',
            'dano', 'defesa', 'durabilidade', 'seda', 'alma', 'slot_custo', 'efeito',
        ]
