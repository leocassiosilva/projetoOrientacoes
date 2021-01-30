from django.contrib import admin
from django.urls import path, include

from accounts.views import CriarUsuario, UserLogin, IndexView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('cadastrar/', CriarUsuario.as_view(), name='cadastrar'),
    path('index', IndexView.as_view(), name='index'),
]
