from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Categoria, Produto, Tipo, Pedido
from .serializers import CategoriaSerializer, ProdutoSerializer, TipoSerializer, PedidoSerializer

from .pagination import CustomPagination

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer.
        """
        # Se a ação for 'list' (GET em múltiplos) ou 'retrieve' (GET em um único),
        # usamos AllowAny, permitindo acesso público.
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        # Para todas as outras ações (create, update, destroy, etc.),
        # exigimos que o usuário esteja autenticado.
        else:
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer.
        """
        # Se a ação for 'list' (GET em múltiplos) ou 'retrieve' (GET em um único),
        # usamos AllowAny, permitindo acesso público.
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        # Para todas as outras ações (create, update, destroy, etc.),
        # exigimos que o usuário esteja autenticado.
        else:
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

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
        # Se a ação for 'list' (GET em múltiplos) ou 'retrieve' (GET em um único),
        # usamos AllowAny, permitindo acesso público.
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        # Para todas as outras ações (create, update, destroy, etc.),
        # exigimos que o usuário esteja autenticado.
        else:
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_queryset(self):
        return Pedido.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)