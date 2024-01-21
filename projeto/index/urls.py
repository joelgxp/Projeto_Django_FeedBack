from django.urls import path
from .views import index_view, usuario_view, colaborador_view, lider_view

urlpatterns = [
    path('', index_view.index, name='index'),
    path('usuario/', usuario_view.usuarios, name='usuario'),
    
    path('lider/', lider_view.lider, name='lider'),
    path('colaborador/', colaborador_view.colaborador, name='colaborador'),
    
    path('accounts/signup/', usuario_view.cadastrar_login, name='accounts/signup'),
    path('accounts/login/', usuario_view.login, name='accounts/login'),
    path('accounts/logout/', usuario_view.logout, name='accounts/logout')
]