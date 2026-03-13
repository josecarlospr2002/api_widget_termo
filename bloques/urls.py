from django.urls import path
from . import views

urlpatterns = [
    path('bloques_todos/', views.Bloques_All.as_view(), name='bloques_todos'),
]