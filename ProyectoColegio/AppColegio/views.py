from django.http import HttpResponse
from django.shortcuts import render
from AppColegio.models import *
from AppColegio.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):

    return render(request, 'AppColegio/inicio.html')
def mensajeclie(request):

    return render(request, 'AppColegio/mensajeuser.html')
def comentarios(request):
    servicios = Opiniones.objects.all()
    return render(request, 'AppColegio/Opiniones/listaopiniones.html',{'resultados':servicios})
@login_required
def entregables(request):
    servicios = Entregables.objects.all()
    return render(request, 'AppColegio/Entregables/listaEntregables.html',{'resultados':servicios})
def about(request):

    return render(request, 'AppColegio/about.html')

def servicios(request):

    servicios = Servicios.objects.all()


    return render(request, "AppColegio/Servicios/listaServicios.html",{'resultados':servicios})

def empleados(request):

    empleados = Empleados.objects.all()

    return render(request, "AppColegio/Empleados/listaEmpleados.html",{'resultados':empleados})


@login_required
def clientes(request):

    clientes = Cliente.objects.all()

    return render(request, "AppColegio/Cliente/listaCliente.html",{'resultados':clientes})


@login_required
def editarServicios(request, servicio_nombre):

    servi = Servicios.objects.get(servicio=servicio_nombre)

    if request.method == "POST":

        miFormulario = ServiciosFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            servi.servicio = informacion['servicio']
            servi.descripcion = informacion['descripcion']
            servi.precio = informacion['precio']
            servi.imagen = informacion['imagen']

            servi.save()

            return render(request, "AppColegio/inicio.html")

    else:

        miFormulario= ServiciosFormulario(initial={'servicio':servi.servicio, 'descripcion':servi.descripcion,
        'precio':servi.precio,'imagen': servi.imagen})

    return render(request, "AppColegio/Servicios/editarServicios.html",{'miFormulario':miFormulario, 'resultado':servicio_nombre})

@login_required
def editarEmpleados(request, empleado_dni):

    emple = Empleados.objects.get(dni=empleado_dni)

    if request.method == "POST":

        miFormulario = EmpleadoFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            emple.dni = informacion['dni']
            emple.nombre = informacion['nombre']
            emple.apellido = informacion['apellido']
            emple.email = informacion['email']
            emple.categoria = informacion['categoria']
            emple.imagen = informacion['imagen']
        
            emple.save()

            return render(request, "AppColegio/inicio.html")

    else:

        miFormulario= EmpleadoFormulario(initial={'dni':emple.dni,'nombre':emple.nombre, 'apellido':emple.apellido,
        'email':emple.email,'categoria': emple.categoria, 'imagen': emple.imagen})

    return render(request, "AppColegio/Empleados/editarEmpleados.html",{'miFormulario':miFormulario, 'resultado':empleado_dni})
@login_required
def editarClientes(request, cliente_dni):

    clien = Cliente.objects.get(dni=cliente_dni)

    if request.method == "POST":

        miFormulario = ClienteFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            clien.dni = informacion['dni']
            clien.nombre = informacion['nombre']
            clien.apellido = informacion['apellido']
            clien.email = informacion['email']
        
            clien.save()

           # return render(request, "AppColegio/Cliente/listaCliente.html")
            return HttpResponse(clientes(request))
            

    else:

        miFormulario= ClienteFormulario(initial={'dni':clien.dni,'nombre':clien.nombre, 'apellido':clien.apellido,
        'email':clien.email})

    return render(request, "AppColegio/Cliente/editarCliente.html",{'miFormulario':miFormulario, 'resultado':cliente_dni})

@login_required

def editarEntregables(request, entregable_id):

    entre = Entregables.objects.get(id=entregable_id)

    if request.method == "POST":

        miFormulario = EntregableFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            entre.nombreservicio = informacion['nombreservicio']
            entre.cliente = informacion['cliente']
            entre.fecha_de_entrega = informacion['fecha_de_entrega']
            entre.entregado = informacion['entregado']
            entre.imagen= informacion['imagen']
            entre.save()

           # return render(request, "AppColegio/Cliente/listaCliente.html")
            return HttpResponse(entregables(request))
            

    else:

        miFormulario= EntregableFormulario(initial={'nombreservicio':entre.nombreservicio,'cliente':entre.cliente, 'fecha_de_entrega':entre.fecha_de_entrega,
        'entregado':entre.entregado,'imagen':entre.imagen})

    return render(request, "AppColegio/Entregables/editarEntregables.html",{'miFormulario':miFormulario, 'resultado':entregable_id})



@login_required
def AgregarServicios(request):

    if request.method == 'POST':

        miFormulario=ServiciosFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data



            servicio = Servicios(servicio=informacion['servicio'], descripcion=informacion['descripcion'],
             precio=informacion['precio'],imagen=informacion['imagen'])

            servicio.save()

            return render(request, 'AppColegio/inicio.html')
    else:

        miFormulario=ServiciosFormulario()

    return render(request, 'AppColegio/Servicios/añadirServicios.html', {'form':miFormulario})
@login_required
def AgregarEmpleados(request):

    if request.method == 'POST':

        miFormulario=EmpleadoFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data



            servicio = Empleados(dni=informacion['dni'], nombre=informacion['nombre'],
             apellido=informacion['apellido'],email=informacion['email'],categoria=informacion['categoria'],imagen=informacion['imagen'])

            servicio.save()

            return render(request, 'AppColegio/inicio.html')
    else:

        miFormulario=EmpleadoFormulario()

    return render(request, 'AppColegio/Empleados/añadirEmpleados.html', {'form':miFormulario})
@login_required
def AñadirClientes(request):

    if request.method == 'POST':

        miFormulario=ClienteFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data



            cliente = Cliente(dni=informacion['dni'], nombre=informacion['nombre'],
             apellido=informacion['apellido'],email=informacion['email'])

            cliente.save()

            return HttpResponse(clientes(request))
    else:

        miFormulario=ClienteFormulario()

    return render(request, 'AppColegio/Cliente/añadirCliente.html', {'form':miFormulario})

@login_required
def AñadirOpiniones(request):

    if request.method == 'POST':

        miFormulario=OpinionesFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            opinion = Opiniones(autor=request.user,opinion=informacion['opinion'], calificacion=informacion['calificacion'])   

            opinion.save()

            return HttpResponse(comentarios(request))
    else:

        miFormulario=OpinionesFormulario()

    return render(request, 'AppColegio/Opiniones/añadiropiniones.html', {'form':miFormulario})

def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"

        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada
            
            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados
            
            
            if user:    #si ha encontrado un usuario con eso datos

                login(request, user)   #hacemos login

                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "AppColegio/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   #si el formulario no es valido (no encuentra usuario)

            #mostramos la página de inicio junto a un mensaje de error.
    
            return render(request, "AppColegio/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "AppColegio/Autentificar/login.html", {'form':form})    #vincular la vista con la plantilla de html
@login_required
def añadirentregables(request):

    if request.method == 'POST':

        miFormulario=EntregableFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data



            cliente = Entregables(nombreservicio=informacion['nombreservicio'], cliente=informacion['cliente'],
             fecha_de_entrega=informacion['fecha_de_entrega'],entregado=informacion['entregado'],imagen=informacion['imagen'])

            cliente.save()

            return HttpResponse(entregables(request))
    else:

        miFormulario=EntregableFormulario()
    return render(request, 'AppColegio/Entregables/añadirEntregables.html', {'form':miFormulario})
def register(request):

    if request.method == 'POST':    #cuando le haga click al botón

        form = RegistroFormulario(request.POST)   #leer los datos   llenados en el formulario

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppColegio/Autentificar/login.html")
    
    else:

        form = RegistroFormulario()   #formulario de django que nos permite crear usuarios.
    
    
    return render(request, "AppColegio/Autentificar/registro.html", {'form':form})
@login_required
def eliminarEmpleado(request, empleado_dni):
 
    emple = Empleados.objects.get(dni=empleado_dni)
    emple.delete()
 
    # vuelvo al menú
    emplead = Empleados.objects.all()  # trae todos los empleados
 
    contexto = {"empleados": emplead}
    #return render(request, "AppColegio/Empleados/listaEmpleados.html", contexto)
    return HttpResponse(empleados(request))
@login_required
def eliminarEntregables(request, entregable_id):
 
    entre = Entregables.objects.get(id=entregable_id)
    entre.delete()
 
    # vuelvo al menú
    entrega = Entregables.objects.all()  # trae todos los empleados
 
    contexto = {"entregables": entrega}
    #return render(request, "AppColegio/Entregables/listaEntregables.html", contexto)
    return HttpResponse(entregables(request))

@login_required
def eliminarClientes(request, cliente_dni):
 
    clie = Cliente.objects.get(dni=cliente_dni)
    clie.delete()
 
    # vuelvo al menú
    client = Cliente.objects.all()  # trae todos los empleados
 
    contexto = {"clientes": client}
    #return render(request, "AppColegio/Cliente/listaCliente.html", contexto)
    return HttpResponse(clientes(request))
@login_required
def busquedaclientes(request):
    if request.GET["dni"]:
       dni= request.GET['dni']
       clientes= Cliente.objects.filter(dni__icontains=dni)
    #return HttpResponse(respuesta)
       return render(request,"AppColegio/Busquedas/resultclientes.html",{"clientes":clientes,"dni":dni})
    else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)
@login_required
def busquedaclientes(request):
    if request.GET["dni"]:
       dni= request.GET['dni']
       clientes= Cliente.objects.filter(dni__icontains=dni)
    #return HttpResponse(respuesta)
       return render(request,"AppColegio/Busquedas/resultclientes.html",{"clientes":clientes,"dni":dni})
    else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)
@login_required
def busquedaentregables(request):
    if request.GET["fecha_de_entrega"]:
       fecha_de_entrega= request.GET['fecha_de_entrega']
       entregas= Entregables.objects.filter(fecha_de_entrega__icontains=fecha_de_entrega)
    #return HttpResponse(respuesta)
       return render(request,"AppColegio/Busquedas/resultentregables.html",{"entregas":entregas,"fecha_de_entrega":fecha_de_entrega})
    else:
       respuesta="No enviaste los datos"
       return HttpResponse(respuesta)