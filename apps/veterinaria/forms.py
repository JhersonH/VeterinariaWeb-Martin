from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Mascota, Productos

class UserVeterinariaForm(UserCreationForm):
	def __init__(self,*args,**kwargs):
		super(UserVeterinariaForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({"placeholder":"juan.perez", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['first_name'].widget.attrs.update({"placeholder":"Juan", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['last_name'].widget.attrs.update({"placeholder":"Perez", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['email'].widget.attrs.update({"placeholder":"Juan@example.com", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['password1'].widget.attrs.update({"placeholder":"********************", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['password2'].widget.attrs.update({"placeholder":"********************", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		]
		labels = {
			"username":"Usuario",
			"first_name":"Nombres",
			"last_name":"Apellidos",
			"email":"Correo Electrónico",
			"password1":"Contraseña",
			"password2":"Repetir Contraseña",
		}

class MascotaVeterinariaForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(MascotaVeterinariaForm, self).__init__(*args, **kwargs)

		self.fields['nombre'].widget.attrs.update({"placeholder":"Nombre de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['especie'].widget.attrs.update({"placeholder":"Especie de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['raza'].widget.attrs.update({"placeholder":"Raza de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['edad'].widget.attrs.update({"placeholder":"Edad de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})

	class Meta:
		model = Mascota
		fields = [
			'nombre',
			'especie',
			'raza',
			'edad',
		]
		labels = {
			"nombre":"Nombre",
			"especie":"Especie",
			"raza":"Raza",
			"edad":"Edad",
		}

class ProductosForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProductosForm, self).__init__(*args, **kwargs)

		self.fields['descripcion'] = forms.ModelChoiceField(label="Nombre", queryset=Productos.objects.all().values_list('descripcion', flat=True))
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Nombre del producto","data-required":"true","data-error-message":"Valor Vacío","class":"form-control"})
		self.fields['precio'].widget.attrs.update({"placeholder": "Precio del producto", "data-required": "true", "disabled":"true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['stock'].widget.attrs.update({"placeholder": "Cantidad del producto", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})

	class Meta:
		model = Productos
		fields = [
            'descripcion',
            'precio',
            'stock',
        ]
		labels = {
            "descripcion": "Nombre",
            "precio": "Precio",
            "stock": "Cantidad",
        }