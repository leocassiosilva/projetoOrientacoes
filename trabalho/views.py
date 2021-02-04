from django.shortcuts import render
from django.views.generic import CreateView

from trabalho.forms import TrabalhoModelForm
from trabalho.models import Trabalho


class TrabalhoCreate(CreateView):
    model = Trabalho
    form_class = TrabalhoModelForm
    template_name = 'trabalho/new-trabalho.html'
