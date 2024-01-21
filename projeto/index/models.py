from django import forms
from django.db import models


class Usuarios(models.Model):
    TIPO_CHOICES = (
        ("Líder", "Lider"),
        ("Colaborador", "Colaborador")
    )
    
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=False, null=False)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento} - {self.tipo}"
    
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'departamento', 'email', 'tipo', 'senha']
        
    widgets = {
        'senha': forms.PasswordInput(),
        'tipo': forms.Select(choices=Usuarios.TIPO_CHOICES),
    }
        

class Lideres(models.Model):   
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    email = models.EmailField()
    tipo = models.CharField(default='Líder', max_length=20)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.departamento}"
    
class LideresForm(forms.ModelForm):
    class Meta:
        model = Lideres
        fields = ['nome', 'departamento', 'email', 'senha']
        
    widgets = {
        'senha': forms.PasswordInput(),
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
        
