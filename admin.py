from django.contrib import admin
from .models import musico, estilo, multimedia, datos, contacto, mensaje, anuncio, mensajeadmin

admin.site.register(musico)
admin.site.register(estilo)
admin.site.register(multimedia)
admin.site.register(datos)
admin.site.register(contacto)
admin.site.register(mensaje)
admin.site.register(anuncio)
admin.site.register(mensajeadmin)
# Register your models here.
