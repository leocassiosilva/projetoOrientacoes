from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView

from tarefa.forms import TarefaModelForm
from tarefa.models import Tarefa
from trabalho.models import Trabalho


class TarefaView(CreateView):
    model = Tarefa
    form_class = TarefaModelForm
    template_name = 'tarefa/new-tarefa.html'
    success_message = "Tarefa cadastrada com sucesso!"

    def form_valid(self, form):
        tarefa = form.save(commit=False)
        token = self.kwargs.get("token")
        trabalho_id = Trabalho.objects.get(token=token)
        tarefa.trabalho = trabalho_id
        tarefa.save()
        return super(TarefaView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')


class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefa/tarefa_listar.html'

    def get_queryset(self):
        token = self.kwargs.get("token")
        trabalho_id = list(trabalho.id for trabalho in Trabalho.objects.filter(token=token))
        tarefa = Tarefa.objects.filter(trabalho__in=trabalho_id)
        return tarefa
