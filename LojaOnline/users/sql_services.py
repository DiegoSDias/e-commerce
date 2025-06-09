from django.db import connection
from django.http import HttpResponse

def testar_banco(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()[0]
    return HttpResponse(f"Conectado ao banco: {db}")

def cadastrar_usuario(cpf, nome, email, senha, telefone, data_nascimento):
    with connection.cursor() as cursor:
        try:
            sql = """
                INSERT INTO Usuario(cpf, nome, email, senha, telefone, data_nascimento)
                VALUEs (%s, %s, %s, %s, %s, %s)
                """
            cursor.execute(sql, [cpf, nome, email, senha, telefone, data_nascimento])
            
        except Exception as e:
            print("ERRO AO INSERIR:", e)
        
def autentificar_usuario(email, senha):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM Usuario WHERE email = %s AND senha = %s
        """, [email, senha])
        usuario = cursor.fetchone()
        return usuario
        