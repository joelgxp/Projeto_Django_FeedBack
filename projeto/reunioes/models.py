from django import forms
from django.db import models
from index.models import Lider, Colaborador

class Reuniao(models.Model):
    id_lider = models.ForeignKey(Lider, on_delete=models.DO_NOTHING)
    id_colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING)
    data = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id_lider} - {self.id_colaborador} - {self.data}"
    
class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = Reuniao
        fields = ['id_lider', 'id_colaborador', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ReuniaoForm, self).__init__(*args, **kwargs)
        
        # Adicionando as escolhas para o campo 'id_lider'
        self.fields['id_lider'].queryset = Lider.objects.filter(ativo=True)

        # Adicionando as escolhas para o campo 'id_colaborador'
        self.fields['id_colaborador'].queryset = Colaborador.objects.filter(ativo=True)
 
