from django.urls import path, include
from .views import GeneratePdf,write_pdf_view, GeneratePDF

urlpatterns = [
    path('trabalhos/', GeneratePdf.as_view(), name='gerar_relatorio'),

]
