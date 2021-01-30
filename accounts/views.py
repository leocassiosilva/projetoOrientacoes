from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin

from accounts.forms import CustomUsuarioCriarForm
from accounts.models import CustomUsuario


class CriarUsuario(CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCriarForm
    template_name = 'accounts/new-user.html'
    success_url = '/accounts/login'
    success_message = 'Bem vindo! Faça login para começar '
