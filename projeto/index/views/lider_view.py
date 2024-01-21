from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from index.models import Lideres, LideresForm

@login_required
def lider(request):
    if request.method == 'GET':
        usuarios = Lideres.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})
    
    elif request.method == 'POST':
        form = LideresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario'))
        else:
            # Crie um formulário vazio (ou preenchido com os dados existentes do líder)
            form = LideresForm()
            
        return render(request, 'usuario.html', {'form': form})
