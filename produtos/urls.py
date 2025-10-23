from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet, ProdutoViewSet, TipoViewSet


router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'tipos', TipoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
