from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from .utils import get_current_year
from datetime import datetime, date

#FORMS
from .forms import UserVeterinariaForm, MascotaVeterinariaForm, VentasForm, ReservacionesForm, RegistrarProductosForm, PropietarioForm, HistoriaClinicaForm

#MODELS
from .models import TratamientosSlider, Productos, FotosSlider, User, Visita, Ventas, HistoriaClinica, Propietario, Mascota

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
			current_user = auth.get_user(request)
			result = form.save(commit=False)
			result.usuario_creacion = current_user
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
		products = Productos.objects.all()[::-1][:3][::-1]
		sells = Ventas.objects.all()[::-1][:3][::-1]
		visits = Visita.objects.all()[::-1][:3][::-1]
		historics = HistoriaClinica.objects.all()[::-1][:3][::-1]
		context = {"users":user, "products":products, "sells":sells, "visits":visits, "historics":historics, "year": year}
		return render(request, "home.html", context)
	else:
		return index(request)

@login_required
def visualizarUsuarios(request):
	year = get_current_year()
	user = User.objects.exclude(username='administrator')
	context = {"users":user, "year": year,}
	return render(request, "visualizar_usuarios.html", context)

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
			result.save()

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
	context = {"products":products, "year": year,}
	return render(request, "visualizar_productos.html", context)

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

	context = {"visits": visits, "year": year,}
	return render(request, "visualizar_citas.html", context)

@login_required
def reporteCitas(request):
	year = get_current_year()
	visits = Visita.objects.all()[::-1][:5][::-1]
	context = {"visits": visits, "year": year,}
	return render(request, "reporte_citas.html", context)

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

def logoutWeb(request):
    logout(request)
    return redirect('/')

#AJAX
def load_precios(request, id):
    precios = list(Productos.objects.filter(id=id).values('precio'))
    return JsonResponse(precios,safe=False)