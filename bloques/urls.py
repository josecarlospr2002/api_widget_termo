from django.urls import path
from . import views

urlpatterns = [
    path('ultimos_registros/', views.ultimos_registros, name='ultimos_registros'),
]