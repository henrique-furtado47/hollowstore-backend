from rest_framework import viewsets

from .models import Categoria, Produto, Tipo
from .serializers import CategoriaSerializer, ProdutoSerializer, TipoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    