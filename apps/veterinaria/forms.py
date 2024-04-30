from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Mascota, Productos, Ventas, Visita, TipoAnimales, Propietario, HistoriaClinica, Doctor

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

class DoctorForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(DoctorForm, self).__init__(*args, **kwargs)

		self.fields['anexo_usuarios'] = forms.ModelChoiceField(label="Usuario", queryset=User.objects.exclude(username='administrator'))
		self.fields['anexo_usuarios'].widget.attrs.update({"placeholder":"Doctor", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['nombre'].widget.attrs.update({"placeholder":"Nombre del Doctor", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['especialidad'].widget.attrs.update({"placeholder":"Dirección del Doctor", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['edad'].widget.attrs.update({"placeholder":"Celular del Doctor", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"DNI del Doctor", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})

	class Meta:
		model = Doctor
		fields = [
			'anexo_usuarios',
			'nombre',
			'especialidad',
			'edad',
			'dni',
		]
		labels = {
			"anexo_usuarios":"Usuario",
			"nombre":"Nombre",
			"especialidad":"Especialidad",
			"edad":"Edad",
			"dni":"DNI",
		}


class PropietarioForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(PropietarioForm, self).__init__(*args, **kwargs)

		self.fields['anexo_usuarios'] = forms.ModelChoiceField(label="Usuario", queryset=User.objects.exclude(username='administrator'))
		self.fields['anexo_usuarios'].widget.attrs.update({"placeholder":"Nombre de Propietario", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['nombre'].widget.attrs.update({"placeholder":"Nombre del Propietario", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['direccion'].widget.attrs.update({"placeholder":"Dirección del Propietario", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['celular'].widget.attrs.update({"placeholder":"Celular del Propietario", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['dni'].widget.attrs.update({"placeholder":"DNI del Propietario", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})

	class Meta:
		model = Propietario
		fields = [
			'anexo_usuarios',
			'nombre',
			'direccion',
			'celular',
			'dni',
		]
		labels = {
			"anexo_usuarios":"Usuario",
			"nombre":"Nombre",
			"direccion":"Dirección",
			"celular":"Celular",
			"dni":"DNI",
		}

class MascotaVeterinariaForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(MascotaVeterinariaForm, self).__init__(*args, **kwargs)

		SEXO_CHOICES = (
		('macho', 'Macho'),
        ('hembra', 'Hembra'),
		)

		self.fields['anexo_propietario'] = forms.ModelChoiceField(label="Propietario", queryset=Propietario.objects.all())
		self.fields['anexo_propietario'].widget.attrs.update({"placeholder":"Nombre de Propietario", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['nombre'].widget.attrs.update({"placeholder":"Nombre de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['especie'].widget.attrs.update({"placeholder":"Especie de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['raza'].widget.attrs.update({"placeholder":"Raza de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['edad'].widget = forms.NumberInput(attrs={"placeholder": "Edad de Mascota", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "step": "0.01", "type": "number"})
		self.fields['color'].widget.attrs.update({"placeholder":"Edad de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['peso'].widget.attrs.update({"placeholder":"Edad de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['sexo'] = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.Select(attrs={"placeholder": "Selecciona sexo","class": "form-control","data-required": "true","data-error-message": "Por favor, selecciona una opción"}))
		self.fields['fecha'].widget = forms.DateInput(attrs={"placeholder": "Fecha", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "type": "date"})
		self.fields['archivo'].widget = forms.ClearableFileInput(attrs={"placeholder": "Imagen del Producto", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "accept": "image/*"})

	class Meta:
		model = Mascota
		fields = [
			'anexo_propietario',
			'nombre',
			'especie',
			'raza',
			'edad',
			'color',
			'peso',
			'sexo',
			'fecha',
			'archivo',
		]
		labels = {
			"anexo_propietario":"Propietario",
			"nombre":"Mascota",
			"especie":"Especie",
			"raza":"Raza",
			"edad":"Edad",
			"color":"Color",
			"peso":"Peso",
			"sexo":"Sexo",
			"fecha":"Fecha de Nacimiento",
			"archivo":"Foto",
		}

class HistoriaClinicaForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(HistoriaClinicaForm, self).__init__(*args, **kwargs)

		self.fields['anexo_doctor'] = forms.ModelChoiceField(label="Doctor", queryset=Doctor.objects.all())
		self.fields['anexo_doctor'].widget.attrs.update({"placeholder":"Nombre del Doctor", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['anexo_mascota'] = forms.ModelChoiceField(label="Mascota", queryset=Mascota.objects.all())
		self.fields['anexo_mascota'].widget.attrs.update({"placeholder":"Nombre de Mascota", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['fecha'].widget = forms.DateInput(attrs={"placeholder": "Fecha", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "type": "date"})
		self.fields['motivo'].widget.attrs.update({"placeholder":"Motivo", "data-required":"true", "data-error-message":"Valor Vacío", "class":"form-control"})
		self.fields['diagnostico'].widget = forms.Textarea(attrs={"placeholder": "Diagnóstico de la Mascota", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "rows":3})
		self.fields['tratamiento'].widget = forms.Textarea(attrs={"placeholder": "Tratamiento de la Mascota", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "rows":3})
		self.fields['observaciones'].widget = forms.Textarea(attrs={"placeholder": "Observaciones adicionales", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "rows":3})

	class Meta:
		model = HistoriaClinica
		fields = [
			'anexo_doctor',
			'anexo_mascota',
			'fecha',
			'motivo',
			'diagnostico',
			'tratamiento',
			'observaciones',
		]
		labels = {
			"anexo_doctor":"Doctor",
			"anexo_mascota":"Mascota",
			"fecha":"Fecha",
			"motivo":"Motivo",
			"diagnostico":"Diagnóstico",
			"tratamiento":"Tratamiento",
			"observaciones":"Observaciones",
		}

class VentasForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VentasForm, self).__init__(*args, **kwargs)

		self.fields['anexo_producto'] = forms.ModelChoiceField(label="Nombre", queryset=Productos.objects.all())
		self.fields['anexo_producto'].widget.attrs.update({"placeholder":"Nombre del producto","data-required":"true","data-error-message":"Valor Vacío","class":"form-control"})
		self.fields['precio'].widget.attrs.update({"placeholder": "Precio del producto", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['cantidad'].widget.attrs.update({"placeholder": "Cantidad del producto", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['total'].widget.attrs.update({"placeholder": "Total del producto", "data-required": "true", "disabled": "true", "data-error-message": "Valor Vacío", "class": "form-control"})

	class Meta:
		model = Ventas
		fields = [
            'anexo_producto',
            'precio',
            'cantidad',
            'total',
        ]
		labels = {
            "anexo_producto": "Nombre",
            "precio": "Precio",
            "cantidad": "Cantidad",
            "total": "Total: ",
        }

class ReservacionesForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ReservacionesForm, self).__init__(*args, **kwargs)

		self.fields['mascota'].widget.attrs.update({"placeholder":"Nombre de la Mascota","data-required":"true","data-error-message":"Valor Vacío","class":"form-control"})
		self.fields['tipo'] = forms.ModelChoiceField(label="Tipo de Animal", queryset=TipoAnimales.objects.all())
		self.fields['tipo'].widget.attrs.update({"placeholder": "Tipo de Animal", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['fecha'].widget = forms.DateInput(attrs={"placeholder": "Fecha de Reservación", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "type": "date"})
		self.fields['motivo'].widget.attrs.update({"placeholder": "Motivo de la Visita", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['nota'].widget = forms.Textarea(attrs={"placeholder": "Breve detalle adicional", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "rows":3})

	class Meta:
		model = Visita
		fields = [
            'mascota',
            'tipo',
            'fecha',
            'motivo',
            'nota',
        ]
		labels = {
            "mascota": "Nombre",
            "tipo": "Tipo",
            "fecha": "Fecha",
            "motivo": "Motivo",
            "nota": "Descripción",
        }

class ReservacionesEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ReservacionesEditForm, self).__init__(*args, **kwargs)

		self.fields['mascota'].widget.attrs.update({"placeholder":"Nombre de la Mascota","data-required":"true","data-error-message":"Valor Vacío","class":"form-control"})
		self.fields['tipo'].widget.attrs.update({"placeholder": "Tipo de Animal", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['fecha'].widget = forms.DateInput(attrs={"placeholder": "Fecha de Reservación", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "type": "date"})
		self.fields['motivo'].widget.attrs.update({"placeholder": "Motivo de la Visita", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['nota'].widget = forms.Textarea(attrs={"placeholder": "Breve detalle adicional", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "rows":3})

	class Meta:
		model = Visita
		fields = [
            'mascota',
            'tipo',
            'fecha',
            'motivo',
            'nota',
        ]
		labels = {
            "mascota": "Nombre",
            "tipo": "Tipo",
            "fecha": "Fecha",
            "motivo": "Motivo",
            "nota": "Descripción",
        }

class RegistrarProductosForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegistrarProductosForm, self).__init__(*args, **kwargs)

		CATEGORIAS_PRODUCTOS = (
			('alimentacion', 'Alimentación'),
			('higiene', 'Higiene y cuidado'),
			('salud', 'Salud y medicamentos'),
			('accesorios', 'Accesorios y juguetes'),
			('equipamiento', 'Equipamiento veterinario'),
		)

		TIPOS_PRODUCTOS = (
			('alimentacion', 'Alimento seco para perros'),
			('alimentacion', 'Alimento húmedo para gatos'),
			('higiene', 'Champú para perros y gatos'),
			('higiene', 'Cepillo dental para mascotas'),
			('salud', 'Antibiótico para gatos'),
			('salud', 'Antipulgas y garrapatas para perros'),
			('accesorios', 'Collar antiparasitario para perros'),
			('accesorios', 'Juguete interactivo para gatos'),
			('equipamiento', 'Arnés para paseo de mascotas'),
			('equipamiento', 'Jaula de transporte para roedores'),
		)

		self.fields['categoria'] = forms.ChoiceField(choices=CATEGORIAS_PRODUCTOS, widget=forms.Select(attrs={"placeholder": "Categoria de Producto","class": "form-control","data-required": "true","data-error-message": "Por favor, selecciona una opción"}))
		self.fields['tipo_producto'] = forms.ChoiceField(choices=TIPOS_PRODUCTOS, widget=forms.Select(attrs={"placeholder": "Tipo de Producto","class": "form-control","data-required": "true","data-error-message": "Por favor, selecciona una opción"}))
		self.fields['descripcion'].widget.attrs.update({"placeholder":"Nombre del Producto","data-required":"true","data-error-message":"Valor Vacío","class":"form-control"})
		self.fields['stock'].widget.attrs.update({"placeholder": "Cantidad registrada", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control"})
		self.fields['fecha_ingreso'].widget = forms.DateInput(attrs={"placeholder": "Fecha", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "type": "date"})
		self.fields['fecha_vencimiento'].widget = forms.DateInput(attrs={"placeholder": "Fecha", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "type": "date"})
		self.fields['precio'].widget = forms.NumberInput(attrs={"placeholder": "Precio del Producto", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "step": "0.01", "type": "number"})
		self.fields['archivo'].widget = forms.ClearableFileInput(attrs={"placeholder": "Imagen del Producto", "data-required": "true", "data-error-message": "Valor Vacío", "class": "form-control", "accept": "image/*"})

	class Meta:
		model = Productos
		fields = [
            'categoria',
            'tipo_producto',
            'descripcion',
            'stock',
            'fecha_ingreso',
            'fecha_vencimiento',
            'precio',
            'archivo',
        ]
		labels = {
            "categoria": "Categoria del Producto",
            "tipo_producto": "Tipo de Producto",
            "descripcion": "Nombre",
            "stock": "Cantidad",
            "fecha_ingreso": "Fecha de Ingreso",
            "fecha_vencimiento": "Fecha de Vencimiento",
            "precio": "Precio",
            "archivo": "Imagen",
        }