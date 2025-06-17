from django.db import connection
from django.http import JsonResponse
from datetime import datetime, date, timedelta

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
            return JsonResponse({'sucesso': True})
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
        
def salvar_endereco_usuario(rua, numero, cep, cidade, estado, complemento, ponto_referencia, cpf_usuario):
    try:
        with connection.cursor() as cursor:
            # Inserir endereço
            cursor.execute("""
                INSERT INTO endereco (rua, numero, cep, cidade, estado, complemento, ponto_referencia)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, [rua, numero, cep, cidade, estado, complemento, ponto_referencia])

            id_endereco = cursor.lastrowid

            # Relacionar endereço ao usuário
            cursor.execute("""
                    INSERT INTO usuario_end (cpf, id_endereco) VALUES (%s, %s)
                """, [cpf_usuario, id_endereco])

            return JsonResponse({"sucesso": "Endereço cadastrado e relacionado com sucesso"})

        return JsonResponse({"erro": "Método não permitido"}, status=405)

    except Exception as e:
        print("Erro ao cadastrar e relacionar endereço:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)
    
    
def salvar_pedidos(cpf_usuario, id_endereco, metodo_pag, tipo, descricao, parcelas, max_parcelas):
    try:
        with connection.cursor() as cursor:
            # Cria novo pedido
            cursor.execute("""
                INSERT INTO pedidos (id_usuario, status_pedido, data_pedido)
                VALUES (%s, %s, %s)
            """, [cpf_usuario, 'p', date.today()])
            
            id_pedido = cursor.lastrowid
            
            data_hoje = date.today() + timedelta(days=1)
            data_futura = data_hoje + timedelta(days=10)
            
            cursor.execute("""
                           INSERT INTO envio (data_envio, data_prevista_entrega, status_envio, id_pedido, id_endereco)
                           VALUES (%s, %s, %s, %s, %s)
                           """, [data_hoje, data_futura, 'en', id_pedido, id_endereco])
            
            # Pega o carrinho atual do usuário
            cursor.execute("""
                SELECT id_carrinho FROM carrinho WHERE id_usuario = %s
            """, [cpf_usuario])
            
            id_carrinho = cursor.fetchone()

            if not id_carrinho:
                return JsonResponse({"erro": "Carrinho não encontrado"}, status=404)
            
            id_carrinho = id_carrinho[0]

            # Transfere os produtos do carrinho para o pedido
            cursor.execute("""
                SELECT id_produto, quant FROM carrinho_produto WHERE id_carrinho = %s
            """, [id_carrinho])
            
            produtos = cursor.fetchall()

            for id_produto, quant in produtos:
                cursor.execute("""
                    INSERT INTO prod_pedido (id_produto, id_pedido, quant)
                    VALUES (%s, %s, %s)
                """, [id_produto, id_pedido, quant])

            # Limpa o carrinho (ou altera status dele, se preferir manter histórico)
            cursor.execute("""
                DELETE FROM carrinho_produto WHERE id_carrinho = %s
            """, [id_carrinho])
            
            cursor.execute("""
                            INSERT INTO metodo_pag (metodo_pag) VALUE (%s)
                           """, [metodo_pag])
            
            if metodo_pag == "vista":
                cursor.execute("""
                                INSERT INTO pag_vista (metodo_pag, tipo) VALUES (%s, %s)
                            """, [metodo_pag, tipo])
                
            elif metodo_pag == "prazo":
                cursor.execute("""
                                INSERT INTO pag_prazo (metodo_pag, tipo, max_parcelas, quant_parcelas, descricao) VALUES (%s, %s, %s, %s, %s)
                            """, [metodo_pag, tipo, max_parcelas, parcelas, descricao])

            cursor.execute("""
                                INSERT INTO pagamento (id_pedido, metodo_pag, status_pagamento) VALUES (%s, %s, %s)
                            """, [id_pedido, metodo_pag, "pg"])
            
        return JsonResponse({"sucesso": "Pedido finalizado com sucesso"})

    except Exception as e:
        print("Erro ao finalizar pedido:", e)
        return JsonResponse({"erro": "Erro no servidor"}, status=500)
    
        
def salvar_carrinho(id_usuario, id_produto):
    try:
        data_criacao = datetime.now()
        
        with connection.cursor() as cursor:

            # Verificar se já existe um carrinho para esse usuário
            cursor.execute("""
                SELECT id_carrinho FROM carrinho
                WHERE id_usuario = %s
            """, [id_usuario])

            carrinho_existente = cursor.fetchone()

            if carrinho_existente:
                id_carrinho = carrinho_existente[0]
            else:
                # Se não existir, cria um novo carrinho
                data_criacao = datetime.now().date()
                
                cursor.execute("""
                    INSERT INTO carrinho (id_usuario, data_criacao)
                    VALUES (%s, %s)
                """, [id_usuario, data_criacao])
                
                id_carrinho = cursor.lastrowid

            # Verifica se o produto já está no carrinho
            cursor.execute("""
                SELECT quant FROM carrinho_produto
                WHERE id_carrinho = %s AND id_produto = %s
            """, [id_carrinho, id_produto])

            produto_existente = cursor.fetchone()

            if produto_existente:
                # Produto já existe no carrinho → atualiza a quantidade
                nova_quant = produto_existente[0] + 1
                cursor.execute("""
                    UPDATE carrinho_produto
                    SET quant = %s
                    WHERE id_carrinho = %s AND id_produto = %s
                """, [nova_quant, id_carrinho, id_produto])
            else:
                # Produto ainda não está no carrinho → insere novo
                cursor.execute("""
                    INSERT INTO carrinho_produto (id_carrinho, id_produto, quant)
                    VALUES (%s, %s, %s)
                """, [id_carrinho, id_produto, 1])

            return JsonResponse({"sucesso": "Carrinho cadastrado e relacionado com sucesso"})

        return JsonResponse({"erro": "Método não permitido"}, status=405)

    except Exception as e:
        print("Erro ao cadastrar e relacionar endereço:", e)
        return JsonResponse({'erro': 'Erro no servidor'}, status=500)
    
def editar_quant_carrinho(id_carrinho, id_produto, quant):
     with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE carrinho_produto SET quant = %s WHERE id_carrinho = %s AND id_produto = %s",
            [quant, id_carrinho, id_produto],
        )
        
def remover_item_carrinho(id_carrinho, id_produto):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM carrinho_produto WHERE id_carrinho = %s AND id_produto = %s",
            [id_carrinho, id_produto]
        )