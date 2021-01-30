from django.contrib import admin
from django.urls import path, include

from accounts.views import CriarUsuario

urlpatterns = [
    # path('login/', Logar, name='login'),
    path('cadastrar/', CriarUsuario.as_view(), name='cadastrar'),
    # path('index', IndexView.as_view(), name='index'),
]
