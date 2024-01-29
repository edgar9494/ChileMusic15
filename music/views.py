from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import musico, estilo, multimedia, datos, contacto, mensaje, anuncio, mensajeadmin
from . forms import MusicoForms, EstiloForms, MultimediaForm, DatosForms
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import requests

def base(request):
    return render(
        request,'base.html',
    )

def inicio(request):
    anuncios = anuncio.objects.all()
    contactos = contacto.objects.filter(usuario=request.user.username)

    return render(
        request,'inicio.html', {'anuncios': anuncios, 'contactos': contactos}
    )    

def musicos(request):
    musicos = musico.objects.all()
    estilos = estilo.objects.all()
    multimedias = multimedia.objects.all()
    datoss = datos.objects.all()
    contactos = contacto.objects.all()

    for x in contactos:
        if x.usuario == request.user.username:
            contacto_encontrado = True
            break

    return render(
        request,'musicos.html', {'musicos': musicos, 'estilos': estilos, 'multimedias': multimedias, 'datoss': datoss, 'contactos': contactos}
    )  

def productos(request):
    return render(
        request,'Productos.html', 
    )      

def lugares(request):
    return render(
        request,'lugares.html',
    )    

def mapa(request):
    return render(
        request,'mapa.html',
    )        

def perfil(request):
    #musicos = musico.objects.filter(usuario = 'edgar94')
    musicos = musico.objects.all()
    estilos = estilo.objects.all()
    multimedias = multimedia.objects.all()
    datoss = datos.objects.all()
    musico_encontrado = False
    estilo_encontrado = False
    multimedia_encontrado = False
    datos_encontrado = False
    for x in musicos:
        if x.usuario == request.user.username:
            musico_encontrado = True
            break
    for x in estilos:
        if x.usuario == request.user.username:
            estilo_encontrado = True
            break
    for x in multimedias:
        if x.usuario == request.user.username:
            multimedia_encontrado = True
            break
    for x in datoss:
        if x.usuario == request.user.username:
            datos_encontrado = True
            break            
    return render(request, 'perfil.html', {'musicos': musicos, 'estilos': estilos, 'multimedias': multimedias, 'datoss': datoss, 'musico_encontrado': musico_encontrado, 'estilo_encontrado': estilo_encontrado, 'multimedia_encontrado': multimedia_encontrado, 'datos_encontrado': datos_encontrado})


def banda(request):
    return render(
        request,'banda.html',
    )       

def mensajes(request):
    contactos = contacto.objects.filter(usuario=request.user.username)
    mensajes = mensaje.objects.filter(usuario=request.user.username) | mensaje.objects.filter(para=request.user.username)
    musicos = musico.objects.all()
    return render(request, 'mensajes.html', {'Contactos': contactos, 'Mensajes': mensajes, 'Musicos': musicos})

def favoritos(request):
    return render(
        request,'favoritos.html',
    )   

def ajustes(request):
    return render(
        request,'ajustes.html',
    )    

def login(request):
    return render(
        request,'login.html',
    )

def redessociales(request):
    return render(
        request,'RedesSociales.html',
    ) 

def manual(request):
    return render(
        request,'manual.html',
    ) 

def acercade(request):
    return render(
        request,'acercade.html',
    ) 

class CrearMusico(CreateView):
    model = musico
    #fields = ('usuario', 'nombre', 'sexo', 'edad', 'carrera', 'region', 'comuna', 'disponibilidad', 'acceso', 'imagen') 
    fields = '__all__'
    success_url = reverse_lazy('perfil') 

class ActualizarMusico(UpdateView):
    model = musico 
    fields = '__all__'   
    success_url = reverse_lazy('perfil') 

class EliminarMusico(DeleteView):
    model = musico
    success_url = reverse_lazy('perfil')

class ConsultarMusico(generic.DetailView):
    model=musico      

class CrearEstilo(CreateView):
    model = estilo 
    fields = '__all__'
    success_url = reverse_lazy('perfil')

class ActualizarEstilo(UpdateView):
    model = estilo 
    fields = '__all__'
    success_url = reverse_lazy('perfil')

class EliminarEstilo(DeleteView):
    model = estilo 
    success_url = reverse_lazy('perfil')         

class CrearMultimedia(CreateView):
    model = multimedia 
    form_class = MultimediaForm
    success_url = reverse_lazy('perfil') 

class ActualizarMultimedia(UpdateView):
    model = multimedia 
    form_class = MultimediaForm
    success_url = reverse_lazy('perfil')

class EliminarMultimedia(DeleteView):
    model = multimedia 
    success_url = reverse_lazy('perfil')    

class CrearDatos(CreateView):
    model = datos 
    fields = '__all__'
    success_url = reverse_lazy('perfil') 

class ActualizarDatos(UpdateView):
    model = datos 
    fields = '__all__'
    success_url = reverse_lazy('perfil') 

class EliminarDatos(DeleteView):
    model = datos 
    success_url = reverse_lazy('perfil')  

class CrearMensaje(CreateView):
    model = mensaje
    fields = '__all__'
    success_url = reverse_lazy('mensajes')  

class CrearContacto(CreateView):
    model = contacto
    fields = '__all__'
    success_url = reverse_lazy('mensajes')

class EliminarContacto(DeleteView):
    model = contacto
    success_url = reverse_lazy('mensajes')      

class CrearAnuncio(CreateView):
    model = anuncio
    fields = '__all__'
    success_url = reverse_lazy('inicio')  

class CrearMensajeAdmin(CreateView):
    model = mensajeadmin
    fields = '__all__'
    success_url = reverse_lazy('inicio')                

def cargar_imagen(request):
    if request.method == 'POST':
        form = MusicoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_exito')
    else:
        form = MusicoForms()
    return render(request, 'inicio.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
 

