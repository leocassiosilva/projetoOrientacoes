from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUsuario


class CustomUsuarioCriarForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('username', 'first_name', 'last_name','matricula')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"]) #recuperar os dados para criptografar a senha
        user.email = self.cleaned_data["username"] #recuperar os dados referente ao e-mail

        if commit:
            user.save()

        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model: CustomUsuario
        fields = ('first_name', 'last_name')
