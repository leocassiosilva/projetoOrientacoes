from django import forms

from tarefa.models import Tarefa


class TarefaModelForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'data_realizacao', 'tipo_tarefa']
