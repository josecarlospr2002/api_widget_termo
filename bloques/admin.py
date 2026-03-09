from django.contrib import admin
from .models import Bloque1, Bloque2, Bloque3

@admin.register(Bloque1)
class Bloque1Admin(admin.ModelAdmin):
    list_display = ('id', 'presion', 'temperatura', 'calor', 'potencia', 'potencia_calor', 'fecha')
    ordering = ('-id',)

@admin.register(Bloque2)
class Bloque2Admin(admin.ModelAdmin):
    list_display = ('id', 'presion', 'temperatura', 'calor', 'potencia', 'potencia_calor', 'fecha')
    ordering = ('-id',)

@admin.register(Bloque3)
class Bloque3Admin(admin.ModelAdmin):
    list_display = ('id', 'presion', 'temperatura', 'calor', 'potencia', 'potencia_calor', 'fecha')
    ordering = ('-id',)