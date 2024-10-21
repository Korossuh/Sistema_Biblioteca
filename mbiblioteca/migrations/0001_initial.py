# Generated by Django 4.2.11 on 2024-10-20 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('biografia', models.TextField(max_length=200)),
                ('namiciento', models.DateTimeField()),
                ('nacionalidad', models.CharField(max_length=20)),
                ('estado', models.IntegerField(max_length=20)),
            ],
            options={
                'db_table': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editorial', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'editorial',
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'idioma',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField()),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbiblioteca.rol')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('fpublicacion', models.DateField()),
                ('stock', models.IntegerField()),
                ('nro_paginas', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbiblioteca.autor')),
                ('id_editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbiblioteca.editorial')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbiblioteca.idioma')),
            ],
            options={
                'db_table': 'libros',
            },
        ),
    ]