from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser

class Lider(AbstractUser):   
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tipo = models.CharField(default='Líder', max_length=20)
    ativo = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'departamento', 'tipo']

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
    
class LiderForm(forms.ModelForm):
    class Meta:
        model = Lider
        fields = ['username', 'departamento', 'email', 'password', 'groups']
        
    widgets = {
        'password': forms.PasswordInput(),
    }
    
class LiderFormSignup(forms.ModelForm):
    class Meta:
        model = Lider
        fields = ['email', 'password']
        
    widgets = {
        'password': forms.PasswordInput(),
    }
        

class Colaborador(models.Model):   
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField()
    tipo = models.CharField(default='Colaborador', max_length=20)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
    
class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'departamento', 'email', 'senha']
        
    widgets = {
        'senha': forms.PasswordInput(),
    }
    

        
