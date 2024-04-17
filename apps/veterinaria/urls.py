from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_usuario/', views.nuevoUsuario, name='registrarUsuario'),
    path('productos/', views.productos, name='productos'),
    path('historial_clinico/', views.historialClinico, name='historialClinico'),
    path('reserva_médica/', views.reservaMedica, name='reservaMedica'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/visualizar_usuarios', views.visualizarUsuarios, name='visualizarUsuarios'),
    path('dashboard/vender_productos', views.venderProductos, name='venderProductos'),
    path('dashboard/visualizar_productos', views.visualizarProductos, name='visualizarProductos'),
    path('dashboard/visualizar_ventas', views.visualizarVentas, name='visualizarVentas'),
    path('dashboard/visualizar_citas', views.visualizarCitas, name='visualizarCitas'),
    path('dashboard/registrar_historial', views.registrarHistorial, name='registrarHistorial'),
    path('dashboard/visualizar_historial', views.visualizarHistorial, name='visualizarHistorial'),
    path('salir/', views.logoutWeb, name='logout'),
]