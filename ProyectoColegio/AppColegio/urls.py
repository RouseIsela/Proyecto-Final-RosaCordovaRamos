from django.urls import path
from AppColegio import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path('mensaje', views.mensajeclie, name='Mensaje'),
    path('about', views.about, name='About'),
    path('servicios', views.servicios, name='servicios'),
    path("editarServicios/<servicio_nombre>", views.editarServicios, name="EditarServicios"),
    path('agregarServicios',views.AgregarServicios, name='AgregarServicios'),
    path('empleados',views.empleados, name='Empleados'),
    path("editarEmpleados/<empleado_dni>", views.editarEmpleados, name="EditarEmpleados"),
    path('agregarEmpleados',views.AgregarEmpleados, name='AgregarEmpleados'),
    path('clientes', views.clientes, name='Clientes'),
    path('editarCliente/<cliente_dni>', views.editarClientes, name='EditarCliente'),
    path('añadirCliente', views.AñadirClientes, name='AñadirClientes'),
    path('login', views.login_request, name='Login'),
    path('agregarOpiniones', views.AñadirOpiniones, name='AgregarOpiniones'),
    path('comentarios', views.comentarios, name='comentarios'),
    path('entregables', views.entregables, name='Entregables'),
    path('editarentregables/<entregable_id>', views.editarEntregables, name='Editarentregables'),
    path('agregarentregables', views.añadirentregables, name='AgregarEntregables'),
    path('registrate', views.register, name='Registrate'),
    path('logout', LogoutView.as_view(template_name='AppColegio/Autentificar/logout.html'), name='Logout'),
    path('eliminarCliente/<cliente_dni>', views.eliminarClientes, name='EliminarCliente'),
    path('eliminarEntregables/<entregable_id>', views.eliminarEntregables, name='EliminarEntregables'),
    path('eliminarEmpleados/<empleado_dni>', views.eliminarEmpleado, name='EliminarEmpleados'),
    path("busquedaClientes/",views.busquedaclientes),
    path("busquedaEntregables/",views.busquedaentregables),
]

