from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rolepermissions.roles import assign_role


from index.models import Lider, LiderForm

@login_required(login_url='accounts/signin')
def lider(request):
    if request.method == 'GET':
        usuarios = Lider.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios, 'usuario': request.user.username})
    
    elif request.method == 'POST':
        form = LiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lider'))
        else:
            # Crie um formulário vazio (ou preenchido com os dados existentes do líder)
            form = LiderForm()
            
        return render(request, 'usuario.html', {'form': form})
  