from django.urls import path, include
from .views import TarefaView, TarefaListView, TarefaUpdateView

urlpatterns = [
    path('cadastrar/<str:token>', TarefaView.as_view(), name='tarefa_cadastrar'),
    path('listar/<str:token>', TarefaListView.as_view(), name='tarefa_listar'),
    path('editar/<int:pk>', TarefaUpdateView.as_view(), name='tarefa_update'),
]
