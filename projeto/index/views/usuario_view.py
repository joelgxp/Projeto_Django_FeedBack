from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from index.models import Usuarios, UsuarioForm

def cadastrar_login(request):
    if request.method == "GET":
        return render(request, 'criar_conta.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        senha_confirmar = request.POST.get('senha_confirmar')
        
        if not senha == senha_confirmar:
            messages.add_message(request, constants.ERROR, 'As senhas não coincídem.')
            return redirect('accounts/signup')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado.')
            return redirect('accounts/signup/')
        try:
            User.objects.create_user(
                username=username,
                password=senha
            )
            return redirect('logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor.')
            return redirect('/criar_conta')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = auth.authenticate(request, username=username, password=senha)
        
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('usuario')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos.')
            return redirect('accounts/login')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('accounts/login')

@login_required
def usuarios(request):
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})
    
    elif request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario'))
        else:
            # Crie um formulário vazio (ou preenchido com os dados existentes do líder)
            form = UsuarioForm()
            
        return render(request, 'usuario.html', {'form': form})
