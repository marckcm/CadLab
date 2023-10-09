from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login 


def cadastro(request):
    if request.method == 'GET':
        return render(request,'cadastro.html')
    elif request.method == 'POST':
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        
        # Confirmações para validação de cadastro de usuário
        if len(primeiro_nome) < 4:
            messages.add_message(request, constants.ERROR, 'Primeiro nome deve conter mais 4 digitos')
            return redirect('/usuario/cadastro')
        
        if len(ultimo_nome) < 4:
            messages.add_message(request, constants.ERROR, 'Último nome deve conter mais 4 digitos')
            return redirect('/usuario/cadastro')
        
        if len(username) < 4:
            messages.add_message(request, constants.ERROR, 'Username tem que conter mais 4 digitos')
            return redirect('/usuario/cadastro')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect('/usuario/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que conter mais de 6 digitos')
            return redirect('/usuario/cadastro')
        
        # Filtra no banco de dados os usuários
        usuario_db = User.objects.filter(username=username).first()
        email_db = User.objects.filter(email=email).first()
        
        # Valida o e-mail pra não existir dois iguais no banco de dados.
        if email_db:
            if email == email_db.email:
                messages.add_message(request, constants.ERROR, 'E-mail Já existente')                
                return redirect('/usuario/cadastro')
            
        try:        
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso')
        except:
            # confere no banco de dados se ja existe o usuário
            if usuario_db:
                if username == usuario_db.username:
                    messages.add_message(request, constants.ERROR, 'Usuario Já existente')
                    return redirect('/usuario/cadastro')
        
        return redirect('/usuario/cadastro')


def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha') 

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/exames/solicitar_exames/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha Invalidos')
            return redirect('/usuario/login')




    
