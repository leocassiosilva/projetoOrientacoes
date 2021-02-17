from django.urls import path, include
from .views import TarefaView

urlpatterns = [
    path('cadastrar/<str:token>', TarefaView.as_view(), name='tarefa_cadastrar'),

]