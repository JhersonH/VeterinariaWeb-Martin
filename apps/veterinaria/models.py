from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
	descripcion = models.CharField("Tipo de Usuario", max_length=50, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTipoUsuario")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTipoUsuario", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Tipo Usuario'
		verbose_name_plural = 'Tipo de Usuarios'

	def __str__(self):
		return "%s" % (self.descripcion)

class Personal(models.Model):
	anexo_usuarios = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuariosPersonal", null=True, blank=True)
	nombres = models.CharField("Nombres Completos", max_length=100, blank=True, null=True)
	apellidos = models.CharField("Apellidos Completos", max_length=100, blank=True, null=True)
	anexo_tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, related_name="AnexoUsuariosPersonal", null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPersonal")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPersonal", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Personal Veterinaria'
		verbose_name_plural = 'Personales Veterinaria'

	def __str__(self):
		return "%s - %s" % (self.anexo_usuarios.first_name, self.anexo_tipo)

class Propietario(models.Model):
	anexo_usuarios = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name="AnexoUsuariosPropietario", null=True, blank=True)
	correo = models.CharField("Correo Electrónico", max_length=100, blank=True, null=True)
	direccion = models.CharField("Nombre de avenida", max_length=100, blank=True, null=True)
	celular = models.IntegerField(blank=True, null=True)
	dni = models.IntegerField(blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionPropietario")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModPropietario", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Propietario'
		verbose_name_plural = 'Propietarios'

	def __str__(self):
		return "%s - %s" % (self.nombre, self.especie)

class Mascota(models.Model):
	anexo_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="AnexoPropietario", null=True, blank=True)
	nombre = models.CharField("Nombre de Mascota", max_length=100, blank=True, null=True)
	especie = models.CharField("Especie de Mascota", max_length=100, blank=True, null=True)
	raza = models.CharField("Raza de Mascota", max_length=100, blank=True, null=True)
	edad = models.IntegerField(blank=True, null=True)
	propietarios = models.ManyToManyField(Propietario)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMascota")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMascota", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Mascota'
		verbose_name_plural = 'Mascotas'

	def __str__(self):
		return "%s - %s" % (self.nombre, self.especie)
	
class Visita(models.Model):
	anexo_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="AnexoVisitaMascota", null=True, blank=True)
	fecha = models.DateField()
	motivo = models.CharField("Motivo de Visita", max_length=150, blank=True, null=True)
	nota = models.CharField("Notas adicionales", max_length=50, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionVisita")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModVisita", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Visita'
		verbose_name_plural = 'Visitas'

	def __str__(self):
		return "%s - %s" % (self.anexo_mascota.nombre, self.motivo)
	
class Vacuna(models.Model):
	anexo_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="AnexoVacunaMascota", null=True, blank=True)
	nombre = models.CharField("Nombre de Vacuna", max_length=100, blank=True, null=True)
	fecha_aplicacion = models.DateField()
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionVacuna")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModVacuna", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Vacuna'
		verbose_name_plural = 'Vacunas'

	def __str__(self):
		return "%s - %s" % (self.anexo_mascota.nombre, self.nombre)
	
class Tratamiento(models.Model):
	anexo_visita = models.ForeignKey(Visita, on_delete=models.CASCADE, related_name="AnexoTratamientoMascota", null=True, blank=True)
	descripcion = models.CharField("Detalle del Tratamiento", max_length=100, blank=True, null=True)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField(blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTratamiento")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTratamiento", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Tratamiento'
		verbose_name_plural = 'Tratamientos'

	def __str__(self):
		return "%s - %s" % (self.anexo_visita.anexo_mascota.nombre, self.descripcion)
	
class Diagnostico(models.Model):
	anexo_visita = models.ForeignKey(Visita, on_delete=models.CASCADE, related_name="AnexoDiagnosticoMascota", null=True, blank=True)
	descripcion = models.CharField("Detalle del Diagnostico", max_length=100, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionDiagnostico")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModDiagnostico", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Diagnostico'
		verbose_name_plural = 'Diagnosticos'

	def __str__(self):
		return "%s - %s" % (self.anexo_visita.anexo_mascota.nombre, self.descripcion)
	
class Productos(models.Model):
	descripcion = models.CharField("Nombre del Producto", max_length=100, blank=True, null=True)
	stock = models.IntegerField("Cantidad del Producto", blank=True, null=True)
	precio = models.DecimalField("Precio del Producto", max_digits=5, decimal_places=2, blank=True, null=True)
	archivo = models.FileField(null=True, blank=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionProductos")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModProductos", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'

	def __str__(self):
		return "%s - %s" % (self.descripcion, self.stock)
	
class TratamientosSlider(models.Model):
	descripcion = models.CharField("Nombre Tratamiento", max_length=50, blank=True, null=True)
	archivo = models.FileField(null=True, blank=True)
	visible = models.BooleanField(default=False)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTratamientosSlider")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTratamientosSlider", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Tratamientos Slider'
		verbose_name_plural = 'Tratamientos Slider'

	def __str__(self):
		return "%s" % (self.descripcion)
	
class FotosSlider(models.Model):
	descripcion = models.CharField("Nombre Imagen", max_length=50, blank=True, null=True)
	archivo = models.FileField(null=True, blank=True)
	visible = models.BooleanField(default=False)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionFotosSlider")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModFotosSlider", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Fotos Slider'
		verbose_name_plural = 'Fotos Slider'

	def __str__(self):
		return "%s" % (self.descripcion)