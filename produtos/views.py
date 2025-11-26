from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Categoria, Produto, Tipo
from .serializers import CategoriaSerializer, ProdutoSerializer, TipoSerializer

from .pagination import CustomPagination

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'categoria__nome': ['exact', 'icontains'], 'tipo__nome': ['exact', 'icontains'], 'preco': ['gte', 'lte']}
    search_fields = ['nome', 'descricao']
    ordering_fields = ['preco', 'nome']
    ordering = ['id']
    pagination_class = CustomPagination
