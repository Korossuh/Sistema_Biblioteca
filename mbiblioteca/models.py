from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    biografia=models.TextField(max_length=600)
    namiciento = models.DateTimeField()
    nacionalidad = models.CharField(max_length=30)
    estado = models.IntegerField()
    
    class Meta:
        db_table = 'autores'

    def __str__(self):
        return self.nombre

class Idioma(models.Model):
    idioma=(models.CharField(max_length=100))
    
    class Meta:
        db_table = 'idioma'

    def __str__(self):
        return self.idioma

class Editorial(models.Model):
    editorial = (models.CharField(max_length=100))
    
    class Meta:
        db_table = 'editorial'
    
    def __str__(self):
        return self.editorial

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.nombre_rol

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.IntegerField()

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre

class Libros(models.Model):
    titulo = models.CharField(max_length=40)
    id_autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    fpublicacion = models.DateField()
    id_editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)
    stock = models.IntegerField()
    nro_paginas = models.IntegerField()
    idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE )
    estado = models.IntegerField()
    
    class Meta:
        db_table = 'libros'

    def __str__(self):
        return self.titulo

