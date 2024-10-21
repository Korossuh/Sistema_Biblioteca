from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

def login(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        password = request.POST['password']

        try:
            usuario = Usuarios.objects.get(nombre=nombre, password=password)

            if usuario.estado == 2:
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                return redirect('inicio')

            else:
                messages.error(request, 'Usuario inactivo.')
        
        except Usuarios.DoesNotExist:
            messages.error(request, 'Credenciales inválidas.')

    return render(request, 'login/login.html')

def cerrarsesion(request):
    try:
        del request.session['usuario_id']
        del request.session['usuario_nombre']
    except KeyError:
        pass
    return redirect('login')


def index(request):
    return render(request,'principal/index.html')

def usuario(request):
    usuarios = Usuarios.objects.all()
    return render(request,'usuario/usuario.html',{'usuarios':usuarios})

def addUsuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = FormUsuario()
    return render(request,'usuario/formuser.html',{'form':form})

def modUsuario(request, id):
    usuarios = Usuarios.objects.get(pk = id)
    
    if request.method == 'POST':
        form = FormUsuario(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = FormUsuario(instance=usuarios)
    return render(request,'usuario/formuser.html',{'form':form})

def deleteUsuario(request,id):
    usuario = Usuarios.objects.get(pk = id)
    usuario.delete()
    return redirect('usuario')

def libro(request):
    libro = Libros.objects.all()
    return render(request,'libros/libro.html',{'libro':libro})

def addLibro(request):
    if request.method == 'POST':
        form = FormLibro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro')
    else:
        form = FormLibro()
    return render(request,'libros/formlibro.html',{'form':form})

def modLibro(request, id):
    libro = Libros.objects.get(pk = id)
    
    if request.method == 'POST':
        form = FormLibro(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro')
    else:
        form = FormLibro(instance=libro)
    return render(request,'libros/formlibro.html',{'form':form})

def deleteLibro(request,id):
    libro = Libros.objects.get(pk = id)
    libro.delete()
    return redirect('libro')

def buscarLibros(request):
    form = BuscarLibro()
    resultados = None
    if 'query' in request.GET:
        query = request.GET.get('query')
        resultados = Libros.objects.filter(titulo__icontains=query) 

    return render(request, 'buscador/buscador.html', {'form': form, 'resultados': resultados})

def autores(request):    
    autores = Autor.objects.all()  # Obtener todos los autores
    return render(request, 'autores/autores.html', {'autores': autores})