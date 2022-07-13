import sys
from django.contrib import admin
from .models import Categoria, Nave, Inventario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Nave)
admin.site.register(Inventario)