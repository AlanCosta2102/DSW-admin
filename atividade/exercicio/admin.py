from django.contrib import admin
from .models import Produto
from .models import Fornecedor
from .models import Categoria

admin.site.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod_produto', 'nome_produto', 'preco', 'qntd_estoque','data_criacao')

    search_fields = ('cod_produto', 'nome')
    ordering = ('data_criacao',)

admin.site.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome_fornecedor', 'cod_fornecedor')

admin.site.register(Categoria)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('cod_categoria', 'nome_categoria')