from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from ..models import Reuniao, ReuniaoForm

@login_required
def reuniao(request):
    if request.method == 'GET':
        reunioes = Reuniao.objects.all()
        return render(request, 'reuniao.html', {'reunioes': reunioes})
    elif request.method == 'POST':
        form = ReuniaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('reunioes'))
        else:
            form = ReuniaoForm()
        
        return render(request, 'reuniao.html', {'form': form})