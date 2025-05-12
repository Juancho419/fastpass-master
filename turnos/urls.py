from django.urls import path
from .views import listar_turnos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', listar_turnos, name='listar_turnos'),
    path('login/', auth_views.LoginView.as_view(template_name='turnos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]