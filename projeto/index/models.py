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
        
class Reunioes(models.Model):
    id_lider = models.CharField(max_length=255)
    id_colaborador = models.CharField(max_length=255)
    data = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id_lider} - {self.id_colaborador} - {self.data}"
    