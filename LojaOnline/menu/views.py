from django.shortcuts import render

def menu(request):
    cpf = request.session.get('cpf_usuario')
    is_superuser = cpf == '15989626645'
    print("is_superuser: ", is_superuser)
    return render(request, "menu/menu.html", {
        'is_superuser': is_superuser
    })
    
