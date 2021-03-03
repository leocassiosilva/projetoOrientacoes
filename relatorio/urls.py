from django.urls import path, include
from .views import GeneratePdf,write_pdf_view

urlpatterns = [
    path('gerar/', write_pdf_view, name='gerar_relatorio'),

]
