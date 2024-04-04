from django.contrib import admin
from app_sage.models import Extrafields


# Definición de la clase ExtraFieldsAdmin que personaliza la visualización en el panel de administración.
class ExtraFieldsAdmin(admin.ModelAdmin):
    # Especifica los campos a mostrar en la lista de registros.
    list_display = ('user',)

# Register your models here.
admin.site.register(Extrafields, ExtraFieldsAdmin)