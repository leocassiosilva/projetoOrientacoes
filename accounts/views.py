from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, TemplateView, RedirectView
from django.views.generic.edit import ModelFormMixin, FormView, UpdateView

from accounts.forms import CustomUsuarioCriarForm
from accounts.models import CustomUsuario
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView


class CriarUsuario(SuccessMessageMixin, CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCriarForm
    template_name = 'accounts/new-user.html'
    success_url = '/accounts/login'
    success_message = 'Bem vindo! Faça login para começar '




class UpdateUsuario(SuccessMessageMixin, UpdateView):
    model = CustomUsuario
    fields = ('username', 'first_name', 'last_name', 'matricula')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('index')


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_url = 'webpage/index'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'


class PasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Senha Alterada com sucesso!'
    template_name = 'accounts/login.html'


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = 'index'
    success_message = "Senha alterada com sucesso!"


class LogoutView(RedirectView):
    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(self, request, *args, **kwargs)
