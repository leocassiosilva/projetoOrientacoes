from zipfile import Path

from django.contrib import admin

# Register your models here.
from .models import Tipo, TipoTarefa, Area

admin.site.register(Tipo)
admin.site.register(TipoTarefa)
admin.site.register(Area)
