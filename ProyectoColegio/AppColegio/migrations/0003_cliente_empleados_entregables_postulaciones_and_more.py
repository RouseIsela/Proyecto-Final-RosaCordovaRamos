# Generated by Django 4.1.5 on 2023-02-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppColegio', '0002_remove_entregable_imagen_remove_opiniones_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('categoria', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Entregables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreservicio', models.CharField(max_length=40)),
                ('cliente', models.CharField(max_length=40)),
                ('fecha_de_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Postulaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('experiencia', models.CharField(max_length=30)),
                ('sitiolaboralpasado', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=100)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
