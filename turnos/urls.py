from django.urls import path
from .views import listar_turnos

urlpatterns = [
    path('', listar_turnos, name='listar_turnos'),
]