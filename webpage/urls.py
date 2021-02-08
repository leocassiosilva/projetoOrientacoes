from django.urls import path, include
from .views import IndexView, HomeView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('', HomeView.as_view(), name='home'),
    path('/', HomeView.as_view(), name='home'),
]
