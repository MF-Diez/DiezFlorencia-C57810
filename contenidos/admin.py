from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Consejos)
admin.site.register(Musica)
admin.site.register(Herramientas)
admin.site.register(Profesionales)
