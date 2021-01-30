from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import ModelFormMixin, FormView

from accounts.forms import CustomUsuarioCriarForm
from accounts.models import CustomUsuario
from django.contrib.auth.views import LoginView, PasswordResetView


class CriarUsuario(CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCriarForm
    template_name = 'accounts/new-user.html'
    success_url = '/accounts/login'
    success_message = 'Bem vindo! Faça login para começar '


class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    success_url = '/accounts/index'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'


class IndexView(TemplateView):
    template_name = 'accounts/index.html'
