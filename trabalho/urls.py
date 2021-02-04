from django.urls import path, include
from .views import TrabalhoCreate

urlpatterns = [
    path('cadastrar/', TrabalhoCreate.as_view(), name='cadastrar'),
]
