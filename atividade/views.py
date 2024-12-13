from django.shortcuts import render, get_object_or_404
from .models import Produto, Fornecedor, Categoria

# View para listar produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'atividade/lista_produtos.html', {'produtos': produtos})

# View para listar fornecedores
def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'atividade/lista_fornecedores.html', {'fornecedores': fornecedores})

# View para listar categorias
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'atividade/lista_categorias.html', {'categorias': categorias})

# View para detalhes de um produto
def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'atividade/detalhes_produto.html', {'produto': produto})
