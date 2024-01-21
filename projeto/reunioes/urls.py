from django.urls import path

from .views import reuniao_view

urlpatterns = [
    path('reunioes/', reuniao_view.reuniao, name='reunioes'),

]