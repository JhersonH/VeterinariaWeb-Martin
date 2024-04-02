from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_usuario/', views.nuevoUsuario, name='registrarUsuario'),
    path('productos/', views.productos, name='productos'),
    path('historial_clinico/', views.historialClinico, name='historialClinico'),
    path('reserva_médica/', views.reservaMedica, name='reservaMedica'),
    path('salir/', views.logoutWeb, name='logout'),
]