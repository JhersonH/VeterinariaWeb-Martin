from django.shortcuts import render, redirect, get_object_or_404
from collections import Counter
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from .utils import get_current_year
from datetime import date
from collections import defaultdict

#FORMS
from .forms import UserVeterinariaForm, MascotaVeterinariaForm, VentasForm, ReservacionesForm, RegistrarProductosForm, PropietarioForm, HistoriaClinicaForm, DoctorForm, ReservacionesEditForm

#MODELS
from .models import TratamientosSlider, Productos, FotosSlider, User, Visita, Ventas, HistoriaClinica, Propietario, Mascota

meses_espanol = {
    1: 'ENERO', 2: 'FEBRERO', 3: 'MARZO', 4: 'ABRIL',
    5: 'MAYO', 6: 'JUNIO', 7: 'JULIO', 8: 'AGOSTO',
    9: 'SEPTIEMBRE', 10: 'OCTUBRE', 11: 'NOVIEMBRE', 12: 'DICIEMBRE'
}

# Create your views here.
def index(request):
	year = get_current_year()
	sliders = TratamientosSlider.objects.all()
	sliders_secundario = FotosSlider.objects.all()
	context = {
		"year": year,
		"sliders": sliders,
		"sliders_secundario": sliders_secundario
	}
	return render(request, "index.html", context)

def productos(request):
	year = get_current_year()
	products = Productos.objects.all()[:3]
	context = {
		"year": year,
		"products": products,
	}
	return render(request, "productos.html", context)

@login_required
def historialClinico(request):
	user_id = request.user.id
	propietario_id = Propietario.objects.get(anexo_usuarios=user_id)
	mascota_id = Mascota.objects.get(anexo_propietario=propietario_id)
	historics = HistoriaClinica.objects.filter(anexo_mascota=mascota_id)
	year = get_current_year()
	context = {"historics": historics, "year": year,}
	return render(request, "historial_clinico.html", context)

def reservaMedica(request):
	year = get_current_year()
	form = ReservacionesForm(request.POST or None)
	context = {"form": form, "year": year}

	if request.method == "POST":
		if form.is_valid():
			result = form.save(commit=False)
			result.save()

			return redirect('index')
	return render(request, 'reserva_medica.html', context)

def nuevoUsuario(request):
	form = UserVeterinariaForm(request.POST or None)
	year = get_current_year()
	context = {"form":form, "year":year}

	if request.method == "POST":
		if form.is_valid():
			result = form.save(commit=False)
			result.save()

			return redirect('index')
	return render(request, 'nuevo_usuario.html', context)

@login_required
def dashboard(request):
	if request.user.username == 'administrator':
		year = get_current_year()

		user = User.objects.exclude(username='administrator')[::-1][:3][::-1]
		userCard = User.objects.exclude(username='administrator')
		users_data = User.objects.values('date_joined__month', 'date_joined__year')
		users_by_month = Counter(f"{user['date_joined__month']:02d} {user['date_joined__year']}" for user in users_data)
		labels = []
		data = list(users_by_month.values())
		for month_year in users_by_month.keys():
			month, year = map(int, month_year.split())
			label = f"{meses_espanol[month]} {year}"
			labels.append(label)

		products = Productos.objects.all()[::-1][:3][::-1]
		productsCard = Productos.objects.all()
		products_data = Productos.objects.values('fecha_ingreso__month', 'fecha_ingreso__year')
		products_by_month = Counter(f"{product['fecha_ingreso__month']:02d} {product['fecha_ingreso__year']}" for product in products_data)
		labels_products = []
		data_products = list(products_by_month.values())
		for month_year in products_by_month.keys():
			month, year = map(int, month_year.split())
			label = f"{meses_espanol[month]} {year}"
			labels_products.append(label)

		sells = Ventas.objects.all()[::-1][:3][::-1]
		sells_data = Ventas.objects.values('fecha_hora_creacion__month', 'fecha_hora_creacion__year')
		sells_by_month = Counter(f"{sell['fecha_hora_creacion__month']:02d} {sell['fecha_hora_creacion__year']}" for sell in sells_data)
		labels_sells = []
		data_sells = list(sells_by_month.values())
		for month_year in sells_by_month.keys():
			month, year = map(int, month_year.split())
			label = f"{meses_espanol[month]} {year}"
			labels_sells.append(label)

		visits = Visita.objects.all()[::-1][:3][::-1]
		visitsCard = Visita.objects.all()
		visits_data = Visita.objects.values('fecha__month', 'fecha__year')
		visits_by_month = Counter(f"{visit['fecha__month']:02d} {visit['fecha__year']}" for visit in visits_data)
		labels_visits = []
		data_visits = list(visits_by_month.values())
		for month_year in visits_by_month.keys():
			month, year = map(int, month_year.split())
			label = f"{meses_espanol[month]} {year}"
			labels_visits.append(label)

		historics = HistoriaClinica.objects.all()
		historicsCard = HistoriaClinica.objects.all()[::-1][:3][::-1]
		context = {
			"users":user, "products":products, "sells":sells, "visits":visits, 
			"usersCard":userCard, "productsCard":productsCard, "historicsCard":historicsCard, "visitsCard":visitsCard, 
			"historics":historics, "year": year, "labels": labels, "data":data,
			"labels_visits": labels_visits, "data_visits":data_visits,
			"labels_products": labels_products, "data_products":data_products,
			"labels_sells": labels_sells, "data_sells":data_sells}
		return render(request, "home.html", context)
	else:
		return index(request)

@login_required
def visualizarUsuarios(request):
	year = get_current_year()
	users = User.objects.exclude(username='administrator')

	if request.method == 'POST':
		if 'crear_usuario' in request.POST:
			print(request.POST)
			form = UserVeterinariaForm(request.POST or None)
			if form.is_valid():
				result = form.save(commit=False)
				result.save()
				return JsonResponse({'success': True})
			else:
				return JsonResponse({'success': False, 'errors': 'Revisa el formulario por favor'}, status=400)
		
	create_form = UserVeterinariaForm()
	context = {
		"users": users,
		"year": year,
		"create_form": create_form,
	}
	return render(request, "visualizar_usuarios.html", context)

@login_required
def editarUsuarios(request, id):
	idUser = get_object_or_404(User, id=id)
	form = UserVeterinariaForm(request.POST or None, instance=idUser)
	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('visualizarUsuarios')
	return render(request, "editar_usuarios.html", context)

@login_required
def eliminarUsuarios(request, id):
	user = get_object_or_404(User, id=id)
	user.delete()
	return redirect('visualizarUsuarios')

@login_required
def venderProductos(request):
	form = VentasForm(request.POST or None)
	year = get_current_year()
	context = {"form":form, "year":year}

	if request.method == "POST":
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user

			producto_id = form.cleaned_data['anexo_producto'].id
			result.anexo_producto_id = producto_id

			result.save()

			producto = Productos.objects.get(id=producto_id)
			cantidad = result.cantidad
			producto.stock -= cantidad
			producto.save()

			return redirect('venderProductos')
	return render(request, 'vender_productos.html', context)

@login_required
def registrarProductos(request):
	year = get_current_year()
	form = RegistrarProductosForm(request.POST or None)
	context = {"form":form, "year": year,}

	if request.method == "POST":
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()

			return redirect('registrarProductos')
	return render(request, "registrar_productos.html", context)

@login_required
def visualizarProductos(request):
	year = get_current_year()
	products = Productos.objects.all()
	context = {"products": products,"year": year}

	return render(request, "visualizar_productos.html", context)

@login_required
def editarProductos(request, id):
	idProduct = get_object_or_404(Productos, id=id)

	if idProduct.fecha_ingreso:
		idProduct.fecha_ingreso = idProduct.fecha_ingreso.strftime('%Y-%m-%d')
	if idProduct.fecha_vencimiento:
		idProduct.fecha_vencimiento = idProduct.fecha_vencimiento.strftime('%Y-%m-%d')

	form = RegistrarProductosForm(request.POST or None, instance=idProduct)

	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('visualizarProductos')
	return render(request, "editar_productos.html", context)

@login_required
def eliminarProductos(request, id):
	product = get_object_or_404(Productos, id=id)
	product.delete()
	return redirect('visualizarProductos')

@login_required
def reporteProductos(request):
	year = get_current_year()
	products = Productos.objects.all()[::-1][:5][::-1]
	context = {"products":products, "year": year,}
	return render(request, "reporte_productos.html", context)

@login_required
def visualizarVentas(request):
	year = get_current_year()
	ventas = Ventas.objects.all()
	context = {"ventas": ventas, "year": year,}
	return render(request, "visualizar_ventas.html", context)

@login_required
def editarVentas(request, id):
	idVenta = get_object_or_404(Ventas, id=id)
	form = VentasForm(request.POST or None, instance=idVenta)

	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('visualizarVentas')
	return render(request, "editar_ventas.html", context)

@login_required
def eliminarVentas(request, id):
	product = get_object_or_404(Ventas, id=id)
	product.delete()
	return redirect('visualizarVentas')

@login_required
def reporteVentas(request):
	year = get_current_year()
	current_month = date.today().month
	sales = Ventas.objects.filter(fecha_hora_creacion__month=current_month)[::-1][:5][::-1]
	context = {"sales": sales, "year": year,}
	return render(request, "reporte_ventas.html", context)

@login_required
def visualizarCitas(request):
	year = get_current_year()
	visits = Visita.objects.all()

	for visit in visits:
		if visit.nota is None:
			visit.nota = ""

	if request.method == 'POST':
		if 'crear_cita' in request.POST:
			form = ReservacionesForm(request.POST or None)
			if form.is_valid():
				current_user = auth.get_user(request)
				result = form.save(commit=False)
				result.usuario_creacion = current_user
				result.save()
				return JsonResponse({'success': True})
			else:
				return JsonResponse({'success': False, 'errors': 'Revisa el formulario por favor'}, status=400)
		
	create_form = ReservacionesForm()
	context = {
		"visits": visits,
		"year": year,
		"create_form": create_form,
	}

	return render(request, "visualizar_citas.html", context)

@login_required
def editarCitas(request, id):
	idCita = get_object_or_404(Visita, id=id)

	if idCita.fecha:
		idCita.fecha = idCita.fecha.strftime('%Y-%m-%d')

	form = ReservacionesEditForm(request.POST or None, instance=idCita)

	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('visualizarCitas')
	return render(request, "editar_citas.html", context)

@login_required
def eliminarCitas(request, id):
	visita = get_object_or_404(Visita, id=id)
	visita.delete()
	return redirect('visualizarCitas')

@login_required
def reporteCitas(request):
    year = get_current_year()
    visits = Visita.objects.all()

    # Obtener las citas por mes y tipos de animales
    citas_por_mes_tipos = defaultdict(lambda: defaultdict(set))
    for visit in visits:
        mes = visit.fecha.strftime("%Y-%m")
        citas_por_mes_tipos[mes][visit.tipo].add(visit.mascota)

    # Contar la cantidad de tipos de animales por mes
    citas_por_mes_tipos_list = []
    for mes, tipos in citas_por_mes_tipos.items():
        cantidad_tipos = sum(len(mascotas) for mascotas in tipos.values())
        citas_por_mes_tipos_list.append((mes, cantidad_tipos))

    context = {
        "visits": visits,
        "year": year,
        "citas_por_mes_tipos": citas_por_mes_tipos_list,
    }
    return render(request, "reporte_citas.html", context)

@login_required
def registrarDoctor(request):
	form = DoctorForm(request.POST or None)
	year = get_current_year()
	context = {"form": form, "year": year,}

	if request.method == "POST":
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()

			return redirect('registrarDoctor')
	return render(request, "registrar_doctor.html", context)


@login_required
def registrarPropietario(request):
	form = PropietarioForm(request.POST or None)
	year = get_current_year()
	context = {"form": form, "year": year,}

	if request.method == "POST":
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()

			return redirect('registrarPropietario')
	return render(request, "registrar_propietario.html", context)

@login_required
def registrarMascota(request):
	form = MascotaVeterinariaForm(request.POST or None)
	year = get_current_year()
	context = {"form": form, "year": year,}

	if request.method == "POST":
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()

			return redirect('registrarMascota')
	return render(request, "registrar_mascota.html", context)

@login_required
def registrarHistorial(request):
	form = HistoriaClinicaForm(request.POST or None)
	year = get_current_year()
	context = {"form": form, "year": year,}

	if request.method == "POST":
		if form.is_valid():
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
			result.save()

			return redirect('registrarHistorial')
	return render(request, "registrar_historial.html", context)

@login_required
def visualizarHistorial(request):
	historics = HistoriaClinica.objects.all()
	year = get_current_year()
	context = {"historics": historics, "year": year,}
	return render(request, "visualizar_historial_clinico.html", context)

@login_required
def editarHistorial(request, id):
	idHistoria = get_object_or_404(HistoriaClinica, id=id)

	if idHistoria.fecha:
		idHistoria.fecha = idHistoria.fecha.strftime('%Y-%m-%d')

	form = HistoriaClinicaForm(request.POST or None, instance=idHistoria)

	context = {"form":form}
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('visualizarHistorial')
	return render(request, "editar_historial.html", context)

@login_required
def eliminarHistorial(request, id):
	visita = get_object_or_404(HistoriaClinica, id=id)
	visita.delete()
	return redirect('visualizarHistorial')

@login_required
def reporteGeneral(request):
	year = get_current_year()
	userCard = User.objects.exclude(username='administrator')
	users_data = User.objects.values('date_joined__month', 'date_joined__year')
	users_by_month = Counter(f"{user['date_joined__month']:02d} {user['date_joined__year']}" for user in users_data)
	labels = []
	data = list(users_by_month.values())
	for month_year in users_by_month.keys():
		month, year = map(int, month_year.split())
		label = f"{meses_espanol[month]} {year}"
		labels.append(label)

	context = {'year': year,'labels': labels, 'data': data}
	return render(request, 'reporte_general.html', context)

def logoutWeb(request):
    logout(request)
    return redirect('/')

#AJAX
def load_precios(request, id):
    precios = list(Productos.objects.filter(id=id).values('precio', 'stock'))
    return JsonResponse(precios,safe=False)

def users_chart(request):
	year = get_current_year()
	userCard = User.objects.exclude(username='administrator')
	users_data = User.objects.values('date_joined__month', 'date_joined__year')
	users_by_month = Counter(f"{user['date_joined__month']:02d} {user['date_joined__year']}" for user in users_data)
	labels = []
	label_dataset = 'Registros Mensuales - Usuarios'
	data = list(users_by_month.values())
	for month_year in users_by_month.keys():
		month, year = map(int, month_year.split())
		label = f"{meses_espanol[month]} {year}"
		labels.append(label)

	context = {'year': year, 'label_dataset': label_dataset, 'labels': labels, 'data': data}
	return render(request, 'reporte_general.html', context)

def products_chart(request):
	year = get_current_year()
	userCard = Productos.objects.all()
	users_data = Productos.objects.values('fecha_hora_creacion__month', 'fecha_hora_creacion__year')
	users_by_month = Counter(f"{user['fecha_hora_creacion__month']:02d} {user['fecha_hora_creacion__year']}" for user in users_data)
	labels = []
	label_dataset = 'Registros Mensuales - Productos'
	data = list(users_by_month.values())
	for month_year in users_by_month.keys():
		month, year = map(int, month_year.split())
		label = f"{meses_espanol[month]} {year}"
		labels.append(label)

	context = {'year': year, 'label_dataset': label_dataset, 'labels': labels, 'data': data}
	return render(request, 'reporte_general.html', context)

def sales_chart(request):
	year = get_current_year()
	userCard = Ventas.objects.all()
	users_data = Ventas.objects.values('fecha_hora_creacion__month', 'fecha_hora_creacion__year')
	users_by_month = Counter(f"{user['fecha_hora_creacion__month']:02d} {user['fecha_hora_creacion__year']}" for user in users_data)
	labels = []
	label_dataset = 'Registros Mensuales - Ventas'
	data = list(users_by_month.values())
	for month_year in users_by_month.keys():
		month, year = map(int, month_year.split())
		label = f"{meses_espanol[month]} {year}"
		labels.append(label)

	context = {'year': year, 'label_dataset': label_dataset, 'labels': labels, 'data': data}
	return render(request, 'reporte_general.html', context)

def dates_chart(request):
	year = get_current_year()
	userCard = Visita.objects.all()
	users_data = Visita.objects.values('fecha_hora_creacion__month', 'fecha_hora_creacion__year')
	users_by_month = Counter(f"{user['fecha_hora_creacion__month']:02d} {user['fecha_hora_creacion__year']}" for user in users_data)
	labels = []
	label_dataset = 'Registros Mensuales - Visitas'
	data = list(users_by_month.values())
	for month_year in users_by_month.keys():
		month, year = map(int, month_year.split())
		label = f"{meses_espanol[month]} {year}"
		labels.append(label)

	context = {'year': year, 'label_dataset': label_dataset, 'labels': labels, 'data': data}
	return render(request, 'reporte_general.html', context)

def record_chart(request):
	year = get_current_year()
	userCard = HistoriaClinica.objects.all()
	users_data = HistoriaClinica.objects.values('fecha_hora_creacion__month', 'fecha_hora_creacion__year')
	users_by_month = Counter(f"{user['fecha_hora_creacion__month']:02d} {user['fecha_hora_creacion__year']}" for user in users_data)
	labels = []
	label_dataset = 'Registros Mensuales - Historia Clinica'
	data = list(users_by_month.values())
	for month_year in users_by_month.keys():
		month, year = map(int, month_year.split())
		label = f"{meses_espanol[month]} {year}"
		labels.append(label)

	context = {'year': year, 'label_dataset': label_dataset, 'labels': labels, 'data': data}
	return render(request, 'reporte_general.html', context)