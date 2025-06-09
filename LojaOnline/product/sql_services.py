from django.db import connection
from django.http import JsonResponse

def salvar_produto(nome, valor_unitario, descricao, quantEstoque_disponivel, quantEstoque_min, quantEstoque_max, id_categoria, id_fornecedor):
    try:
        
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO produto (nome, valor_unitario, descricao, quantEstoque_disponivel,
                quantEstoque_min, quantEstoque_max, id_categoria, id_fornecedor)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, [nome, valor_unitario, descricao, quantEstoque_disponivel, quantEstoque_min, quantEstoque_max, id_categoria, id_fornecedor])
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
    