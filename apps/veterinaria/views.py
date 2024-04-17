from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from .utils import get_current_year

#FORMS
from .forms import UserVeterinariaForm, MascotaVeterinariaForm, ProductosForm

#MODELS
from .models import Personal, TratamientosSlider, Productos, FotosSlider, User, Visita

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
	form = MascotaVeterinariaForm(request.POST or None)
	year = get_current_year()
	context = {"form":form, "year": year,}
	return render(request, "historial_clinico.html", context)

def reservaMedica(request):
	year = get_current_year()
	context = {"year": year,}
	return render(request, "reserva_medica.html", context)

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
	year = get_current_year()
	user = User.objects.exclude(username='administrator')[::-1][:3][::-1]
	products = Productos.objects.all()[::-1][:3][::-1]
	context = {"users":user, "products":products, "year": year,}
	return render(request, "home.html", context)

@login_required
def visualizarUsuarios(request):
	year = get_current_year()
	user = User.objects.exclude(username='administrator')
	context = {"users":user, "year": year,}
	return render(request, "visualizar_usuarios.html", context)

@login_required
def venderProductos(request):
	form = ProductosForm(request.POST or None)
	year = get_current_year()
	context = {"form":form, "year":year}

	if request.method == "POST":
		if form.is_valid():
			result = form.save(commit=False)
			result.save()

			return redirect('vender_productos')
	return render(request, 'vender_productos.html', context)

@login_required
def visualizarProductos(request):
	year = get_current_year()
	products = Productos.objects.all()
	context = {"products":products, "year": year,}
	return render(request, "visualizar_productos.html", context)

@login_required
def visualizarVentas(request):
	year = get_current_year()
	context = {"year": year,}
	return render(request, "visualizar_ventas.html", context)

@login_required
def visualizarCitas(request):
	year = get_current_year()
	visits = Visita.objects.all()
	context = {"visits": visits, "year": year,}
	return render(request, "visualizar_citas.html", context)

@login_required
def registrarHistorial(request):
	year = get_current_year()
	context = {"year": year,}
	return render(request, "registrar_historial.html", context)

@login_required
def visualizarHistorial(request):
	year = get_current_year()
	context = {"year": year,}
	return render(request, "visualizar_historial_clinico.html", context)

def logoutWeb(request):
    logout(request)
    return redirect('/')