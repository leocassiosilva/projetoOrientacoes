from django.urls import path, include
from .views import TrabalhoCreate, TrabalhoListView, TrabalhoUpdateView

urlpatterns = [
    path('cadastrar/', TrabalhoCreate.as_view(), name='cadastrar'),
    path('listar/', TrabalhoListView.as_view(), name='listar'),
    path('editar/<int:pk>', TrabalhoUpdateView.as_view(), name='trabalho_update'),

]
