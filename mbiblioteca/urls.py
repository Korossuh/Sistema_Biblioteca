from django.urls import path
from .views import *
from mbiblioteca import views

urlpatterns = [
    #url para login
    path('',login,name='login'),
    #url para inicio admin
    path('Index/', index , name='index'),
    #url para CRUD Usuarios
    path('Usuario/',usuario, name='usuario'),
    path('AddUsuario/',addUsuario,name='addUsuario'),
    path('Modificar Usuario/<int:id>',views.modUsuario, name='modUsuario'),
    path('Eliminar Usuario/<int:id>',views.deleteUsuario, name='deleteUsuario'),
    #url para Crud Libros
    path('Libros/',libro, name='libro'),
    path('AddLibro/',addLibro, name='addLibro'),
    path('Modificar Libro/<int:id>',views.modLibro, name='modLibro'),
    path('Eliminar Libro/<int:id>',views.deleteLibro, name='deleteLibro'),
    #url cerrar sesion
    path('cerrarsesion/',cerrarsesion,name='cerrarsesion'),
    #url buscador
    path('Buscador/', views.buscarLibros, name='buscarLibro'),
    #url para ver Autores
    path('Autores/', autores,name='autores'),
    #url para no admin
    path('Inicio/', indexComun, name='inicioComun'),
    path('BuscadorLibros/',views.buscadorComun, name='buscadorComun'),
    path('AutoresVisualizar/', autoresComun, name='autoresComun')
]
