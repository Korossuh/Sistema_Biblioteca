from django import forms
from .models import *

class FormUsuario(forms.ModelForm):
    nombre= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese nombre'}))
    correo= forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Ingrese correo'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Ingrese contraseña'}))
    id_rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, widget=forms.Select(attrs={'placeholder': 'Seleccione su Rol'}))
    estado = forms.ChoiceField(
        widget=forms.Select(attrs={'placeholder': 'Seleccionar estado'}),
        choices=[(0, 'Inactivo'), (1, 'Activo')]
    )
    class Meta:
        model = Usuarios
        fields = ['nombre','correo','password','id_rol','estado']


class FormLibro(forms.ModelForm):
    titulo = forms.CharField(max_length=40)
    id_autor = forms.ModelChoiceField(queryset=Autor.objects.all(),required=True,widget=forms.Select(attrs={'placeholder':'Seleccione autor'}))
    fpublicacion = forms.DateField()
    id_editorial = forms.ModelChoiceField(queryset=Editorial.objects.all(),required=True,widget=forms.Select(attrs={'placeholder':'Seleccionar editorial'}))
    stock = forms.IntegerField()
    nro_paginas = forms.IntegerField()
    idioma = forms.ModelChoiceField(queryset=Idioma.objects.all(),required=True,widget=forms.Select(attrs={'placeholder':'Seleccione Idioma'}))
    estado = forms.IntegerField()

    class Meta:
        model = Libros
        fields = ['titulo','id_autor','fpublicacion','id_editorial','stock','nro_paginas','idioma','estado']

class BuscarLibro(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Buscar por título'}))