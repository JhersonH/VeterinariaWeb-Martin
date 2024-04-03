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
from .forms import UserVeterinariaForm, MascotaVeterinariaForm

#MODELS
from .models import Personal, TratamientosSlider, Productos, FotosSlider, User

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
	products = Productos.objects.all()
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
	user = User.objects.all()
	context = {"users":user, "year": year,}
	return render(request, "home.html", context)

def logoutWeb(request):
    logout(request)
    return redirect('/')