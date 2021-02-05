from django.urls import path, include
from .views import TrabalhoCreate, TrabalhoListView

urlpatterns = [
    path('cadastrar/', TrabalhoCreate.as_view(), name='cadastrar'),
    path('listar/', TrabalhoListView.as_view(), name='listar'),

]
