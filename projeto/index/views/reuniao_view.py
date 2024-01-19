from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from index.models import Reunioes

@login_required
def reuniao(request):
    reunioes = Reunioes.objects.all()
    return render(request, 'reuniao.html')