from django.contrib import admin

from .models import Categoria, Produto, Tipo, Pedido, ItemPedido

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'tipo', 'imagem')
    list_filter = ('categoria', 'tipo')
    search_fields = ('nome', 'descricao')
    ordering = ('id',)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1  # Quantas linhas vazias aparecem por padrão
    readonly_fields = ('preco_unitario',) # Opcional: impedir edição de preço após criado

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'data_criacao', 'total')
    list_filter = ('status', 'data_criacao')
    inlines = [ItemPedidoInline]