from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.base, name='base'),
    path('inicio/', views.inicio, name='inicio'),
    path('musicos/', views.musicos, name='musicos'),
    path('productos/', views.productos, name='productos'),
    path('lugares/', views.lugares, name='lugares'),
    path('mapa/', views.mapa, name='mapa'),
    path('perfil/', views.perfil, name='perfil'),
    path('banda/', views.banda, name='banda'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('ajustes/', views.ajustes, name='ajustes'),
    path('redes/', views.redessociales, name='redes'),
    path('manual/', views.manual, name='manual'),
    path('acercade/', views.acercade, name='acercade'),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=[
    path('perfil/crear/', views.CrearMusico.as_view()),
    path('perfil/<str:pk>/editar/', views.ActualizarMusico.as_view()),
    path('perfil/<str:pk>/eliminar/', views.EliminarMusico.as_view()),

    path('perfil/crear_estilo/', views.CrearEstilo.as_view()),
    path('perfil/<str:pk>/editar_estilo/', views.ActualizarEstilo.as_view()),
    path('perfil/<str:pk>/eliminar_estilo/', views.EliminarEstilo.as_view()),

    path('perfil/crear_multimedia/', views.CrearMultimedia.as_view()),
    path('perfil/<str:pk>/editar_multimedia/', views.ActualizarMultimedia.as_view()),
    path('perfil/<str:pk>/eliminar_multimedia/', views.EliminarMultimedia.as_view()),
    
    path('perfil/crear_datos/', views.CrearDatos.as_view()),
    path('perfil/<str:pk>/editar_datos/', views.ActualizarDatos.as_view()),
    path('perfil/<str:pk>/eliminar_datos/', views.EliminarDatos.as_view()),

    path('mensajes/enviar/', views.CrearMensaje.as_view()),

    path('musicos/contactar/', views.CrearContacto.as_view(), name='crear_contacto'),
    path('mensajes/<str:pk>/eliminar_contacto/', views.EliminarContacto.as_view()),

    path('inicio/anunciar/<str:pk>', views.CrearAnuncio.as_view()),

    path('inicio/contactanos/<str:pk>', views.CrearMensajeAdmin.as_view()),

]

