from django.urls import path
from .views import *
from mbiblioteca import views

urlpatterns = [
    path('',login,name='login'),
    path('Inicio/', index , name='inicio'),
    path('Usuario/',usuario, name='usuario'),
    path('AddUsuario/',addUsuario,name='addUsuario'),
    path('Modificar Usuario/<int:id>',views.modUsuario, name='modUsuario'),
    path('Eliminar Usuario/<int:id>',views.deleteUsuario, name='deleteUsuario'),
    path('Libros/',libro, name='libro'),
    path('AddLibro/',addLibro, name='addLibro'),
    path('Modificar Libro/<int:id>',views.modLibro, name='modLibro'),
    path('Eliminar Libro/<int:id>',views.deleteLibro, name='deleteLibro'),
    path('cerrarsesion/',cerrarsesion,name='cerrarsesion'),
    path('Buscador/', views.buscarLibros, name='buscarLibro'),
    path('Autores/', autores,name='autores')
]
