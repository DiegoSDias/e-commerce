from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .sql_services import cadastrar_usuario, autentificar_usuario
import json

def welcome(request):
    return render(request, "login_register/login_register.html")



def login(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        email = dados.get('email')
        senha = dados.get('senha')
        
        if not all([email, senha]):
            return JsonResponse({'erro': 'Email e senha são obrigatórios'}, status=400)
        
        user = autentificar_usuario(email, senha)
        
        if user is not None:
            print("User: ", user)
            request.session['cpf_usuario'] = user[0]
            return JsonResponse({'sucesso': 'Login realizado'})
        else:
            return JsonResponse({'erro': 'Credenciais inválidas'}, status=401)
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

def register(request):
    if request.method == "POST":
        dados = json.loads(request.body)

        cpf = dados.get("cpf")
        nome = dados.get("nome")
        email = dados.get("email")
        senha = dados.get("senha")
        telefone = dados.get("telefone")
        data_nascimento = dados.get("data_nascimento")

        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'erro': 'Email inválido'}, status=400)

        if not all([cpf, nome, email, senha, telefone, data_nascimento]):
            return JsonResponse({'erro': 'Todos os campos são obrigatórios'}, status=400)

        cadastrar_usuario(cpf, nome, email, senha, telefone, data_nascimento)
        return JsonResponse({'sucesso': 'Usuário cadastrado com sucesso'})

    # Se não for POST, retornar erro ou JSON
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

    
    
    