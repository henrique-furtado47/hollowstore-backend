from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import Produto
from ..pagination import CustomPagination
from ..serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'categoria__nome': ['exact', 'icontains'], 'tipo__nome': ['exact', 'icontains'], 'preco': ['gte', 'lte']}
    search_fields = ['nome', 'descricao']
    ordering_fields = ['preco', 'nome']
    ordering = ['id']
    pagination_class = CustomPagination

    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
