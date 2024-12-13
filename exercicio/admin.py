from django.contrib import admin
from .models import Produto, Fornecedor, Categoria

class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod_produto', 'nome_produto', 'preco', 'qntd_estoque', 'data_criacao')
    search_fields = ('cod_produto', 'nome_produto')
    ordering = ('data_criacao',)

admin.site.register(Produto, ProductAdmin)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
