from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUsuario


class CustomUsuarioCriarForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('username', 'first_name', 'last_name','matricula')
        labels = {'username': 'Username/E-mail'}




class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model: CustomUsuario
        fields = ('first_name', 'last_name')
