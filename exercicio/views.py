from django.shortcuts import render
from .models import Produto
from .models import Categoria

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos
    }

    return render(request, 'index.html', context)

