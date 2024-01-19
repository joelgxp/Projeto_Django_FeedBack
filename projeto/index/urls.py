from django.urls import path
from .views import index_view, usuario_view

urlpatterns = [
    path('', index_view.index, name='index'),
    path('usuario/', usuario_view.usuarios, name='usuario'),
    path('usuario/criar_editar_usuario/', usuario_view.criar_editar_usuario, name='criar_editar_usuario'),
    path('criar_conta/', usuario_view.cadastrar_login, name='criar_conta'),
    path('logar/', usuario_view.logar, name='logar'),
    path('logout/', usuario_view.logout, name='logout')
]