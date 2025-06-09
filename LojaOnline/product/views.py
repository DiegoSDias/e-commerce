from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .sql_services import salvar_produto, salvar_categoria, salvar_fornecedor, salvar_endereco
import json

def smartphones(request):
    return render(request, "smartphones/smartphones.html")

def brand(request):
    return render(request, "brands/brand.html")

def accessories(request):
    return render(request, "accessories/accessories.html")

def promotion(request):
    return render(request, "promotion/promotion.html")

def launch(request):
    return render(request, "launch/launch.html")

def cart(request):
    return render(request, "cart/cart.html")

def smartphones_marca(request, marca):
    #lista = NOMEDATABELA.objects.filter(marca__iexact=marca)
    #return render(request, "smartphones/smartphones.html", {"smartphones": lista})
    print("oi")

def adicionar_produto(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_categoria, nome FROM categoria")
        categorias = cursor.fetchall()

        cursor.execute("SELECT CNPJ, nome FROM fornecedor")
        fornecedores = cursor.fetchall()
        
        cursor.execute("SELECT id_endereco, rua, numero, cidade FROM endereco")
        enderecos = cursor.fetchall()
        
    return render(request, "products/add_product.html", {
        "categorias": categorias,
        "fornecedores": fornecedores,
        "enderecos": enderecos
    })

def add_category(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        nome = dados.get("nome")
        
        salvar_categoria(nome)
        return JsonResponse({'sucesso': 'Categoria cadastrado com sucesso'})
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

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
        return JsonResponse({'sucesso': 'Categoria cadastrado com sucesso'})
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

def add_supplier(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        cnpj = dados.get("cnpj")
        nome_fornecedor = dados.get("nome_fornecedor")
        email_fornecedor = dados.get("email_fornecedor")
        telefone_fornecedor = dados.get("telefone_fornecedor")
        endereco_fornecedor = dados.get("endereco_fornecedor")
        
        salvar_fornecedor(cnpj, nome_fornecedor, email_fornecedor, telefone_fornecedor, endereco_fornecedor)
        return JsonResponse({'sucesso': 'Fornecedor cadastrado com sucesso'})
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

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
        id_fornecedor = dados.get('id_fornecedor')
        
        print("DADOS: ", dados)
        
        salvar_produto(nome, valor_unitario, descricao, quantEstoque_disponivel, quantEstoque_min, quantEstoque_max, id_categoria, id_fornecedor)
        return JsonResponse({'sucesso': 'Produto cadastrado com sucesso'})

    return JsonResponse({'erro': 'Método não permitido'}, status=405)

def listar_opcoes(request, tipo):
    mapa = {
        'produto': "SELECT id_produto, nome, valor_unitario FROM produto",
        'categoria': "SELECT id_categoria, nome FROM categoria",
        'fornecedor': "SELECT CNPJ, nome FROM fornecedor",
        'endereco': "SELECT id_endereco, rua, numero, cidade FROM endereco"
    }

    if tipo not in mapa:
        return JsonResponse({'erro': 'Tipo inválido'}, status=400)

    with connection.cursor() as cursor:
        cursor.execute(mapa[tipo])
        dados = cursor.fetchall()

    if tipo == 'endereco':
        resultados = [{'id': r[0], 'nome': f"{r[1]}, {r[2]} - {r[3]}"} for r in dados]
    elif tipo == 'produto':
        resultados = [{'id': r[0], 'nome': f"{r[1]} - R${r[2]}"} for r in dados]
    else:
        resultados = [{'id': r[0], 'nome': r[1]} for r in dados]

    return JsonResponse({'resultados': resultados})

def excluir_item(request, tipo, id):
    if request.method != "DELETE":
        return JsonResponse({'erro': 'Método não permitido'}, status=405)
    
    mapa = {
        'produto': ('produto', 'id_produto'),
        'categoria': ('categoria', 'id_categoria'),
        'fornecedor': ('fornecedor', 'CNPJ'),
        'endereco': ('endereco', 'id_endereco')
    }

    if tipo not in mapa:
        return JsonResponse({'erro': 'Tipo inválido'}, status=400)

    tabela, campo = mapa[tipo]

    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM {tabela} WHERE {campo} = %s", [id])

    return JsonResponse({'sucesso': f'{tipo.capitalize()} excluído com sucesso'})