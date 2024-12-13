from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('produto/<int:pk>/', views.detalhes_produto, name='detalhes_produto'),
]
