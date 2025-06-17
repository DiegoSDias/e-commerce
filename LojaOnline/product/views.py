from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .sql_services import (salvar_produto, salvar_categoria, salvar_marca, salvar_fornecedor, 
                           salvar_endereco, atualizar_produto, atualizar_categoria, atualizar_marca, 
                           atualizar_fornecedor, atualizar_endereco, salvar_endereco_usuario, salvar_pedidos,
                           salvar_carrinho, editar_quant_carrinho, remover_item_carrinho)
import json

def smartphones(request):
    return render(request, "smartphones/smartphones.html")

def brand(request):
    return render(request, "brands/brand.html")

def accessories(request):
    return render(request, "accessories/accessories.html")

def cart(request):
    return render(request, "cart/cart.html")


def adicionar_produto(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_categoria, nome FROM categoria")
        categorias = cursor.fetchall()
        
        cursor.execute("SELECT id_marca, nome FROM marca")
        marcas = cursor.fetchall()

        cursor.execute("SELECT CNPJ, nome FROM fornecedor")
        fornecedores = cursor.fetchall()
        
        cursor.execute("SELECT id_endereco, rua, numero, cidade FROM endereco")
        enderecos = cursor.fetchall()
        
    return render(request, "products/add_product.html", {
        "categorias": categorias,
        "marcas": marcas,
        "fornecedores": fornecedores,
        "enderecos": enderecos
    })

def add_product(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        nome = dados.get('nome'),
        descricao = dados.get('descricao'),
        valor_unitario = dados.get('valor_unitario'),
        quantEstoque_disponivel = dados.get('quantEstoque_disponivel'),
        quantEstoque_min = dados.get('quantEstoque_min'),
        quantEstoque_max = dados.get('quantEstoque_max'),
        id_categoria = dados.get('id_categoria'),
        id_fornecedor = dados.get('id_fornecedor'),
        id_marca = dados.get('id_marca'),
        
        salvar_produto(nome, valor_unitario, descricao, quantEstoque_disponivel, quantEstoque_min, quantEstoque_max, id_categoria, id_marca, id_fornecedor)
        return JsonResponse({'sucesso': 'Produto cadastrado com sucesso'})

    return JsonResponse({'erro': 'Método não permitido'}, status=405)

def add_category(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        nome = dados.get("nome")
        
        salvar_categoria(nome)
        return JsonResponse({"sucesso": "Categoria cadastrado com sucesso"})
    
    return JsonResponse({"erro": "Método não permitido"}, status=405)

def add_marca(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        nome = dados.get("nome")
        salvar_marca(nome)
        return JsonResponse({"sucesso": "Marca cadastrado com sucesso"})
    
    return JsonResponse({"erro": "Método não permitido"}, status=405)

def add_address(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        rua = dados.get("rua")
        numero = dados.get("numero")
        cep = dados.get("cep")
        cidade = dados.get("cidade")
        estado = dados.get("estado")
        complemento = dados.get("complemento")
        ponto_referencia = dados.get("ponto_referencia")
        
        salvar_endereco(rua, numero, cep, cidade, estado, complemento, ponto_referencia)
        return JsonResponse({"sucesso": "Endereço cadastrado com sucesso"})
    
    return JsonResponse({"erro": "Método não permitido"}, status=405)

def add_supplier(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        cnpj = dados.get("cnpj")
        nome = dados.get("nome_fornecedor")
        email = dados.get("email_fornecedor")
        telefone = dados.get("telefone_fornecedor")
        id_endereco = dados.get("id_endereco")

        salvar_fornecedor(cnpj, nome, email, telefone, id_endereco)
        return JsonResponse({"sucesso": "Fornecedor cadastrado com sucesso"})
    return JsonResponse({"erro": "Método não permitido"}, status=405)

def listar_opcoes(request, tipo):
    mapa = {
        'produto': "SELECT id_produto, nome, valor_unitario, descricao FROM produto",
        'categoria': "SELECT id_categoria, nome FROM categoria",
        'marca': "SELECT id_marca, nome FROM marca",
        'fornecedor': "SELECT CNPJ, nome, email, telefone FROM fornecedor",
        'endereco': "SELECT id_endereco, rua, numero, CEP, cidade FROM endereco"
    }

    if tipo not in mapa:
        return JsonResponse({'erro': 'Tipo inválido'}, status=400)

    with connection.cursor() as cursor:
        cursor.execute(mapa[tipo])
        dados = cursor.fetchall()

    if tipo == 'endereco':
        resultados = [{'id': r[0], 'nome': f"{r[1]}, {r[2]} - {r[3]}, {r[4]}"} for r in dados]
    elif tipo == 'produto':
        resultados = [{'id': r[0], 'nome': f"{r[1]} - R${r[2]}, Descrição: {r[3]}"} for r in dados]
    elif tipo == 'fornecedor':
        resultados = [{'id': r[0], 'nome': f"{r[0]}, {r[1]}, {r[2]}, {r[3]}"} for r in dados]
    else:
        resultados = [{'id': r[0], 'nome': r[1]} for r in dados]

    return JsonResponse({'resultados': resultados})


def add_address_user(request):
        cpf_usuario = request.session.get('cpf_usuario')
        if not cpf_usuario:
            return JsonResponse({"erro": "Usuário não autenticado"}, status=401)

        if request.method == "POST":
            dados = json.loads(request.body)
            rua = dados.get("rua")
            numero = dados.get("numero")
            cep = dados.get("cep")
            cidade = dados.get("cidade")
            estado = dados.get("estado")
            complemento = dados.get("complemento")
            ponto_referencia = dados.get("ponto_referencia")
            
            salvar_endereco_usuario(rua, numero, cep, cidade, estado, complemento, ponto_referencia, cpf_usuario)
            return JsonResponse({"sucesso": "Endereço cadastrado com sucesso"})
    
        return JsonResponse({"erro": "Método não permitido"}, status=405)
            
def listar_end_usuario(request, tipo):
    # Obtem o CPF do usuário logado
    cpf_usuario = request.session.get('cpf_usuario')
    mapa = {
        'endereco': """
            SELECT e.id_endereco, e.rua, e.numero, e.CEP, e.cidade
            FROM endereco e
            JOIN usuario_end ue ON e.id_endereco = ue.id_endereco
            WHERE ue.CPF = %s
        """
    }

    if tipo not in mapa:
        return JsonResponse({'erro': 'Tipo inválido'}, status=400)

    with connection.cursor() as cursor:
        if tipo == 'endereco':
            cursor.execute(mapa[tipo], [cpf_usuario])
        else:
            cursor.execute(mapa[tipo])
        dados = cursor.fetchall()

    # Formata os resultados com base no tipo
    if tipo == 'endereco':
        resultados = [{'id': r[0], 'nome': f"{r[1]}, {r[2]} - {r[3]}, {r[4]}"} for r in dados]

    return JsonResponse({'resultados': resultados})

def excluir_endereco(request, id):
    if request.method == "DELETE":

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM usuario_end WHERE id_endereco = %s", [id])
            cursor.execute("DELETE FROM endereco WHERE id_endereco = %s", [id])

        return JsonResponse({"sucesso": "Item excluído com sucesso"})
    return JsonResponse({"erro": "Método não permitido"}, status=405)

def excluir_item(request, tipo, id):
    if request.method == "DELETE":
        with connection.cursor() as cursor:
            if tipo == "produto":
                cursor.execute("DELETE FROM produto WHERE id_produto = %s", [id])
            elif tipo == "categoria":
                cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", [id])
            elif tipo == "marca":
                cursor.execute("DELETE FROM marca WHERE id_marca = %s", [id])
            elif tipo == "fornecedor":
                cursor.execute("DELETE FROM fornecedor WHERE CNPJ = %s", [id])
            elif tipo == "endereco":
                cursor.execute("DELETE FROM endereco WHERE id_endereco = %s", [id])
            else:
                return JsonResponse({"erro": "Tipo inválido"}, status=400)
            return JsonResponse({"sucesso": "Item excluído com sucesso"})
    return JsonResponse({"erro": "Método não permitido"}, status=405)

def detalhe_produto(request, tipo):
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT p.*, m.nome AS 'nome_marca', c.nome AS 'nome_categoria' FROM produto p
                        LEFT JOIN marca m ON p.id_marca = m.id_marca LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
                    """)
        
        # Acessar a descrição das colunas antes de consumir o cursor
        columns = [col[0] for col in cursor.description]
        
        # Agora, obtenha os resultados
        resultado = cursor.fetchall()
        
    if not resultado:
        return JsonResponse({'erro': 'Produto não encontrado'}, status=404)

    # Criar o dicionário a partir dos resultados
    resultado_dict = [dict(zip(columns, row)) for row in resultado]  # Criando uma lista de dicionários
    return JsonResponse({'resultados': resultado_dict})  # Retorne os resultados em um dicionário


def detalhe_item(request, tipo, id):
    with connection.cursor() as cursor:
        if tipo == "produto":
            cursor.execute("SELECT * FROM produto WHERE id_produto = %s", [id])
        elif tipo == "categoria":
            cursor.execute("SELECT * FROM categoria WHERE id_categoria = %s", [id])
        elif tipo == "marca":
            cursor.execute("SELECT * FROM marca WHERE id_marca = %s", [id])
        elif tipo == "fornecedor":
            cursor.execute("SELECT * FROM fornecedor WHERE CNPJ = %s", [id])
        elif tipo == "endereco":
            cursor.execute("SELECT * FROM endereco WHERE id_endereco = %s", [id])
        else:
            return JsonResponse({"erro": "Tipo inválido"}, status=400)
        
        resultado = dict_fetch_one(cursor)

    if resultado:
        return JsonResponse(resultado)
    return JsonResponse({"erro": "Item não encontrado"}, status=404)

def dict_fetch_one(cursor):
    """Retorna uma linha de uma consulta como um dicionário."""
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
    if row:
        return dict(zip(columns, row))
    return None

def edit_item(request, tipo, id):
    if request.method == "PUT":
        dados = json.loads(request.body)
        with connection.cursor() as cursor:
            if tipo == "produto":
                atualizar_produto(id, dados)
            elif tipo == "categoria":
                atualizar_categoria(id, dados)
            elif tipo == "marca":
                atualizar_marca(id, dados)
            elif tipo == "fornecedor":
                atualizar_fornecedor(id, dados)
            elif tipo == "endereco":
                atualizar_endereco(id, dados)
            else:
                return JsonResponse({"erro": "Tipo inválido"}, status=400)
            return JsonResponse({"sucesso": "Item atualizado com sucesso"})
    return JsonResponse({"erro": "Método não permitido"}, status=405)


def finalizar_produto(request):
    return render(request, "brands/finalizar_produto.html")


def salvar_pedido(request):
    cpf_usuario = request.session.get('cpf_usuario')
    if not cpf_usuario:
        return JsonResponse({"erro": "Usuário não autenticado"}, status=401)

    dados = json.loads(request.body)
    metodo_pag = dados.get("metodo_pag")
    tipo = dados.get("tipo")
    id_endereco = dados.get("id_endereco")
    descricao = dados.get("descricao"),
    parcelas = dados.get("parcelas"),
    max_parcelas = dados.get("max_parcelas")
    
    salvar_pedidos(cpf_usuario, id_endereco, metodo_pag, tipo, descricao, parcelas, max_parcelas)
    return JsonResponse({'sucesso': 'Pedido cadastrado com sucesso'})
    

def criar_carrinho(request):
    
    cpf_usuario = request.session.get('cpf_usuario')
    if not cpf_usuario:
        return JsonResponse({"erro": "Usuário não autenticado"}, status=401)
        
    dados = json.loads(request.body)
    id_produto = dados.get("productId")
    
    salvar_carrinho(cpf_usuario, id_produto)
    return JsonResponse({'sucesso': 'Carrinho cadastrado com sucesso'})
    
def mostra_carrinho(request):
    cpf_usuario = request.session.get('cpf_usuario')
    if not cpf_usuario:
        return JsonResponse({"erro": "Usuário não autenticado"}, status=401)
    
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT p.nome, p.valor_unitario, cp.quant, cp.id_carrinho, cp.id_produto FROM carrinho c
                        JOIN carrinho_produto cp ON c.id_carrinho = cp.id_carrinho
                        JOIN produto p ON cp.id_produto = p.id_produto
                        WHERE c.id_usuario = %s;
                        """, [cpf_usuario])
            
         # Acessar a descrição das colunas antes de consumir o cursor
        columns = [col[0] for col in cursor.description]
        
        # Agora, obtenha os resultados
        resultado = cursor.fetchall()
        
    if not resultado:
        return JsonResponse({'erro': 'Produto não encontrado'}, status=404)

    # Criar o dicionário a partir dos resultados
    resultado_dict = [dict(zip(columns, row)) for row in resultado]  # Criando uma lista de dicionários
    return JsonResponse({'resultado': resultado_dict})  # Retorne os resultados em um dicionário

def editar_quant(request):
    
    cpf_usuario = request.session.get('cpf_usuario')
    if not cpf_usuario:
        return JsonResponse({"erro": "Usuário não autenticado"}, status=401)
    
    dados = json.loads(request.body)
    quant = dados.get("quant")
    id_carrinho = dados.get("id_carrinho")
    id_produto = dados.get("id_produto")
    editar_quant_carrinho(id_carrinho, id_produto, quant)
    return JsonResponse({"sucesso": "Item atualizado com sucesso"})
   
def remover_item(request):
    
    dados = json.loads(request.body)
    id_carrinho = dados.get("id_carrinho")
    id_produto = dados.get("id_produto")
    
    remover_item_carrinho(id_carrinho, id_produto)
    return JsonResponse({"sucesso": "Item atualizado com sucesso"})