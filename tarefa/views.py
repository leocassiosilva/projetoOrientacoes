from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from tarefa.forms import TarefaModelForm
from tarefa.models import Tarefa


class TarefaView(CreateView):
    model = Tarefa
    form_class = TarefaModelForm
    template_name = 'tarefa/new-tarefa.html'
    success_message = "Senha alterada com sucesso!"

    def get_success_url(self):
        return reverse('index')
