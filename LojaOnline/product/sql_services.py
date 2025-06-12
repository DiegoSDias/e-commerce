from django.db import connection
from django.http import JsonResponse

def salvar_produto(nome, valor_unitario, descricao, quantEstoque_disponivel, quantEstoque_min, quantEstoque_max, id_categoria, id_marca, id_fornecedor):
    try:
        
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO produto (nome, valor_unitario, descricao, quantEstoque_disponivel,
                quantEstoque_min, quantEstoque_max, id_categoria, id_marca, id_fornecedor)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, [nome, valor_unitario, descricao, quantEstoque_disponivel, quantEstoque_min, quantEstoque_max, id_categoria, id_marca, id_fornecedor])
        return JsonResponse({'sucesso': 'Produto cadastrado'})
    except Exception as e:
        print("Erro ao cadastrar produto:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)
    
def salvar_categoria(nome):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO categoria (nome) VALUE (%s)""", [nome])
        return JsonResponse({'sucesso': 'Erro no servidor'}, status=500)
    except Exception as e:
        print("Erro ao cadastrar categoria:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)
    
def salvar_marca(nome):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO marca (nome) VALUE (%s)""", [nome])
        return JsonResponse({'sucesso': 'Erro no servidor'}, status=500)
    except Exception as e:
        print("Erro ao cadastrar marca:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)
    
def salvar_endereco(rua, numero, cep, cidade, estado, complemento, ponto_referencia):
    try: 
        with connection.cursor() as cursor:
            cursor.execute("""
                           INSERT INTO endereco (rua, numero, cep, cidade, estado, complemento, ponto_referencia)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)
                           """, [rua, numero, cep, cidade, estado, complemento, ponto_referencia])
            return JsonResponse({'sucesso': 'Erro no servidor'}, status=500)
    except Exception as e:
        print("Erro ao cadastrar endereço:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)

def salvar_fornecedor(cnpj, nome, email, telefone, endereco):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO fornecedor (CNPJ, nome, email, telefone, id_endereco)
                        VALUES (%s, %s, %s, %s, %s)  
                           """, [cnpj, nome, email, telefone, endereco])
            return JsonResponse({'sucesso': 'Erro no servidor'}, status=500)
    except Exception as e:
        print("Erro ao cadastrar categoria:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)
    
def atualizar_produto(id, dados):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE produto SET nome = %s, descricao = %s, valor_unitario = %s, quantEstoque_disponivel = %s, quantEstoque_min = %s, quantEstoque_max = %s, id_categoria = %s, id_fornecedor = %s WHERE id_produto = %s",
            [
                dados["nome"],
                dados["descricao"],
                dados["valor_unitario"],
                dados["quantEstoque_disponivel"],
                dados["quantEstoque_min"],
                dados["quantEstoque_max"],
                dados["id_categoria"],
                dados["id_fornecedor"],
                id,
            ],
        )

def atualizar_categoria(id, dados):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE categoria SET nome = %s WHERE id_categoria = %s",
            [dados["nome"], id],
        )
        
def atualizar_marca(id, dados):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE marca SET nome = %s WHERE id_marca = %s",
            [dados["nome"], id],
        )

def atualizar_fornecedor(id, dados):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE fornecedor SET CNPJ = %s, nome = %s, email = %s, telefone = %s, id_endereco = %s WHERE CNPJ = %s",
            [
                dados["cnpj"],
                dados["nome_fornecedor"],
                dados["email_fornecedor"],
                dados["telefone_fornecedor"],
                dados["id_endereco"],
                id
            ],
        )

def atualizar_endereco(id, dados):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE endereco SET rua = %s, numero = %s, cep = %s, cidade = %s, estado = %s, complemento = %s, ponto_referencia = %s WHERE id_endereco = %s",
            [
                dados["rua"],
                dados["numero"],
                dados["cep"],
                dados["cidade"],
                dados["estado"],
                dados["complemento"],
                dados["ponto_referencia"],
                id,
            ],
        )