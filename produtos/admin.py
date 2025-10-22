from django.contrib import admin

from .models import Categoria, Produto, Tipo

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
    ordering = ('nome',)