from django.urls import path
from .views import index_view, usuario_view, colaborador_view, lider_view

urlpatterns = [
    path('', index_view.index, name='index'),
    
    path('lider/', lider_view.lider, name='lider'),
    path('colaborador/', colaborador_view.colaborador, name='colaborador'),
    
    path('accounts/signup/', usuario_view.signup, name='accounts/signup'),
    path('accounts/signin/', usuario_view.signin, name='accounts/signin'),
    path('accounts/logout/', usuario_view.logout, name='accounts/logout')
]