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
    path('dashboard/editar_usuario/<int:id>', views.editarUsuarios, name='editarUsuarios'),
    path('dashboard/eliminar_usuario/<int:id>', views.eliminarUsuarios, name='eliminarUsuarios'),
    path('dashboard/vender_productos', views.venderProductos, name='venderProductos'),
    path('dashboard/registrar_productos', views.registrarProductos, name='registrarProductos'),
    path('dashboard/visualizar_productos', views.visualizarProductos, name='visualizarProductos'),
    path('dashboard/editar_producto/<int:id>', views.editarProductos, name='editarProductos'),
    path('dashboard/eliminar_producto/<int:id>', views.eliminarProductos, name='eliminarProductos'),
    path('dashboard/reporte_productos', views.reporteProductos, name='reporteProductos'),
    path('dashboard/visualizar_ventas', views.visualizarVentas, name='visualizarVentas'),
    path('dashboard/editar_venta/<int:id>', views.editarVentas, name='editarVentas'),
    path('dashboard/eliminar_venta/<int:id>', views.eliminarVentas, name='eliminarVentas'),
    path('dashboard/reporte_ventas', views.reporteVentas, name='reporteVentas'),
    path('dashboard/visualizar_citas', views.visualizarCitas, name='visualizarCitas'),
    path('dashboard/editar_cita/<int:id>', views.editarCitas, name='editarCitas'),
    path('dashboard/eliminar_cita/<int:id>', views.eliminarCitas, name='eliminarCitas'),
    path('dashboard/reporte_citas', views.reporteCitas, name='reporteCitas'),
    path('dashboard/registrar_doctor', views.registrarDoctor, name='registrarDoctor'),
    path('dashboard/registrar_propietario', views.registrarPropietario, name='registrarPropietario'),
    path('dashboard/registrar_mascota', views.registrarMascota, name='registrarMascota'),
    path('dashboard/registrar_historial', views.registrarHistorial, name='registrarHistorial'),
    path('dashboard/visualizar_historial', views.visualizarHistorial, name='visualizarHistorial'),
    path('dashboard/editar_historial/<int:id>', views.editarHistorial, name='editarhistorial'),
    path('dashboard/eliminar_historial/<int:id>', views.eliminarHistorial, name='eliminarhistorial'),
    path('dashboard/reporte_general', views.reporteGeneral, name='reporteGeneral'),
    path('salir/', views.logoutWeb, name='logout'),

    path('users/chart/', views.users_chart, name='users_chart'),
    path('products/chart/', views.products_chart, name='products_chart'),
    path('sales/chart/', views.sales_chart, name='sales_chart'),
    path('dates/chart/', views.dates_chart, name='dates_chart'),
    path('record/chart/', views.record_chart, name='record_chart'),

    #AJAX
    path('ajax/load-precios/<int:id>/', views.load_precios, name='ajax_load_precios'),
]