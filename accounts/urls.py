from django.contrib import admin
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import path, include

from .views import CriarUsuario, UserLogin, IndexView, PasswordResetView, PasswordReset, PasswordResetDone

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('cadastrar/', CriarUsuario.as_view(), name='cadastrar'),
    path('index', IndexView.as_view(), name='index'),
    # path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/', PasswordReset.as_view(), name='password-reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),

]
