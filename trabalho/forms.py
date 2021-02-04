from django import forms

from trabalho.models import Trabalho


class TrabalhoModelForm(forms.ModelForm):
    class Meta:
        model = Trabalho
        fields = ['nome', 'descricao', 'data_inicio', 'data_entrega', 'area', 'tipo']
