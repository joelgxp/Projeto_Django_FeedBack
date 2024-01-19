from django.urls import path
from .views import index_view, usuario_view, reuniao_view, colaborador_view

urlpatterns = [
    path('', index_view.index, name='index'),
    path('usuario/', usuario_view.usuarios, name='usuario'),
    path('colaborador/', colaborador_view.colaborador, name='colaborador'),
    path('reuniao/', reuniao_view.reuniao, name='reuniao'),
    path('criar_conta/', usuario_view.cadastrar_login, name='criar_conta'),
    path('accounts/login/', usuario_view.login, name='accounts/login'),
    path('accounts/logout/', usuario_view.logout, name='accounts/logout')
]