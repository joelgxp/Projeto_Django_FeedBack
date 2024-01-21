from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from index.models import Colaboradores, ColaboradoresForm

@login_required
def colaborador(request):
    if request.method == 'GET':
        colaboradores = Colaboradores.objects.all()
        return render(request, 'colaborador.html', {'colaboradores': colaboradores})

    elif request.method == 'POST':
        form = ColaboradoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('colaborador'))
        else:
            # Crie um formulário vazio (ou preenchido com os dados existentes do usuário)
            form = ColaboradoresForm()
            
        return render(request, 'colaborador.html', {'form': form})