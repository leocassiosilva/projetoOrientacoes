from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from trabalho.forms import TrabalhoModelForm
from trabalho.models import Trabalho


class TrabalhoCreate(CreateView):
    model = Trabalho
    form_class = TrabalhoModelForm
    template_name = 'trabalho/new-trabalho.html'

    def form_valid(self, form):
        trabalho = form.save(commit=False)
        trabalho.id_usuario = self.request.user
        trabalho.save()
        return super(TrabalhoCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')
