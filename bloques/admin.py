from django.contrib import admin
from .models import Bloque1, Bloque2, Bloque3

@admin.register(Bloque1)
class Bloque1Admin(admin.ModelAdmin):
    list_display = (
        'id',
        'presion',
        'temperatura',
        'calor',
        'potencia',
        'fecha'
    )
    ordering = ('-id',)

    # Solo para lectura: desactivar agregar, modificar y eliminar
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Bloque2)
class Bloque2Admin(admin.ModelAdmin):
    list_display = (
        'id',
        'presion',
        'temperatura',
        'calor',
        'potencia',
        'fecha'
    )
    ordering = ('-id',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Bloque3)
class Bloque3Admin(admin.ModelAdmin):
    list_display = (
        'id',
        'presion',
        'temperatura',
        'calor',
        'potencia',
        'fecha'
    )
    ordering = ('-id',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
