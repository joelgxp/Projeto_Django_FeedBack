from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

from ..models import Reuniao, ReuniaoForm

@login_required(login_url='accounts/signin')
def reuniao(request):
    if request.method == 'GET':
        reunioes = Reuniao.objects.filter(Q(id_lider_id__username=request.user.username) | Q(id_colaborador_id__nome=request.user.username))

        return render(request, 'reuniao.html', {'reunioes': reunioes, 'usuario': request.user.username})
    
    elif request.method == 'POST':
        form = ReuniaoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(f"erro ao salvar: {e}")    
            return redirect(reverse('reunioes'))
        else:
            form = ReuniaoForm()
        
        return render(request, 'reuniao.html', {'form': form})