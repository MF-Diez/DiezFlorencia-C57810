# Generated by Django 5.0.6 on 2024-07-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consejos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRed', models.CharField(max_length=50)),
                ('desarrollo', models.CharField(max_length=300)),
                ('nombreAutor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('funcion', models.CharField(max_length=300)),
                ('link', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=80)),
                ('estilo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Profesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
