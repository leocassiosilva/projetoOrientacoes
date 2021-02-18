from django.urls import path, include
from .views import TarefaView, TarefaListView

urlpatterns = [
    path('cadastrar/<str:token>', TarefaView.as_view(), name='tarefa_cadastrar'),
    path('listar/<str:token>', TarefaListView.as_view(), name='tarefa_listar'),

]
