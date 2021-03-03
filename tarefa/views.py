from django.shortcuts import render

from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from core.models import TipoTarefa
from tarefa.forms import TarefaModelForm
from tarefa.models import Tarefa
from trabalho.models import Trabalho


class TarefaView(CreateView):
    model = Tarefa
    form_class = TarefaModelForm
    template_name = 'tarefa/new-tarefa.html'
    success_message = "Tarefa cadastrada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_tarefas'] = list(TipoTarefa.objects.all())

        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        token = self.kwargs.get("token")
        context['trabalho'] = list(Trabalho.objects.filter(token=token))
        return context

    def get_queryset(self):
        token = self.kwargs.get("token")
        trabalho_id = list(trabalho.id for trabalho in Trabalho.objects.filter(token=token))
        tarefa = Tarefa.objects.filter(trabalho__in=trabalho_id)
        return tarefa


class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaModelForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        id_tarefa = self.kwargs.get("pk")
        tarefa_id = list(tarefa.trabalho.id for tarefa in Tarefa.objects.filter(id=id_tarefa))
        trabalho = Trabalho.objects.filter(id__in=tarefa_id)

        for member in trabalho.iterator():
            token = member.token

        return reverse('tarefa_listar', args=[token])


class TarefaDeleteView(DeleteView):
    model = Tarefa

    def get_success_url(self):
        id_tarefa = self.kwargs.get("pk")
        tarefa_id = list(tarefa.trabalho.id for tarefa in Tarefa.objects.filter(id=id_tarefa))
        trabalho = Trabalho.objects.filter(id__in=tarefa_id)

        for member in trabalho.iterator():
            token = member.token

        return reverse('tarefa_listar', args=[token])


class TarefaDetailView(DetailView):
    model = Tarefa
    fields = ['nome', 'descrição', 'data_realizacao', 'tipo_tarefa', 'trabalho']
