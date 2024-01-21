from django import forms
from django.db import models
from index.models import Lideres, Colaboradores

class Reuniao(models.Model):
    id_lider = models.ForeignKey(Lideres, on_delete=models.DO_NOTHING)
    id_colaborador = models.ForeignKey(Colaboradores, on_delete=models.DO_NOTHING)
    data = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id_lider} - {self.id_colaborador} - {self.data}"
    
class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = Reuniao
        fields = ['id_lider', 'id_colaborador', 'data']
