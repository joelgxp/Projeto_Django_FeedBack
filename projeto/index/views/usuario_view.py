from django.shortcuts import render, redirect
from index.models import Usuarios, UsuarioForm
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http.response import HttpResponse

def cadastrar_login(request):
    if request.method == "GET":
        return render(request, 'criar_conta.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        senha_confirmar = request.POST.get('senha_confirmar')
        
        if not senha == senha_confirmar:
            messages.add_message(request, constants.ERROR, 'As senhas não coincídem.')
            return redirect('criar_conta')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado.')
            return redirect('criar_conta')
        try:
            User.objects.create_user(
                username=username,
                password=senha
            )
            return redirect('logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor.')
            return redirect('/criar_conta')

def logar(request):
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
            return redirect('logar')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('logar')

@login_required
def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuario.html', {'usuarios': usuarios})

@login_required
def criar_editar_usuario(request, usuario_id=None):
    # Verifique se o usuario existe ou cria um novo
    if usuario_id:
        usuario = Usuarios.objects.get(pk=usuario_id)
    else:
        usuario = Usuarios()

    if request.method == 'POST':
        # Crie um formulário com os dados do POST e os dados existentes do usuario
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario'))
    else:
        # Crie um formulário vazio (ou preenchido com os dados existentes do líder)
        form = UsuarioForm(instance=usuario)

    return render(request, 'formulario.html', {'form': form})