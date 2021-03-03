from django.urls import path, include
from .views import GeneratePdf,write_pdf_view, GeneratePDF

urlpatterns = [
    path('gerar/', GeneratePDF.as_view(), name='gerar_relatorio'),

]
