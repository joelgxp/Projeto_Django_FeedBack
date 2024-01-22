from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from ..models import Lider, LiderFormSignup

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    
    elif request.method == 'POST':
        username =  request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        senha_confirmar = request.POST.get('senha_confirmar')
        
        if not password == senha_confirmar:
            messages.add_message(request, constants.ERROR, 'As senhas não coincídem.')
            return redirect('accounts/signup')
        
        user = Lider.objects.filter(email=email)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado.')
            return redirect('accounts/signup')
        try:
            Lider.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('accounts/signin')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor.')
            return redirect('accounts/signup')

def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/signin.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = auth.authenticate(request, username=username, password=senha)
        
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('index')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos.')
            return redirect('accounts/signin')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('accounts/signin')

