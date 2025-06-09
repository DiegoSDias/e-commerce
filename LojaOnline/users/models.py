from django.db import models

class Usuario(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    class Meta:
        db_table = 'usuario'
        managed = False


class Endereco(models.Model):
    id_endereco = models.IntegerField()
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    CEP = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=100)
    complemento = models.CharField(max_length=20)
    ponto_referencia = models.CharField(max_length=50)

    class Meta:
        db_table = 'endereco'
        managed = False


class Usuario_End(models.Model):
    CPF = models.CharField(max_length=100)
    id_endereco = models.IntegerField()

    class Meta:
        db_table = 'usuario_end'
        managed = False


class Fornecedor(models.Model):
    CNPJ = models.CharField(max_length=100)
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    id_endereco = models.IntegerField()

    class Meta:
        db_table = 'fornecedor'
        managed = False