from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Propietario(models.Model):
	anexo_usuarios = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AnexoUsuariosPropietario", null=True, blank=True)
	nombre = models.CharField("Nombre del Propietario", max_length=100, blank=True, null=True)
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
		return "%s - %s" % (self.anexo_usuarios.first_name, self.anexo_usuarios.last_name)

class Mascota(models.Model):
	anexo_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="AnexoPropietario", null=True, blank=True)
	nombre = models.CharField("Nombre de Mascota", max_length=100, blank=True, null=True)
	especie = models.CharField("Especie de Mascota", max_length=100, blank=True, null=True)
	raza = models.CharField("Raza de Mascota", max_length=100, blank=True, null=True)
	edad = models.CharField("Edad de Mascota", max_length=100, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionMascota")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModMascota", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Mascota'
		verbose_name_plural = 'Mascotas'

	def __str__(self):
		return "%s - %s" % (self.nombre, self.especie)
	
class HistoriaClinica(models.Model):
	anexo_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="AnexoMascota", null=True, blank=True)
	fecha = models.DateField()
	motivo = models.CharField("Motivo de Consulta", max_length=150, blank=True, null=True)
	diagnostico = models.CharField("Diagnóstico de Consulta", max_length=300, blank=True, null=True)
	tratamiento = models.CharField("Tratamiento de Consulta", max_length=300, blank=True, null=True)
	observaciones = models.CharField("Observaciones", max_length=150, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionHistoriaClinica")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModHistoriaClinica", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'HistoriaClinica'
		verbose_name_plural = 'HistoriasClinicas'

	def __str__(self):
		return "%s - %s" % (self.anexo_mascota.nombre, self.motivo)
	
class Visita(models.Model):
	mascota = models.CharField("Nombre de Mascota", max_length=150, blank=True, null=True)
	tipo = models.CharField("Tipo de Mascota", max_length=100, blank=True, null=True)
	fecha = models.DateField()
	motivo = models.CharField("Motivo de Visita", max_length=300, blank=True, null=True)
	nota = models.CharField("Notas adicionales", max_length=100, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionVisita")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModVisita", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Visita'
		verbose_name_plural = 'Visitas'

	def __str__(self):
		return "%s - %s" % (self.mascota, self.motivo)
	
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
		return "%s" % (self.descripcion)
	
class Ventas(models.Model):
	anexo_producto=models.ForeignKey(Productos, on_delete=models.CASCADE, related_name="AnexoProductoVentas",null=True, blank=True)
	precio = models.DecimalField("Precio del Producto", max_digits=5, decimal_places=2, blank=True, null=True)
	cantidad = models.IntegerField("Cantidad del Producto", blank=True, null=True)
	total = models.DecimalField("Total de Venta", max_digits=5, decimal_places=2, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionVentas")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModVentas", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Venta'
		verbose_name_plural = 'Ventas'

	def __str__(self):
		return "%s - %s" % (self.anexo_producto.descripcion, self.total)
	
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
	
class TipoAnimales(models.Model):
	tipo = models.CharField("Tipo de Animal", max_length=50, blank=True, null=True)
	
	usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UsercreacionTipoAnimal")
	fecha_hora_creacion = models.DateTimeField("Fecha y Hora de Creación", auto_now_add=True)
	usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserModTipoAnimal", null=True, blank=True)
	fecha_hora_modificacion = models.DateTimeField("Fecha y Hora de Modificación", null=True, blank=True)
	
	class Meta:
		verbose_name = 'Tipo de Animal'
		verbose_name_plural = 'Tipo de Animal'

	def __str__(self):
		return "%s" % (self.tipo)