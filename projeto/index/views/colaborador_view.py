from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from index.models import Colaborador, ColaboradorForm

@login_required(login_url='accounts/signin')
def colaborador(request):
    if request.method == 'GET':
        colaboradores = Colaborador.objects.all()
        return render(request, 'colaborador.html', {'colaboradores': colaboradores, 'usuario': request.user.username})

    elif request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('colaborador'))
        else:
            # Crie um formulário vazio (ou preenchido com os dados existentes do usuário)
            form = ColaboradorForm()
            
        return render(request, 'colaborador.html', {'form': form})