from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser

class Lideres(AbstractUser):   
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tipo = models.CharField(default='Líder', max_length=20)
    ativo = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'nome', 'departamento', 'tipo']

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
    
class LideresForm(forms.ModelForm):
    class Meta:
        model = Lideres
        fields = ['nome', 'departamento', 'email', 'password']
        
    widgets = {
        'password': forms.PasswordInput(),
    }
        

class Colaboradores(models.Model):   
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField()
    tipo = models.CharField(default='Colaborador', max_length=20)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
    
class ColaboradoresForm(forms.ModelForm):
    class Meta:
        model = Colaboradores
        fields = ['nome', 'departamento', 'email', 'senha']
        
    widgets = {
        'senha': forms.PasswordInput(),
    }
        
