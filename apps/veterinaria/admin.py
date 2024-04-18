from django.contrib import admin
from .models import TratamientosSlider
from .models import Productos
#from .models import FotosSlider
from .models import Ventas
from .models import TipoAnimales

# Register your models here.
admin.site.register(TratamientosSlider)
admin.site.register(Productos)
#admin.site.register(FotosSlider)
admin.site.register(Ventas)
admin.site.register(TipoAnimales)