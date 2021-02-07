from django.contrib import admin
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import path, include

from .views import CriarUsuario, UserLogin, IndexView, PasswordResetView, PasswordReset, PasswordResetDone, \
    PasswordResetConfirm, PasswordResetCompleteView, LogoutView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('cadastrar/', CriarUsuario.as_view(), name='cadastrar'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('index', IndexView.as_view(), name='index'),
    # path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/', PasswordReset.as_view(), name='password-reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_complete'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),

]
