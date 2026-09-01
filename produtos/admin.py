from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Colunas mostradas na listagem do admin
    list_display = ('nome', 'categoria', 'preco', 'quantidade_estoque', 'ativo')
    # Filtros que aparecem na lateral direita
    list_filter = ('categoria', 'ativo')
    # Campo de busca no topo da listagem
    search_fields = ('nome', 'codigo_barras', 'fornecedor')
