from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppColegio.models import *
class ServiciosFormulario(forms.ModelForm):
   class Meta:

        model = Servicios
        fields = ['servicio', 'descripcion', 'precio','imagen']
class EmpleadoFormulario(forms.ModelForm):
   class Meta:

        model = Empleados
        fields = ['dni', 'nombre', 'apellido','email','categoria','imagen']
class ClienteFormulario(forms.ModelForm):
   class Meta:

        model = Cliente
        fields = ['dni', 'nombre', 'apellido','email']

class OpinionesFormulario(forms.ModelForm):
    class Meta:
        model = Opiniones
        fields= ['opinion','calificacion']

class EntregableFormulario(forms.ModelForm):
    class Meta:
        model = Entregables
        fields= ['nombreservicio','cliente','fecha_de_entrega','entregado','imagen']
class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

