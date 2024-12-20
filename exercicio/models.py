from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length = 255, null = False, blank=False,verbose_name = "Nome da categoria")
    cod_categoria = models.CharField(max_length=100,unique=True,blank=False,null=False)


    def __str__(self):
       return self.nome_categoria
   
   
   

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255,null=False,blank=False)
    cod_produto = models.CharField(max_length=100, unique=True, blank=False, null=False)
    descricao = models.TextField(null=True,blank= True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qntd_estoque = models.IntegerField(null=False, blank=False)
    data_criacao = models.DateField(auto_now_add=True)
    categories =  models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nome_produto
    
class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=255,null=False,blank=False)
    cod_fornecedor = models.CharField(max_length=100, unique=True, blank=False, null=False)
    fornecer = models.ForeignKey(Produto, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome_fornecedor


class Meta:
    app_label = 'atividade'