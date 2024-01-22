from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts/signin')
def index(request):
    username = request.user.username
    return render(request, 'index.html', {'usuario': username})