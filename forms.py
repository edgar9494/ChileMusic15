from django import forms
from .models import musico, estilo, multimedia, datos, mensaje, contacto, anuncio, mensajeadmin

class MusicoForms(forms.ModelForm):
    class meta:
        model = musico
        #fields = ('usuario','nombre',"sexo",'edad','carrera','region','comuna','disponibilidad','acceso', 'imagen')
        fields = '__all__'


class EstiloForms(forms.ModelForm):
    class meta:
        model = estilo
        fields = '__all__'

class MultimediaForm(forms.ModelForm):
    class Meta:
        model = multimedia
        fields = '__all__'
    
    imagen1 = forms.ImageField(required=False)
    imagen2 = forms.ImageField(required=False)
    imagen3 = forms.ImageField(required=False)
    imagen4 = forms.ImageField(required=False)
    imagen5 = forms.ImageField(required=False)
    
    video1 = forms.FileField(required=False)
    video2 = forms.FileField(required=False)
    video3 = forms.FileField(required=False)
    video4 = forms.FileField(required=False)
    video5 = forms.FileField(required=False)
    
    audio1 = forms.FileField(required=False)
    audio2 = forms.FileField(required=False)
    audio3 = forms.FileField(required=False)
    audio4 = forms.FileField(required=False)
    audio5 = forms.FileField(required=False)     

class DatosForms(forms.ModelForm):
    class meta:
        model = datos
        fields = '__all__'   

class MensajeForms(forms.ModelForm):
    class meta:
        model = mensaje
        fields = '__all__'                  

class ContactoForms(forms.ModelForm):
    class meta:
        model = contacto
        fields = '__all__'     

class AnuncioForms(forms.ModelForm):
    class meta:
        model = anuncio
        fields = '__all__'        

class MensajeAdminForms(forms.ModelForm):
    class meta:
        model = mensajeadmin
        fields = '__all__'               