from django.urls import path, include
from .views import TrabalhoCreate, TrabalhoListView, TrabalhoUpdateView, TrabalhoDeleteView

urlpatterns = [
    path('cadastrar/', TrabalhoCreate.as_view(), name='trabalho_cadastrar'),
    path('listar/', TrabalhoListView.as_view(), name='trabalho_listar'),
    path('editar/<int:pk>', TrabalhoUpdateView.as_view(), name='trabalho_update'),
    path('deletar/<int:pk>/', TrabalhoDeleteView.as_view(), name='trabalho_delete'),

]
