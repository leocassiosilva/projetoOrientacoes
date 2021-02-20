from django.urls import path, include
from .views import TarefaView, TarefaListView, TarefaUpdateView, TarefaDeleteView, TarefaDetailView

urlpatterns = [
    path('cadastrar/<str:token>', TarefaView.as_view(), name='tarefa_cadastrar'),
    path('listar/<str:token>', TarefaListView.as_view(), name='tarefa_listar'),
    path('editar/<int:pk>', TarefaUpdateView.as_view(), name='tarefa_update'),
    path('deletar/<int:pk>/', TarefaDeleteView.as_view(), name='tarefa_delete'),
    path('detalhe/<int:pk>/', TarefaDetailView.as_view(), name='tarefa_detalhe'),

]
