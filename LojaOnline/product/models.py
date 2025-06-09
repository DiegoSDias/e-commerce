from django.db import models

class Categoria(models.Model):
    id_categoria = models.IntegerField()  # PK
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'categoria'
        managed = False
        
class Produto(models.Model):
    id_produto = models.IntegerField()  # PK
    nome = models.CharField(max_length=50)
    valor_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=255)
    quantEstoque_disponivel = models.IntegerField()
    quantEstoque_min = models.IntegerField()
    quantEstoque_max = models.IntegerField()
    id_categoria = models.IntegerField()
    id_fornecedor = models.CharField(max_length=100)

    class Meta:
        db_table = 'produto'
        managed = False

class Pedidos(models.Model):
    id_pedido = models.IntegerField()  # PK
    id_usuario = models.CharField(max_length=100)
    status_pedido = models.CharField(max_length=255)
    data_pedido = models.DateField()
    id_envio = models.IntegerField()

    class Meta:
        db_table = 'pedidos'
        managed = False

class Prod_Pedido(models.Model):
    id_produto = models.IntegerField()
    id_pedido = models.IntegerField()
    quant = models.IntegerField()

    class Meta:
        db_table = 'prod_pedido'
        managed = False

class Pagamento(models.Model):
    id_pagamento = models.IntegerField()  # PK
    id_pedido = models.IntegerField()
    metodo_pag = models.CharField(max_length=10)
    status_pagamento = models.CharField(max_length=100)

    class Meta:
        db_table = 'pagamento'
        managed = False

class Metodo_Pag(models.Model):
    metodo_pag = models.CharField(max_length=10)  # PK
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'metodo_pag'
        managed = False

class Pag_Vista(models.Model):
    id_pagVista = models.IntegerField()  # PK
    metodo_pag = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    max_parcelas = models.IntegerField()
    quant_parcelas = models.IntegerField()

    class Meta:
        db_table = 'pag_vista'
        managed = False

class Pag_Prazo(models.Model):
    id_pagPrazo = models.IntegerField()  # PK
    metodo_pag = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    max_parcelas = models.IntegerField()
    quant_parcelas = models.IntegerField()

    class Meta:
        db_table = 'pag_prazo'
        managed = False

class Envio(models.Model):
    id_envio = models.IntegerField()  # PK
    data_envio = models.DateField()
    data_prevista_entrega = models.DateField()
    status_envio = models.CharField(max_length=20)

    class Meta:
        db_table = 'envio'
        managed = False